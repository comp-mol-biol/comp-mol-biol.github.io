#!/usr/bin/env python3
"""
Refresh _data/citation_data.json from live sources.

Primary source: Semantic Scholar author endpoint (gives title, year, DOI,
authors, and a live citation count in a single request). Secondary source:
the ORCID public API, used only to catch very new works (typically
preprints) that Semantic Scholar hasn't indexed yet -- for those we try one
extra Semantic Scholar DOI lookup, and fall back to ORCID's own title/year
with citation_count 0 if that paper isn't indexed there either.

Every candidate DOI (before deduplication) is also checked against Crossref
to see whether it's still a preprint (type "posted-content") rather than a
peer-reviewed article, so the site can show a "Preprint" indicator. This
check has to happen before deduplication, and deduplication has to prefer
a non-preprint sibling when one exists rather than just picking whichever
DOI has the higher citation_count -- see the comment on dedupe_by_title()
for why relying on citation_count alone previously mislabelled papers that
had already been published as "still a preprint".

No API keys required; all three APIs are public and CORS-friendly.

Usage: python3 scripts/update_citations.py
Writes: _data/citation_data.json (sorted newest-first)
"""

import json
import pathlib
import sys
import urllib.error
import urllib.request

ORCID_ID = "0000-0002-5348-0277"
SEMANTIC_SCHOLAR_AUTHOR_ID = "5059616"
OUTPUT_PATH = pathlib.Path(__file__).resolve().parent.parent / "_data" / "citation_data.json"

USER_AGENT = "comp-mol-biol.github.io citation updater (mailto:lstelzl@uni-mainz.de)"


def fetch_json(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def normalize_doi(doi):
    if not doi:
        return None
    return doi.strip().lower().removeprefix("https://doi.org/").removeprefix("doi:")


def fetch_semantic_scholar_papers():
    url = (
        f"https://api.semanticscholar.org/graph/v1/author/{SEMANTIC_SCHOLAR_AUTHOR_ID}"
        "?fields=name,papers.title,papers.year,papers.publicationDate,"
        "papers.citationCount,papers.externalIds,papers.authors"
    )
    data = fetch_json(url)
    by_doi = {}
    for p in data.get("papers", []):
        doi = normalize_doi((p.get("externalIds") or {}).get("DOI"))
        if not doi:
            continue
        by_doi[doi] = {
            "doi": f"https://doi.org/{doi}",
            "title": p.get("title") or "",
            "authors": [a.get("name", "") for a in (p.get("authors") or [])],
            "publication_date": p.get("publicationDate") or (str(p["year"]) if p.get("year") else ""),
            "citation_count": p.get("citationCount") or 0,
        }
    return by_doi


def fetch_semantic_scholar_by_doi(doi):
    url = (
        f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}"
        "?fields=title,year,publicationDate,citationCount,authors"
    )
    try:
        p = fetch_json(url)
    except urllib.error.HTTPError:
        return None
    return {
        "doi": f"https://doi.org/{doi}",
        "title": p.get("title") or "",
        "authors": [a.get("name", "") for a in (p.get("authors") or [])],
        "publication_date": p.get("publicationDate") or (str(p["year"]) if p.get("year") else ""),
        "citation_count": p.get("citationCount") or 0,
    }


def fetch_orcid_works():
    url = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"
    data = fetch_json(url, headers={"Accept": "application/json"})
    works = []
    for group in data.get("group", []):
        doi = None
        for eid in (group.get("external-ids") or {}).get("external-id", []):
            if eid.get("external-id-type") == "doi":
                doi = normalize_doi(eid.get("external-id-value"))
                break
        if not doi:
            continue
        summary = (group.get("work-summary") or [{}])[0]
        title = ((summary.get("title") or {}).get("title") or {}).get("value") or ""
        year = ((summary.get("publication-date") or {}).get("year") or {}).get("value")
        works.append({"doi": doi, "title": title, "publication_date": year or ""})
    return works


# DOI prefixes of known preprint servers, used only if the Crossref lookup
# below fails (e.g. a transient error) -- Crossref's own "posted-content"
# type is the primary, more general signal.
PREPRINT_DOI_PREFIXES = (
    "10.1101/",    # bioRxiv / medRxiv (legacy prefix)
    "10.64898/",   # bioRxiv (openRxiv, current prefix)
    "10.26434/",   # chemRxiv
    "10.21203/",   # Research Square
    "10.48550/",   # arXiv
)


def fetch_crossref_work(doi):
    url = f"https://api.crossref.org/works/{doi}"
    try:
        data = fetch_json(url)
    except (urllib.error.HTTPError, urllib.error.URLError):
        return None
    return data.get("message") or {}


def fetch_crossref_metadata(doi):
    """
    Returns {"is_preprint": bool, "published_doi": str or None}.
    published_doi comes from Crossref's own "is-preprint-of" relation,
    which some preprint servers (bioRxiv included) assert once a paper is
    published -- this is far more reliable than matching titles, since a
    paper's title sometimes changes between preprint and publication (see
    dedupe_by_title()'s docstring for a real example of that happening).
    """
    work = fetch_crossref_work(doi)
    if work is None:
        return {"is_preprint": doi.startswith(PREPRINT_DOI_PREFIXES), "published_doi": None}

    is_pre = work.get("type") == "posted-content"
    published_doi = None
    if is_pre:
        relations = (work.get("relation") or {}).get("is-preprint-of") or []
        for rel in relations:
            if rel.get("id-type") == "doi":
                published_doi = normalize_doi(rel.get("id"))
                break
    return {"is_preprint": is_pre, "published_doi": published_doi}


def fetch_crossref_basic_entry(doi):
    """Minimal entry built from Crossref alone, for a published DOI that
    Semantic Scholar doesn't have indexed yet."""
    work = fetch_crossref_work(doi)
    if not work:
        return None
    title = (work.get("title") or [""])[0]
    authors = [
        " ".join(part for part in (a.get("given"), a.get("family")) if part)
        for a in (work.get("author") or [])
    ]
    date_parts = (
        (work.get("published") or work.get("published-print") or work.get("published-online") or {})
        .get("date-parts", [[]])[0]
    )
    publication_date = "-".join(f"{p:02d}" if i else str(p) for i, p in enumerate(date_parts))
    return {
        "doi": f"https://doi.org/{doi}",
        "title": title,
        "authors": authors,
        "publication_date": publication_date,
        "citation_count": 0,
    }


def resolve_preprint_supersessions(by_doi):
    """
    For every preprint that Crossref says has since been published, fold it
    into that published DOI (adding the published entry from Semantic
    Scholar / Crossref if we don't have it yet) instead of leaving the
    stale preprint entry to be matched -- or missed -- by title alone.
    """
    for doi in list(by_doi):
        entry = by_doi[doi]
        published_doi = entry.get("published_doi")
        if not entry.get("is_preprint") or not published_doi:
            continue

        if published_doi not in by_doi:
            found = fetch_semantic_scholar_by_doi(published_doi) or fetch_crossref_basic_entry(published_doi)
            if not found:
                continue  # can't resolve it yet; leave the preprint entry as-is
            found["is_preprint"] = False
            found["published_doi"] = None
            by_doi[published_doi] = found
            print(f"  resolved preprint -> published: {entry['title'][:60]}", file=sys.stderr)

        target = by_doi[published_doi]
        target["citation_count"] = max(target.get("citation_count") or 0, entry.get("citation_count") or 0)
        del by_doi[doi]


def sort_key(entry):
    date = entry.get("publication_date") or "0000"
    return date


def normalize_title(title):
    return "".join(ch.lower() for ch in title if ch.isalnum())


def dedupe_by_title(entries):
    """
    ORCID often lists a preprint (chemRxiv/bioRxiv) and its later published
    version as separate DOIs with the same title. We must not pick the
    "winner" by citation_count alone: Semantic Scholar frequently keeps
    tracking citations against the preprint DOI for a while after the
    paper is actually published, so the preprint can show *more* citations
    than the brand-new published record. Picking by citation_count then
    keeps the preprint DOI around (and flags a now-published paper as a
    preprint).

    So: each entry must already have "is_preprint" set (see is_preprint())
    before calling this. Within a title group we always prefer a
    non-preprint (published) entry if one exists, and only fall back to
    the preprint entries if every sibling is still a preprint. Either way,
    we report the highest citation_count seen across the whole group, so a
    published paper doesn't under-report citations that Semantic Scholar
    only attached to its preprint sibling.
    """
    groups = {}
    for e in entries:
        groups.setdefault(normalize_title(e["title"]), []).append(e)

    deduped = []
    for group in groups.values():
        published = [e for e in group if not e.get("is_preprint")]
        candidates = published or group
        best = dict(max(candidates, key=lambda e: (e.get("citation_count") or 0, e.get("publication_date") or "")))
        best["citation_count"] = max((e.get("citation_count") or 0) for e in group)
        deduped.append(best)
    return deduped


def main():
    print(f"Fetching Semantic Scholar author {SEMANTIC_SCHOLAR_AUTHOR_ID} ...", file=sys.stderr)
    by_doi = fetch_semantic_scholar_papers()
    print(f"  -> {len(by_doi)} papers with DOIs", file=sys.stderr)

    print(f"Fetching ORCID {ORCID_ID} works ...", file=sys.stderr)
    orcid_works = fetch_orcid_works()
    print(f"  -> {len(orcid_works)} works with DOIs", file=sys.stderr)

    missing = [w for w in orcid_works if w["doi"] not in by_doi]
    print(f"  -> {len(missing)} not already covered by Semantic Scholar", file=sys.stderr)

    for w in missing:
        enriched = fetch_semantic_scholar_by_doi(w["doi"])
        if enriched:
            by_doi[w["doi"]] = enriched
            print(f"  enriched via Semantic Scholar: {w['title'][:70]}", file=sys.stderr)
        else:
            by_doi[w["doi"]] = {
                "doi": f"https://doi.org/{w['doi']}",
                "title": w["title"],
                "authors": [],
                "publication_date": str(w["publication_date"]),
                "citation_count": 0,
            }
            print(f"  added from ORCID only (not yet indexed): {w['title'][:70]}", file=sys.stderr)

    print("Checking preprint status via Crossref ...", file=sys.stderr)
    for doi, e in by_doi.items():
        meta = fetch_crossref_metadata(doi)
        e["is_preprint"] = meta["is_preprint"]
        e["published_doi"] = meta["published_doi"]
    preprint_count = sum(1 for e in by_doi.values() if e["is_preprint"])
    print(f"  -> {preprint_count} of {len(by_doi)} candidate DOIs are preprints", file=sys.stderr)

    resolve_preprint_supersessions(by_doi)
    for e in by_doi.values():
        e.pop("published_doi", None)

    entries = dedupe_by_title(by_doi.values())
    removed = len(by_doi) - len(entries)
    if removed:
        print(f"Dropped {removed} duplicate-title entries, preferring the published version when one exists", file=sys.stderr)
    final_preprint_count = sum(1 for e in entries if e["is_preprint"])
    print(f"  -> {final_preprint_count} of {len(entries)} entries are still preprints after dedup", file=sys.stderr)

    entries = sorted(entries, key=sort_key, reverse=True)

    OUTPUT_PATH.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(entries)} entries to {OUTPUT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
