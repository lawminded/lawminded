/* Law Minded — ambient "alive" field around the hero brain logo.
   Glowing gold particles (circuit dots) drift near the logo, connected by faint
   wire lines with light pulses travelling along them. Gently reacts to the cursor.
   Desktop only; disabled for reduced-motion. Pauses when the tab is hidden. */
(function () {
  var fx = document.getElementById('heroFx');
  var cv = document.getElementById('heroParticles');
  if (!fx || !cv) return;
  if (window.matchMedia) {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    if (window.matchMedia('(max-width:800px)').matches) return; // hero-visual is hidden on mobile
  }
  var ctx = cv.getContext('2d');
  if (!ctx) return;

  var GOLD = '232,160,32';
  var DPR = Math.min(window.devicePixelRatio || 1, 2);
  var W = 0, H = 0, parts = [], raf = null;
  var mouse = { x: -999, y: -999, active: false };

  function size() {
    var r = fx.getBoundingClientRect();
    W = Math.max(1, r.width); H = Math.max(1, r.height);
    cv.width = W * DPR; cv.height = H * DPR;
    cv.style.width = W + 'px'; cv.style.height = H + 'px';
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  }
  function build() {
    size();
    var n = Math.max(14, Math.min(34, Math.round(W * H / 9000)));
    parts = [];
    for (var i = 0; i < n; i++) {
      parts.push({
        x: Math.random() * W, y: Math.random() * H,
        vx: (Math.random() - 0.5) * 0.22, vy: (Math.random() - 0.5) * 0.22,
        r: Math.random() * 1.6 + 0.8
      });
    }
  }

  window.addEventListener('mousemove', function (e) {
    var r = fx.getBoundingClientRect();
    var x = e.clientX - r.left, y = e.clientY - r.top;
    if (x >= -60 && x <= W + 60 && y >= -60 && y <= H + 60) { mouse.x = x; mouse.y = y; mouse.active = true; }
    else { mouse.active = false; }
  }, { passive: true });

  function frame() {
    ctx.clearRect(0, 0, W, H);

    for (var i = 0; i < parts.length; i++) {
      var p = parts[i];
      if (mouse.active) {
        var mx = mouse.x - p.x, my = mouse.y - p.y, md = Math.hypot(mx, my);
        if (md < 140 && md > 0.1) { var f = (140 - md) / 140 * 0.018; p.vx += mx / md * f; p.vy += my / md * f; }
      }
      p.x += p.vx; p.y += p.vy;
      p.vx *= 0.992; p.vy *= 0.992;
      // keep a gentle minimum drift so it never freezes
      if (Math.abs(p.vx) < 0.04) p.vx += (Math.random() - 0.5) * 0.03;
      if (Math.abs(p.vy) < 0.04) p.vy += (Math.random() - 0.5) * 0.03;
      if (p.x < 0 || p.x > W) p.vx *= -1;
      if (p.y < 0 || p.y > H) p.vy *= -1;
      p.x = Math.max(0, Math.min(W, p.x));
      p.y = Math.max(0, Math.min(H, p.y));
    }

    // wires + travelling pulses
    var now = Date.now();
    for (var a = 0; a < parts.length; a++) {
      for (var b = a + 1; b < parts.length; b++) {
        var p1 = parts[a], p2 = parts[b];
        var dx = p1.x - p2.x, dy = p1.y - p2.y, d = Math.hypot(dx, dy);
        if (d < 116) {
          var o = (1 - d / 116) * 0.5;
          ctx.strokeStyle = 'rgba(' + GOLD + ',' + (o * 0.5).toFixed(3) + ')';
          ctx.lineWidth = 0.6;
          ctx.beginPath(); ctx.moveTo(p1.x, p1.y); ctx.lineTo(p2.x, p2.y); ctx.stroke();
          var t = ((now / 1500) + (a * 0.13 + b * 0.07)) % 1;
          ctx.fillStyle = 'rgba(' + GOLD + ',' + o.toFixed(3) + ')';
          ctx.beginPath(); ctx.arc(p1.x + (p2.x - p1.x) * t, p1.y + (p2.y - p1.y) * t, 1.1, 0, 6.2832); ctx.fill();
        }
      }
    }

    // dots with soft glow
    ctx.shadowBlur = 6; ctx.shadowColor = 'rgba(' + GOLD + ',0.6)';
    for (var k = 0; k < parts.length; k++) {
      var q = parts[k];
      ctx.fillStyle = 'rgba(' + GOLD + ',0.85)';
      ctx.beginPath(); ctx.arc(q.x, q.y, q.r, 0, 6.2832); ctx.fill();
    }
    ctx.shadowBlur = 0;

    raf = requestAnimationFrame(frame);
  }

  function start() { if (!raf) frame(); }
  function stop() { if (raf) { cancelAnimationFrame(raf); raf = null; } }

  window.addEventListener('resize', build, { passive: true });
  document.addEventListener('visibilitychange', function () { if (document.hidden) stop(); else start(); });
  build();
  start();
})();
