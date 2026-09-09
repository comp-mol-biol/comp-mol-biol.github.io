---
permalink: /
title: "Biomolecular Simulation"
excerpt: "Resolving dynamic self-organization in cells by multi-scale simulations."
layout: single
author_profile: true
header:
  overlay_image: mut16_interactions_heroband.jpg
  overlay_filter: 0.5
  caption: "Slab simulation of a phase-separated condensate of MUT-16 foci-forming region chains (Gaurav et al., eLife 2026)."
---

<h1 class="home-welcome">Welcome to our Lab</h1>

<div class="home-slideshow" data-interval="5000">
  <img src="/images/group_picutre_winter.png" alt="The Stelzl Lab group">
  <img src="/images/group_picture_komet.png" alt="">
  <img src="/images/profile_pic.png" alt="">
  <div class="home-slideshow__dots"></div>
</div>
<script>
  (function () {
    var box = document.currentScript.previousElementSibling;
    var slides = box.querySelectorAll('img');
    var dotsWrap = box.querySelector('.home-slideshow__dots');
    var n = slides.length, i = 0, dots = [], timer;

    for (var k = 0; k < n; k++) {
      var d = document.createElement('button');
      d.type = 'button';
      d.className = 'home-slideshow__dot';
      d.setAttribute('aria-label', 'Show group photo ' + (k + 1));
      dotsWrap.appendChild(d);
      dots.push(d);
      d.addEventListener('click', (function (idx) {
        return function () { show(idx); restart(); };
      })(k));
    }

    function show(idx) {
      slides[i].classList.remove('is-active');
      dots[i].classList.remove('is-active');
      i = (idx + n) % n;
      slides[i].classList.add('is-active');
      dots[i].classList.add('is-active');
    }

    function start() {
      if (!window.matchMedia || !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        timer = setInterval(function () { show(i + 1); }, parseInt(box.getAttribute('data-interval'), 10) || 5000);
      }
    }
    function restart() { clearInterval(timer); start(); }

    show(0);
    start();
  })();
</script>

The Stelzl Lab is a computational biophysics research group at the [Institute of Molecular Physiology (imP)](https://www.bio.uni-mainz.de/imp/), Johannes Gutenberg University Mainz, led by Prof. Dr. Lukas Stelzl. We use multi-scale molecular simulations, from atomistic detail to residue-level and coarse-grained models, to understand how biomolecular condensates and liquid-liquid phase separation regulate gene expression in health, ageing, and disease.

<div class="home-links">
  <a class="home-links__card" href="/research/">
    <h3>Research</h3>
    <p>Multi-scale simulations of biomolecular condensates and liquid-liquid phase separation.</p>
  </a>
  <a class="home-links__card" href="/group/">
    <h3>Group</h3>
    <p>Meet the PI, students, research assitants and alumni of the lab.</p>
  </a>
  <a class="home-links__card" href="/publications/">
    <h3>Publications</h3>
    <p>Our papers on condensates, disordered proteins, and multi-scale methods and more.</p>
  </a>
  <a class="home-links__card" href="/contact/">
    <h3>Contact</h3>
    <p>Find us at the Institute of Molecular Physiology (imP), JGU Mainz.</p>
  </a>
</div>

## Funding

Our research is supported by:

<div class="funding-logos">
  <a href="https://www.dfg.de/de" target="_blank" rel="noopener" title="Deutsche Forschungsgemeinschaft (DFG)">
    <img src="/images/dfg_cropped.jpeg" alt="Deutsche Forschungsgemeinschaft (DFG)" loading="lazy">
  </a>
  <a href="https://trr146.uni-mainz.de/" target="_blank" rel="noopener" title="CRC/TRR 146 — Multiscale Simulation Methods for Soft Matter Systems">
    <img src="/images/logo-trr146.jpg" alt="CRC/TRR 146" loading="lazy">
  </a>
  <a href="https://crc1551.com/" target="_blank" rel="noopener" title="CRC/SFB 1551 — Polymer Concepts in Cellular Function">
    <img src="/images/sfb1551_logo_cropped-300x120.png" alt="CRC/SFB 1551" loading="lazy">
  </a>
  <a href="https://sfb1552.de/" target="_blank" rel="noopener" title="CRC/SFB 1552 — Defiance">
    <img src="/images/LogoSFB1552-dark.svg" alt="CRC/SFB 1552" loading="lazy">
  </a>
  <a href="https://grk2516.uni-mainz.de/" target="_blank" rel="noopener" title="Research Training Group GRK 2516">
    <img src="/images/GRK2516_logo-300x300.jpg" alt="Research Training Group GRK 2516" loading="lazy">
  </a>
  <a href="https://www.mpgc-mainz.de/494575/Molecular-and-Materials-AI" target="_blank" rel="noopener" title="Max Planck Graduate Center with the Johannes Gutenberg University (MPGC)">
    <img src="/images/Logo-MPGC-_long-version_.jpg" alt="Max Planck Graduate Center (MPGC)" loading="lazy">
  </a>
  <a href="https://reality.uni-mainz.de/" target="_blank" rel="noopener" title="ReALity — Resilience, Adaptation and Longevity">
    <img src="/images/JGU_Logo_ReALity_Claim_200220_RGB_cropped.jpg" alt="ReALity — Resilience, Adaptation and Longevity" loading="lazy">
  </a>
  <a href="https://model.uni-mainz.de/" target="_blank" rel="noopener" title="M³ODEL — Mainz Institute of Multiscale Modeling">
    <img src="/images/logo_m3odel.png" alt="M³ODEL" loading="lazy">
  </a>
  <a href="https://mwwg.rlp.de/themen/wissenschaft/forschung/forschung-an-hochschulen/forschungsinitiative" target="_blank" rel="noopener" title="Forschungsinitiative des Landes Rheinland-Pfalz">
    <img src="/images/logo_forschungsinitiative_RLP_transparent.png" alt="Forschungsinitiative des Landes Rheinland-Pfalz" loading="lazy">
  </a>
  <a href="https://www.carl-zeiss-stiftung.de/" target="_blank" rel="noopener" title="Carl-Zeiss-Stiftung">
    <img src="/images/CZS_RGB_pos_Logo_web.png" alt="Carl-Zeiss-Stiftung" loading="lazy">
  </a>
</div>
