---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<!-- Sorting controls -->
<div class="sorting-controls">
  <label>Sort by:</label>
  <button id="sort-by-date" class="sort-button active">Publication Date</button>
  <button id="sort-by-citation" class="sort-button">Citation Count</button>
</div>

<!-- Publications container -->
<div id="publications-container">
  {% for paper in site.data.citation_data %}
    <div class="archive__item" data-citation="{{ paper.citation_count }}" data-date="{{ paper.publication_date }}">
      <h2 class="archive__item-title">
        <a href="{{ paper.doi }}" target="_blank">{{ paper.title }}</a>
        {% if paper.is_preprint %}<span class="preprint-badge" title="Not yet peer-reviewed">Preprint</span>{% endif %}
      </h2>
      <p class="archive__item-excerpt">
        {% for author in paper.authors %}
          {% if forloop.last and paper.authors.size > 1 %}
            and {{ author }}
          {% else %}
            {{ author }}{% unless forloop.last %}, {% endunless %}
          {% endif %}
        {% endfor %}
      </p>
      <p class="archive__item-excerpt">
        <strong>Citation Count:</strong> {{ paper.citation_count }}
        {% if paper.publication_date != "" %}
          <br><strong>Published:</strong> {{ paper.publication_date }}
        {% endif %}
      </p>
    </div>
  {% endfor %}
</div>

<!-- JavaScript for sorting -->
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const publicationsContainer = document.getElementById('publications-container');
    const sortByCitationBtn = document.getElementById('sort-by-citation');
    const sortByDateBtn = document.getElementById('sort-by-date');

    /* Get all publication items */
    let publications = Array.from(publicationsContainer.children);

    /* Sort by citation count (descending) */
    function sortByCitation() {
      publications.sort((a, b) => {
        const citationA = parseInt(a.getAttribute('data-citation'));
        const citationB = parseInt(b.getAttribute('data-citation'));
        return citationB - citationA; /* descending order */
      });
      updatePublications();
      setActiveButton(sortByCitationBtn);
    }

    /* Sort by publication date (descending) with year grouping */
    function sortByDate() {
      publications.sort((a, b) => {
        const dateA = a.getAttribute('data-date');
        const dateB = b.getAttribute('data-date');

        /* handle empty dates */
        if (!dateA && !dateB) return 0;
        if (!dateA) return 1;
        if (!dateB) return -1;

        /* parse dates (assuming format like "YYYY-MM-DD") */
        const dateObjA = new Date(dateA);
        const dateObjB = new Date(dateB);

        return dateObjB - dateObjA; /* descending order */
      });

      /* group by year and add year headers */
      updatePublicationsWithYearGrouping();
      setActiveButton(sortByDateBtn);
    }

    /* Update the DOM with sorted publications and year grouping */
    function updatePublicationsWithYearGrouping() {
      publicationsContainer.innerHTML = '';

      let currentYear = null;
      let yearGroup = [];

      publications.forEach(pub => {
        const date = pub.getAttribute('data-date');
        if (!date) {
          /* add to current year group if no date */
          yearGroup.push(pub);
          return;
        }

        const year = new Date(date).getFullYear();

        /* if year changed, add year header and previous year's publications */
        if (year !== currentYear) {
          if (currentYear !== null) {
            /* add year header */
            const yearHeader = document.createElement('h3');
            yearHeader.className = 'year-header';
            yearHeader.textContent = currentYear;
            publicationsContainer.appendChild(yearHeader);

            /* add publications for previous year */
            yearGroup.forEach(pubItem => publicationsContainer.appendChild(pubItem));
            yearGroup = [];
          }
          currentYear = year;
        }

        yearGroup.push(pub);
      });

      /* add the last year's publications */
      if (currentYear !== null) {
        const yearHeader = document.createElement('h3');
        yearHeader.className = 'year-header';
        yearHeader.textContent = currentYear;
        publicationsContainer.appendChild(yearHeader);

        yearGroup.forEach(pubItem => publicationsContainer.appendChild(pubItem));
      }
    }

    /* Update the DOM with sorted publications (without year grouping) */
    function updatePublications() {
      publicationsContainer.innerHTML = '';
      publications.forEach(pub => publicationsContainer.appendChild(pub));
    }

    /* Set active button */
    function setActiveButton(activeBtn) {
      sortByCitationBtn.classList.remove('active');
      sortByDateBtn.classList.remove('active');
      activeBtn.classList.add('active');
    }

    /* add event listeners */
    sortByCitationBtn.addEventListener('click', sortByCitation);
    sortByDateBtn.addEventListener('click', sortByDate);

    /* initialize with date sorting */
    sortByDate();
  });
</script>
