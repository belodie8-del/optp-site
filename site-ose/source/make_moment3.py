"""Test: 3 light versions of the 'Pourquoi c'est le moment' section of the formations page."""
exec(open('make_formations.py', encoding='utf-8').read())
HDR = BODY[:BODY.index('<main id="top">')]
TITLE = '<span class="hand">On fait le point ?</span><h2 class="h2">Pourquoi c’est le moment</h2>'
SUB = '<p class="sub">Je ne vais pas te convaincre avec des arguments bateau, parce que tu les vis au quotidien :</p>'
CTA = '<a class="btn rdvbtn" href="' + RDV + '" target="_blank" rel="noopener">On en parle ? ' + ARR + '</a>'
def label(n, t): return '<div class="vlab"><div class="wrap"><b>Version %d</b> · %s</div></div>' % (n, t)

V1 = ('<section class="room peach mv1"><div class="wrap"><div class="ctr">' + TITLE + SUB + '</div>'
      '<div class="mv1-g">' + ''.join('<article class="mv1-c"><span class="mv1-n">%02d</span><span class="mv1-p">Parce que</span><p>%s</p></article>' % (i + 1, t) for i, t in enumerate(WHY_NOW)) +
      '</div><div class="ctarow center">' + CTA + '</div></div></section>')

V2 = ('<section class="room mint mv2"><div class="wrap mv2-w"><div class="mv2-h">' + TITLE + SUB +
      '<p class="mv2-hint">Coche ce qui te parle 👉</p><div class="mv2-res" hidden><p><b class="mv2-k">0</b> sur 5. Alors oui, c’est le moment.</p>' + CTA + '</div></div>'
      '<div class="mv2-s">' + ''.join('<label class="mv2-i"><input type="checkbox"><span class="mv2-b" aria-hidden="true"></span><span class="mv2-t"><span class="mv2-p">Parce que</span> %s</span></label>' % t for t in WHY_NOW) +
      '</div></div></section>'
      '<script>(function(){var r=document.querySelector(".mv2-res"),k=document.querySelector(".mv2-k"),h=document.querySelector(".mv2-hint");'
      '[].forEach.call(document.querySelectorAll(".mv2-i input"),function(c){c.addEventListener("change",function(){var n=document.querySelectorAll(".mv2-i input:checked").length;'
      'k.textContent=n;r.hidden=n===0;h.hidden=n>0;});});})();</script>')

V3 = ('<section class="room mv3"><div class="wrap"><div class="ctr">' + TITLE + SUB + '</div><ol class="mv3-l">' +
      ''.join('<li class="%s"><span class="mv3-n" aria-hidden="true">%02d</span><p><span class="mv3-p">Parce que</span> %s</p></li>' % ('r' if i % 2 else 'l', i + 1, t) for i, t in enumerate(WHY_NOW)) +
      '</ol><div class="ctarow center">' + CTA + '</div></div></section>')

CSS_M = '''<style>
.vlab{background:#1D2A28;color:#fff;padding:14px 0;font-size:15px;position:sticky;top:0;z-index:40;}
.vlab b{color:#FFCFA3;}
mark{background:none;color:var(--ink);font-weight:800;box-shadow:inset 0 -.45em 0 rgba(255,145,77,.38);padding:0 2px;}
/* V1 cards on peach */
.mv1-g{display:flex;flex-wrap:wrap;justify-content:center;gap:20px;margin-top:48px;}
.mv1-c{flex:0 1 calc((100% - 40px) / 3);min-width:260px;background:#fff;border-radius:26px;padding:28px 26px;box-shadow:0 22px 40px -32px rgba(180,86,31,.7);display:flex;flex-direction:column;gap:6px;}
.mv1-n{font-family:var(--display);font-size:46px;line-height:1;color:var(--ember);}
.mv1-p{font-family:var(--hand);font-weight:700;font-size:25px;color:var(--teal);margin-top:6px;}
.mv1-c p{margin:0;font-size:16.5px;line-height:1.6;color:var(--ink);}
.mv1 .ctarow{margin-top:44px;}
/* V2 checklist on mint */
.mv2-w{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:64px;align-items:center;}
.mv2-hint{margin:22px 0 0;font-family:var(--hand);font-weight:700;font-size:28px;color:var(--ember-ink);}
.mv2-res{margin-top:22px;padding:22px 24px;border-radius:22px;background:#fff;box-shadow:0 18px 34px -26px rgba(8,80,85,.7);}
.mv2-res p{margin:0 0 14px;font-family:var(--display);font-size:24px;color:var(--pine);} .mv2-k{font-family:var(--display);font-weight:400;font-size:34px;color:var(--ember-ink);}
.mv2-s{background:#fff;border-radius:30px;padding:16px 28px;box-shadow:0 30px 50px -36px rgba(8,80,85,.7);}
.mv2-i{display:flex;gap:16px;align-items:flex-start;padding:20px 4px;border-bottom:1.5px dashed var(--line);cursor:pointer;}
.mv2-i:last-child{border-bottom:0;}
.mv2-i input{position:absolute;opacity:0;width:1px;height:1px;}
.mv2-b{flex:none;width:28px;height:28px;margin-top:2px;border-radius:9px;border:2.5px solid var(--teal);display:grid;place-items:center;transition:background .15s;}
.mv2-b::after{content:"";width:12px;height:7px;border:3px solid #fff;border-top:0;border-right:0;transform:rotate(-45deg) translate(1px,-1px);opacity:0;}
.mv2-i input:checked + .mv2-b{background:var(--teal);} .mv2-i input:checked + .mv2-b::after{opacity:1;}
.mv2-i input:focus-visible + .mv2-b{outline:3px solid var(--ember);outline-offset:2px;}
.mv2-t{font-size:16.5px;line-height:1.6;color:var(--ink);}
.mv2-p{font-family:var(--hand);font-weight:700;font-size:23px;color:var(--teal);margin-right:2px;}
.mv2-i:hover .mv2-b{background:var(--mint);}
.mv2-i input:checked ~ .mv2-t{color:var(--pine);}
/* V3 big alternating list on white */
.mv3-l{list-style:none;margin:56px auto 0;padding:0;max-width:980px;display:grid;gap:26px;}
.mv3-l li{position:relative;width:min(100%,640px);padding:30px 34px 30px 110px;border-radius:28px;background:var(--peach);}
.mv3-l li.r{margin-left:auto;background:var(--mint);}
.mv3-n{position:absolute;left:26px;top:22px;font-family:var(--display);font-size:62px;line-height:1;color:var(--ember);opacity:.85;}
.mv3-l li.r .mv3-n{color:var(--teal);}
.mv3-l p{margin:0;font-family:var(--display);font-size:clamp(19px,1.9vw,23px);line-height:1.4;color:var(--ink);}
.mv3-l mark{font-weight:400;}
.mv3-p{display:block;font-family:var(--hand);font-weight:700;font-size:25px;line-height:1;color:var(--ember-ink);margin-bottom:8px;}
.mv3-l li.r .mv3-p{color:var(--teal);}
.mv3 .ctarow{margin-top:48px;}
@media (max-width:1020px){.mv1-c{flex-basis:calc((100% - 20px) / 2);} .mv2-w{grid-template-columns:1fr;gap:36px;}}
@media (max-width:620px){.mv1-c{flex-basis:100%;min-width:0;} .mv2-s{padding:8px 18px;} .mv3-l li{padding:76px 22px 24px;} .mv3-n{left:22px;top:18px;font-size:46px;}}
</style>
'''
html = head + CSS_A + CSS_F + CSS_M + HDR + '<main>' + label(1, 'Cartes sur fond pêche') + V1 + label(2, 'Une liste à cocher, sur fond menthe') + V2 + label(3, 'Grandes phrases en alternance, sur fond blanc') + V3 + '</main>' + defs
open(S + 'home/moment-3-versions.html', 'w', encoding='utf-8').write(html)
print(len(html))
