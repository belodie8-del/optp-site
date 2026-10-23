"""3 email signature designs inspired by the new site (rendered as images, 600 px wide)."""
exec(open('_pre.py', encoding='utf-8').read())
MAIL = 'elodie.boyer@ebformationconsulting.com'
LOGO = '<svg class="lg" viewBox="0 0 287 90" role="img" aria-label="EB Formation Consulting"><use href="#optplogo"/></svg>'
V1 = '''<div class="sig s1" id="s1">
  <div class="s1-v"><img src="''' + ARCH_O + '''" alt=""><p class="pi">On ne naît pas manager.<br><b>Ça s’apprend.</b></p></div>
  <div class="s1-t"><span class="hd">Formatrice en management</span><h1>Élodie Boyer</h1><p class="co">Fondatrice · EB Formation Consulting</p>
    <p class="ct">06 79 35 34 41 &nbsp;·&nbsp; ''' + MAIL + '''<br><b>www.oseprendretaplace.fr</b></p>
    <div class="pl"><span class="p1">Mes formations →</span><span class="p2">❄ Winter Pack →</span></div></div>
</div>'''
V2 = '''<div class="sig s2" id="s2">
  <div class="s2-t">''' + LOGO + '''<h1>Élodie Boyer</h1><span class="hd">Construire un management humain mais exigeant</span>
    <p class="ct"><span>☎</span> 06 79 35 34 41<br><span>✉</span> ''' + MAIL + '''<br><span>✦</span> <b>www.oseprendretaplace.fr</b></p>
    <div class="pl"><span class="p1">Mes formations →</span><span class="p2">❄ Le Winter Pack →</span></div></div>
  <div class="s2-v"><img src="''' + ARCH_T + '''" alt=""></div>
</div>'''
V3 = '''<div class="sig s3" id="s3">
  <div class="s3-top"><img class="ph" src="''' + ORANGE + '''" alt="">
    <div><h1>Élodie Boyer</h1><span class="hd">Fondatrice EB Formation Consulting</span>
    <p class="ct">06 79 35 34 41<br>''' + MAIL + '''<br><b>www.oseprendretaplace.fr</b></p></div>
    ''' + LOGO + '''</div>
  <div class="s3-band"><i>❄</i><span><b>Nouveau · Le Winter Pack</b> 8 outils pour mener tes entretiens avec une vraie méthode</span><em>Découvrir →</em></div>
</div>'''
CSS = '''<style>
:root{--pine:#085055;--teal:#0F868A;--ember:#FF914D;--ink-e:#B4561F;--peach:#FFF4EE;--peach2:#FFE7D8;--mint:#E4F5F6;--ink:#1D2A28;}
*{box-sizing:border-box;margin:0}
body{background:#eee;padding:30px;display:grid;gap:40px;justify-content:center;font-family:'Nunito Sans',sans-serif;color:var(--ink)}
.lab{font:800 14px/1 'Nunito Sans';letter-spacing:.1em;text-transform:uppercase;color:#555;margin-bottom:-28px}
.sig{width:600px;position:relative;overflow:hidden}
h1{font-family:'Young Serif',Georgia,serif;font-weight:400;line-height:1.05}
.hd{font-family:'Caveat',cursive;font-weight:700;line-height:1.1;display:block}
.ct{font-size:12.5px;line-height:1.65}
.ct b{font-weight:800}
.pl{display:flex;gap:8px;margin-top:10px}
.pl span{font-weight:800;font-size:12.5px;border-radius:999px;padding:7px 14px;white-space:nowrap}
.lg{width:118px;height:37px;display:block}
/* V1 · bandeau vert comme le haut du site */
.s1{display:flex;gap:26px;align-items:center;background:var(--pine);border-radius:20px;padding:22px 26px 22px 30px;color:#fff;height:226px}
.s1::after{content:"";position:absolute;right:-60px;top:-80px;width:220px;height:220px;border-radius:50%;background:rgba(255,255,255,.05)}
.s1-v{position:relative;flex:none;width:128px}
.s1-v img{display:block;width:128px;height:166px;object-fit:cover;object-position:top;border-radius:64px 64px 12px 12px;background:var(--ember)}
.pi{position:absolute;left:-18px;bottom:-12px;background:#FFF1C9;color:var(--ink);padding:6px 10px;border-radius:5px 5px 13px 5px;font-family:'Caveat';font-weight:700;font-size:15px;line-height:1.05;transform:rotate(-4deg);box-shadow:0 10px 18px -10px rgba(0,0,0,.6);white-space:nowrap}
.pi b{color:var(--ink-e)}
.s1-t{position:relative;z-index:1;min-width:0}
.s1 .hd{color:var(--ember);font-size:21px}
.s1 h1{font-size:34px;color:#fff;margin:2px 0 4px}
.s1 .co{font-size:13px;font-weight:700;color:rgba(255,255,255,.75)}
.s1 .ct{color:rgba(255,255,255,.9);margin-top:8px}
.s1 .ct b{color:#fff}
.s1 .p1{background:var(--ember);color:#2B1304}.s1 .p2{background:rgba(255,255,255,.14);color:#fff;border:1.5px solid rgba(255,255,255,.4)}
/* V2 · carte pêche, arche photo */
.s2{display:flex;justify-content:space-between;align-items:center;gap:20px;background:var(--peach);border:1.5px solid var(--peach2);border-radius:20px;padding:24px 26px 22px 30px;min-height:236px}
.s2 h1{font-size:32px;color:var(--pine);margin:12px 0 0}
.s2 .hd{color:var(--ink-e);font-size:19px;margin-top:2px}
.s2 .ct{margin-top:8px}.s2 .ct span{color:var(--ember);display:inline-block;width:14px}.s2 .ct b{color:var(--teal)}
.s2 .p1{background:var(--ember);color:#2B1304}.s2 .p2{background:var(--pine);color:#fff}
.s2-v{flex:none;align-self:flex-end;margin-bottom:-22px}
.s2-v img{display:block;width:150px;height:196px;object-fit:cover;object-position:top;border-radius:75px 75px 0 0;background:var(--teal)}
/* V3 · blanche épurée + bandeau Winter Pack */
.s3{background:#fff;border:1.5px solid #EFE3DA;border-radius:20px}
.s3-top{display:flex;align-items:center;gap:20px;padding:20px 24px 16px}
.s3-top .ph{width:92px;height:92px;border-radius:50%;flex:none}
.s3-top > div{flex:1;min-width:0}
.s3 h1{font-size:28px;color:var(--pine)}
.s3 .hd{color:var(--ember);font-size:19px}
.s3 .ct{margin-top:4px}.s3 .ct b{color:var(--teal)}
.s3 .lg{align-self:flex-start;width:96px;height:30px}
.s3-band{display:flex;align-items:center;gap:12px;background:linear-gradient(90deg,var(--pine),var(--teal));color:#fff;padding:11px 22px}
.s3-band i{font-style:normal;font-size:20px}
.s3-band span{flex:1;font-size:12.5px;line-height:1.35}.s3-band b{display:block;font-family:'Young Serif';font-weight:400;font-size:16px}
.s3-band em{font-style:normal;font-weight:800;font-size:12.5px;background:var(--ember);color:#2B1304;border-radius:999px;padding:7px 14px;white-space:nowrap}
</style>'''
html = '<!doctype html><meta charset="utf-8">' + CSS + '<p class="lab">Version 1</p>' + V1 + '<p class="lab">Version 2</p>' + V2 + '<p class="lab">Version 3</p>' + V3 + defs
open(S + 'sig/sig-versions.html', 'w', encoding='utf-8').write(html)
print('ok')
