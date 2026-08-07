// ─── Theme ───────────────────────────────────────────────────────────────────
// The button shows a moon (switch to dark) or sun (switch to light) icon, swapped
// purely in CSS via [data-theme]. JS only flips the attribute + persists choice.
function toggleTheme() {
  const b = document.body;
  const next = b.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
  const apply = () => {
    b.setAttribute('data-theme', next);
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('lm_theme', next);
  };
  // Crossfade the whole page (logo, hero image and colours together) via the
  // native View Transitions API; browsers without it just swap instantly.
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (document.startViewTransition && !reduce) {
    document.startViewTransition(apply);
  } else {
    apply();
  }
}
// Initial theme is applied pre-paint by an inline script in base.html (default
// dark; a saved 'light'/'dark' choice wins) — no flash, so nothing to do here.

// ─── Nav ─────────────────────────────────────────────────────────────────────
function toggleNav() {
  document.getElementById('navLinks').classList.toggle('open');
}

// ─── Search bar toggle ─────────────────────────────────────────────────────────
function toggleSearch() {
  const bar = document.getElementById('searchBar');
  if (!bar) return;
  bar.classList.toggle('open');
  if (bar.classList.contains('open')) {
    const inp = document.getElementById('searchInput');
    if (inp) setTimeout(() => inp.focus(), 100);
  }
}

// ─── Tabs ────────────────────────────────────────────────────────────────────
function switchTab(id, btn) {
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  const el = document.getElementById('tab-' + id);
  if (el) el.classList.add('active');
  if (btn) btn.classList.add('active');
}

// ─── FAQ ─────────────────────────────────────────────────────────────────────
function toggleFaq(el) {
  el.classList.toggle('open');
}

// ─── Cookie ──────────────────────────────────────────────────────────────────
function acceptCookie() { setCookieChoice('accepted'); }
function declineCookie() { setCookieChoice('declined'); }
function setCookieChoice(value) {
  const banner = document.getElementById('cookieBanner');
  if (banner) banner.classList.add('hidden');
  localStorage.setItem('lm_cookie', value);
}
if (localStorage.getItem('lm_cookie')) {
  const banner = document.getElementById('cookieBanner');
  if (banner) banner.classList.add('hidden');
}

// ─── Scroll hint (hide once the user scrolls) ──────────────────────────────────
(function () {
  const hint = document.getElementById('scrollHint');
  if (!hint) return;
  window.addEventListener('scroll', function () {
    if (window.scrollY > 40) {
      hint.style.opacity = '0';
      hint.style.pointerEvents = 'none';
    } else {
      hint.style.opacity = '1';
    }
  }, { passive: true });
})();

// ─── Share modal ───────────────────────────────────────────────────────────────
let shareData = { title: '', url: '' };
function openShare(title, url) {
  shareData.title = title || document.title;
  shareData.url = url || window.location.href;
  const t = document.getElementById('shareTitle');
  if (t) t.textContent = shareData.title;
  const copied = document.getElementById('shareCopied');
  if (copied) copied.classList.remove('show');
  // Show "More options" only if the device supports the native share sheet
  const moreBtn = document.getElementById('shareMoreBtn');
  if (moreBtn) moreBtn.style.display = navigator.share ? 'flex' : 'none';
  document.getElementById('shareOverlay').classList.add('open');
}
function closeShare() {
  document.getElementById('shareOverlay').classList.remove('open');
}
function shareWhatsApp() {
  const text = encodeURIComponent(shareData.title + ' - ' + shareData.url);
  window.open('https://wa.me/?text=' + text, '_blank');
}
function shareCopy() {
  const url = shareData.url;
  const done = () => {
    const copied = document.getElementById('shareCopied');
    if (copied) copied.classList.add('show');
  };
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(url).then(done).catch(fallbackCopy);
  } else {
    fallbackCopy();
  }
  function fallbackCopy() {
    const ta = document.createElement('textarea');
    ta.value = url; document.body.appendChild(ta); ta.select();
    try { document.execCommand('copy'); } catch (e) {}
    document.body.removeChild(ta);
    done();
  }
}
function shareNative() {
  if (navigator.share) {
    navigator.share({ title: shareData.title, url: shareData.url }).catch(() => {});
  }
}

// ─── CSRF helper (token rendered in <meta name="csrf-token">) ───────────────────
function csrfHeaders() {
  var m = document.querySelector('meta[name="csrf-token"]');
  return m ? { 'X-CSRFToken': m.getAttribute('content') } : {};
}

// ─── Download Modal (email capture before every document download) ──────────────
let currentDl = { url: '', name: '' };
function openDlModal(url, name) {
  currentDl = { url: url || '', name: name || '' };
  document.getElementById('dlOverlay').classList.add('open');
  const inp = document.getElementById('dlEmail');
  if (inp) { inp.value = ''; setTimeout(function () { inp.focus(); }, 80); }
}
function closeDlModal() {
  document.getElementById('dlOverlay').classList.remove('open');
}
function dlSubscribeAndDownload() {
  const email = document.getElementById('dlEmail').value.trim();
  if (email && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    const fd = new FormData();
    fd.append('email', email);
    fd.append('template', currentDl.name);
    fetch('/download-request', { method: 'POST', body: fd, headers: csrfHeaders() }).catch(() => {});
  }
  closeDlModal();
  triggerDownload();
}
function dlSkipAndDownload() {
  closeDlModal();
  triggerDownload();
}
function triggerDownload() {
  if (currentDl.url) window.location.href = currentDl.url;
}

// ─── Contact Form ────────────────────────────────────────────────────────────
function submitForm() {
  const n = document.getElementById('fname');
  const e = document.getElementById('femail');
  const q = document.getElementById('fquery');
  const successEl = document.getElementById('formSuccess');
  const errorEl = document.getElementById('formErrorMsg');

  [n, e, q].forEach(f => f.classList.remove('error'));
  ['fnameErr', 'femailErr', 'fqueryErr'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.remove('show');
  });
  if (successEl) successEl.classList.remove('show');
  if (errorEl) errorEl.classList.remove('show');

  const hp = document.getElementById('fhp');
  const fd = new FormData();
  fd.append('name', n.value.trim());
  fd.append('email', e.value.trim());
  fd.append('query', q.value.trim());
  fd.append('website', hp ? hp.value : '');

  fetch('/contact', { method: 'POST', body: fd, headers: csrfHeaders() })
    .then(r => r.json())
    .then(data => {
      if (data.success) {
        if (successEl) successEl.classList.add('show');
        n.value = ''; e.value = ''; q.value = '';
      } else {
        const errs = data.errors || {};
        if (errs.name) { n.classList.add('error'); const el = document.getElementById('fnameErr'); if (el) { el.textContent = errs.name; el.classList.add('show'); } }
        if (errs.email) { e.classList.add('error'); const el = document.getElementById('femailErr'); if (el) { el.textContent = errs.email; el.classList.add('show'); } }
        if (errs.query) { q.classList.add('error'); const el = document.getElementById('fqueryErr'); if (el) { el.textContent = errs.query; el.classList.add('show'); } }
      }
    })
    .catch(() => {
      if (errorEl) { errorEl.textContent = 'Something went wrong. Please try again.'; errorEl.classList.add('show'); }
    });
}

// ─── Newsletter ───────────────────────────────────────────────────────────────
function subscribeNewsletter() {
  const nameEl = document.getElementById('nlName');
  const emailEl = document.getElementById('nlEmail');
  const btn = document.getElementById('nlBtn');
  const name = nameEl ? nameEl.value.trim() : '';
  const email = emailEl ? emailEl.value.trim() : '';

  const hp = document.getElementById('nlHp');
  const fd = new FormData();
  fd.append('name', name);
  fd.append('email', email);
  fd.append('website', hp ? hp.value : '');

  fetch('/newsletter', { method: 'POST', body: fd, headers: csrfHeaders() })
    .then(r => r.json())
    .then(data => {
      if (btn) btn.textContent = data.message;
      if (data.success) {
        if (nameEl) nameEl.value = '';
        if (emailEl) emailEl.value = '';
      }
    })
    .catch(() => {
      if (btn) btn.textContent = 'Something went wrong.';
    });
}

// ─── Act Comparison ──────────────────────────────────────────────────────────
// ─── Animated Counters ────────────────────────────────────────────────────────
const statsObs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      document.querySelectorAll('.stat-num').forEach(el => {
        const target = parseInt(el.dataset.target), suffix = el.dataset.suffix || '';
        let start = 0;
        const step = Math.ceil(target / 88);
        const t = setInterval(() => {
          start = Math.min(start + step, target);
          el.textContent = start + suffix;
          if (start >= target) clearInterval(t);
        }, 16);
      });
      statsObs.disconnect();
    }
  });
// Fires early (200px out) so the count-up finishes as the bar scrolls in. The
// real numbers are now server-rendered, so a late trigger would visibly snap
// them back to 0 before counting.
}, { threshold: 0, rootMargin: '200px 0px' });
const sb = document.getElementById('statsBar');
if (sb) statsObs.observe(sb);

// ─── Global click handlers ────────────────────────────────────────────────────
window.addEventListener('click', e => {
  const dl = document.getElementById('dlOverlay');
  if (dl && e.target === dl) closeDlModal();
  const sh = document.getElementById('shareOverlay');
  if (sh && e.target === sh) closeShare();
});

// ─── Header auto-hide (slide up on scroll down, back on scroll up) ─────────────
(function () {
  var nav = document.getElementById('mainNav');
  if (!nav) return;
  var isHero = nav.classList.contains('nav-hero');
  var hero = document.querySelector('.hero--media');
  var lastY = window.scrollY;
  function heroThreshold() {
    return hero ? Math.max(80, hero.offsetHeight - nav.offsetHeight - 24) : 80;
  }
  function onScroll() {
    var y = window.scrollY;
    if (isHero) {
      var solid = y > heroThreshold();
      nav.classList.toggle('nav-solid', solid);                 // solid white past the hero
      nav.classList.toggle('nav-glass', !solid && y > 8);       // frosted over the hero (not at the very top)
    }
    // Auto-hide: slide up on scroll down, reveal on scroll up.
    if (y > lastY && y > 90) nav.classList.add('nav-hidden');
    else nav.classList.remove('nav-hidden');
    lastY = y;
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();

// ─── Floating search widget modal ──────────────────────────────────────────────
function openSearchModal() {
  var m = document.getElementById('searchModal');
  if (!m) return;
  m.classList.add('open');
  var i = document.getElementById('searchModalInput');
  if (i) setTimeout(function () { i.focus(); }, 80);
}
function closeSearchModal() {
  var m = document.getElementById('searchModal');
  if (m) m.classList.remove('open');
}
window.addEventListener('click', function (e) {
  var sm = document.getElementById('searchModal');
  if (sm && e.target === sm) closeSearchModal();
});
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') { closeSearchModal(); closeShare && closeShare(); }
});

// ─── Scroll-reveal animations ──────────────────────────────────────────────────
(function () {
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (!('IntersectionObserver' in window)) return;
  // Cards are handled by the scroll-driven 3D page-open in CSS; here we only
  // reveal the non-card content (headings, quotes, timeline, callouts).
  var sel = '.person-card,.timeline-item,.about-quote,.legal-tldr,.section-title';
  var els = [].slice.call(document.querySelectorAll(sel));
  var obs = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add('in-view'); obs.unobserve(en.target); }
    });
  }, { threshold: 0.12 });
  var cardSel = '.offer-card,.blog-card,.template-card,.resource-card,.landmark-card,.resolution-card,.search-result';
  els.forEach(function (el, i) {
    var variant = 'reveal-up';
    if (el.matches(cardSel)) variant = (i % 2 === 0) ? 'reveal-left' : 'reveal-right';
    else if (el.matches('.person-card')) variant = 'reveal-right';
    else if (el.matches('.about-quote,.legal-tldr')) variant = 'reveal-zoom';
    el.classList.add('reveal', variant);
    el.style.transitionDelay = ((i % 6) * 0.07) + 's';
    obs.observe(el);
  });
})();

// ─── Resolution preview modal ──────────────────────────────────────────────────
function previewResolution(slug) {
  var src = document.getElementById('res-' + slug);
  if (!src) return;
  var name = src.getAttribute('data-title') || 'Preview';
  var url = src.getAttribute('data-download') || '';
  document.getElementById('previewTitle').textContent = name;
  document.getElementById('previewBody').innerHTML = src.innerHTML;
  // The preview's "Download" routes through the email-capture modal too.
  var dl = document.getElementById('previewDownload');
  dl.onclick = function (e) { e.preventDefault(); closePreview(); openDlModal(url, name); };
  document.getElementById('previewOverlay').classList.add('open');
}
// Preview for the real .docx document formats — fetches rendered HTML on demand.
function previewFormat(slug, name, url) {
  var body = document.getElementById('previewBody');
  document.getElementById('previewTitle').textContent = name || 'Preview';
  body.innerHTML = '<p style="text-align:center;color:var(--mid)">Loading preview…</p>';
  var dl = document.getElementById('previewDownload');
  dl.onclick = function (e) { e.preventDefault(); closePreview(); openDlModal(url, name); };
  document.getElementById('previewOverlay').classList.add('open');
  fetch('/format/' + encodeURIComponent(slug) + '/preview')
    .then(function (r) { if (!r.ok) throw new Error('bad status'); return r.text(); })
    .then(function (htmlStr) { body.innerHTML = htmlStr; body.scrollTop = 0; })
    .catch(function () {
      body.innerHTML = '<p style="text-align:center;color:var(--mid)">Preview unavailable. Please download the Word file to view it.</p>';
    });
}
function closePreview() {
  var o = document.getElementById('previewOverlay');
  if (o) o.classList.remove('open');
}
window.addEventListener('click', function (e) {
  var o = document.getElementById('previewOverlay');
  if (o && e.target === o) closePreview();
});
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') closePreview();
});

// ─── Article: reading-progress bar ─────────────────────────────────────────────
(function () {
  var bar = document.getElementById('readBar');
  var article = document.getElementById('articleProse');
  if (!bar || !article) return;
  function update() {
    var rect = article.getBoundingClientRect();
    var total = rect.height - window.innerHeight + 120;
    var done = Math.min(Math.max(-rect.top + 120, 0), total);
    var pct = total > 0 ? (done / total) : 0;
    bar.style.transform = 'scaleX(' + pct.toFixed(4) + ')';
  }
  update();
  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update, { passive: true });
})();

// ─── Article: auto table of contents from headings ─────────────────────────────
(function () {
  var prose = document.getElementById('articleProse');
  var toc = document.getElementById('toc');
  var list = document.getElementById('tocList');
  if (!prose || !toc || !list) return;
  var heads = [].slice.call(prose.querySelectorAll('h2'));
  if (heads.length < 2) return;            // not worth a TOC for a short piece
  heads.forEach(function (h, i) {
    if (!h.id) h.id = 'sec-' + (i + 1);
    var li = document.createElement('li');
    var a = document.createElement('a');
    a.href = '#' + h.id;
    a.textContent = h.textContent;
    li.appendChild(a);
    list.appendChild(li);
  });
  toc.hidden = false;
})();

// ─── AdSense: reveal a slot when an ad is served, collapse it otherwise ─────────
// filled   -> show the ad and its "Advertisement" label.
// unfilled -> collapse the zone (no empty box).
// blocked / never resolves -> collapse the zone (after a generous wait).
// The zone is left visible + measurable WHILE loading, because collapsing it up
// front (display:none) stops responsive AdSense units from ever filling.
(function () {
  function apply(zone, filled) {
    var container = zone.closest('.ad-container') || zone;
    zone.classList.toggle('is-filled', filled);
    if (container !== zone) container.classList.toggle('is-filled', filled);
    zone.style.display = filled ? '' : 'none';
  }
  [].slice.call(document.querySelectorAll('[data-ad-zone]')).forEach(function (zone) {
    var ins = zone.querySelector('ins.adsbygoogle');
    if (!ins) return;
    function resolve() {
      var status = ins.getAttribute('data-ad-status');
      if (status === 'filled')   { apply(zone, true);  return true; }
      if (status === 'unfilled') { apply(zone, false); return true; }
      return false; // not resolved yet — leave the zone so the ad can still load
    }
    if (resolve()) return;
    var mo = new MutationObserver(function () { if (resolve()) mo.disconnect(); });
    mo.observe(ins, { attributes: true, attributeFilter: ['data-ad-status'] });
    // Ad-blocker / no-response fallback: collapse ONLY if still unresolved after 12s.
    setTimeout(function () {
      if (ins.getAttribute('data-ad-status') == null) { mo.disconnect(); apply(zone, false); }
    }, 12000);
  });
})();

