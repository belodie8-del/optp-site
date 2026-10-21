"""Shared animations for the Ose prendre ta place pages. `python3 anim.py file.html ...` injects them (idempotent)."""
import sys

REVEAL = ['main h1', 'main .lede', 'main .ctas', 'main .hand', 'main .h2', 'main .sub', '.pg-q', '.mo-me',
          '.sp-logos li', '.sp-stats li', '.h2o-s li', '.fh-s li',
          '.bub', '.mv3-l li', '.fit-c', '.aq-a', '.aq-b', '.why2', '.obj', '.oc', '.ao', '.aud-n',
          '.trk', '.eq-op', '.md', '.mdg-t', '.kit2', '.kit2-l li', '.mods li', '.pk', '.stp li', '.tr-l li', '.wd', '.wd-end', '.bx', '.fm-quote',
          '.tms', '.ms', '.fq-big', '.ab-v', '.ab-t > *', '.why2-a', '.why2-b', '.co-p', '.cq', '.co-c',
          '.nl', '.nlb', '.pc2', '.bc', '.ft', '.flt', '.as', '.art > *', '.share', '.aut',
          '.kcf', '.kco2 > *', '.ksc-c', '.wq', '.wtags', '.fq', '.trk-k']

ANIM = '''<style id="oa-anim">
@media (prefers-reduced-motion: no-preference){
  html.oa .oa-r{opacity:0;translate:0 26px;transition:opacity .7s ease var(--oa-d,0ms),translate .8s cubic-bezier(.2,.8,.2,1) var(--oa-d,0ms);}
  html.oa .oa-r.oa-in{opacity:1;translate:0 0;}
  html.oa mark.oa-m{box-shadow:none!important;background-image:linear-gradient(rgba(255,145,77,.32),rgba(255,145,77,.32));background-repeat:no-repeat;background-position:0 92%;background-size:0 .4em;transition:background-size 1s cubic-bezier(.3,.7,.2,1) .35s;}
  html.oa mark.oa-m.oa-on{background-size:100% .4em;}
  .h2o h1 em path{stroke-dasharray:420;stroke-dashoffset:420;animation:oa-draw 1.3s cubic-bezier(.4,.1,.2,1) .7s forwards;}
  @keyframes oa-draw{to{stroke-dashoffset:0;}}
  .arch img,.hb-p,.hc-r img,.ch-v img,.fh-v .arch img{animation:oa-zoom 1.6s cubic-bezier(.2,.8,.2,1) both;}
  @keyframes oa-zoom{from{scale:1.08;opacity:.4;}to{scale:1;opacity:1;}}
  .tag,.hb-st,.fh-st,.ch-bub,.kch-bub,.hb-badge{animation:oa-float 5s ease-in-out 1.2s infinite;}
  .hb-st.r,.fh-st.s2{animation-delay:2.4s;}
  @keyframes oa-float{0%,100%{translate:0 0;}50%{translate:0 -8px;}}
  .btn > span[aria-hidden="true"]{display:inline-block;transition:translate .25s ease;}
  .btn:hover > span[aria-hidden="true"]{translate:5px 0;}
  .sp-logos li img{transition:opacity .3s,scale .3s;} .sp-logos li img:hover{opacity:1;scale:1.06;}
  .fq[open] .fq-a,.md-dt[open] > ul,.md-dt[open] > .md-x{animation:oa-open .45s ease both;}
  @keyframes oa-open{from{opacity:0;translate:0 -8px;}to{opacity:1;translate:0 0;}}
  .rdvbtn.big{animation:oa-pulse 3.2s ease-in-out 2s infinite;}
  @keyframes oa-pulse{0%,100%{box-shadow:0 16px 28px -16px rgba(180,86,31,.9);}50%{box-shadow:0 16px 28px -16px rgba(180,86,31,.9),0 0 0 8px rgba(255,145,77,.18);}}
}
</style>
<script id="oa-anim-js">
(function(){
  if (!('IntersectionObserver' in window) || !window.matchMedia || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var root = document.documentElement; root.classList.add('oa');
  var sel = __SEL__;
  var seen = [];
  sel.forEach(function(s){ [].forEach.call(document.querySelectorAll(s), function(el){
    if (seen.indexOf(el) > -1 || el.closest('header') || el.closest('footer')) return;
    for (var p = el.parentElement; p; p = p.parentElement){ if (seen.indexOf(p) > -1 && p.classList.contains('oa-r') && !p.matches('main .wrap, section')) { if (!el.matches('.trk, .md, .pc2, .bc, li, .ao, .ksc-c, .co-c, .fit-c, .wd, .fq')) return; } }
    seen.push(el); el.classList.add('oa-r');
  }); });
  seen.forEach(function(el){
    var sib = [].filter.call(el.parentElement.children, function(c){ return c.classList.contains('oa-r'); });
    el.style.setProperty('--oa-d', Math.min(sib.indexOf(el), 6) * 90 + 'ms');
  });
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting){ e.target.classList.add('oa-in'); io.unobserve(e.target); } }); }, {rootMargin:'0px 0px -8% 0px', threshold:0.08});
  seen.forEach(function(el){ io.observe(el); });
  var marks = [].slice.call(document.querySelectorAll('main mark'));
  var mo = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting){ e.target.classList.add('oa-on'); mo.unobserve(e.target); } }); }, {threshold:0.6});
  marks.forEach(function(m){ m.classList.add('oa-m'); mo.observe(m); });
  function count(el){
    var txt = el.textContent, m = txt.match(/^(\\+?)(\\d(?:[\\d\\u00a0\\u202f ]*\\d)?)(.*)$/);
    if (!m || /^\\s*\\//.test(m[3])) return;
    var n = parseInt(m[2].replace(/[^\\d]/g, ''), 10); if (!(n >= 2)) return;
    var spaced = /[\\u00a0\\u202f ]\\d/.test(m[2]), t0 = null, dur = 1400;
    function fmt(v){ var s = String(v); return spaced ? s.replace(/\\B(?=(\\d{3})+(?!\\d))/g, '\\u00a0') : s; }
    function step(t){ if (!t0) t0 = t; var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      el.textContent = m[1] + fmt(Math.round(n * e)) + m[3]; if (k < 1) requestAnimationFrame(step); else el.textContent = txt; }
    el.textContent = m[1] + fmt(0) + m[3]; requestAnimationFrame(step);
  }
  var nums = [].slice.call(document.querySelectorAll('.sp-stats b, .h2o-s b, .fh-s b'));
  var co = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting){ count(e.target); co.unobserve(e.target); } }); }, {threshold:0.6});
  nums.forEach(function(n){ co.observe(n); });
})();
</script>
'''.replace('__SEL__', repr(REVEAL).replace("'", '"'))

def inject(path):
    s = open(path, encoding='utf-8').read()
    if 'id="oa-anim"' in s:
        a = s.index('<style id="oa-anim">'); b = s.index('</script>', s.index('id="oa-anim-js"')) + len('</script>\n')
        s = s[:a] + s[b:]
    k = s.rfind('<svg width="0" height="0"')
    assert k > 0, path
    s = s[:k] + ANIM + s[k:]
    open(path, 'w', encoding='utf-8').write(s)

if __name__ == '__main__':
    for f in sys.argv[1:]:
        inject(f); print('anim ->', f)
