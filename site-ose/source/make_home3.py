"""Test: 3 versions of the oseprendretaplace.fr home page (same codes as the Winter Pack, own layouts, no Winter mention)."""
exec(open('_pre.py', encoding='utf-8').read())
exec(open('_bodyA.py', encoding='utf-8').read())
exec(open('_cssA.py', encoding='utf-8').read())

def swap(body, marker, new):
    i = body.index(marker); j = body.index('</section>', i) + len('</section>')
    return body[:i] + new + body[j:]
def chip_list(xs): return ''.join('<li>%s<span>%s</span></li>' % (CHK, x) for x in xs)
INC = ['RESET', 'Lecture d’équipe', 'Posture & Crédibilité', '3 séances de coaching avec Élodie']
BOO = ['Courage & Influence', 'Alliance individuelle', 'Collectif', '3 séances de coaching avec Élodie']
OPT = ['Les 6 modules', '6 séances de coaching individuel avec Élodie', 'Le groupe WhatsApp privé', 'Les lives exclusifs de la communauté']
RES = '<p class="res">Tu n’improvises plus. <b>Tu sais.</b><br>Tu n’esquives plus. <b>Tu oses.</b><br>Tu n’attends plus d’être légitime. <b>Tu l’es.</b></p>'
LEDE = 'Une méthode concrète pour incarner une autorité naturelle, fédérer ton équipe et retrouver le plaisir de manager, même si tu n’as jamais été formé(e).'
PAIN_H = '<span class="hand">On fait le point ?</span><h2 class="h2">Pourquoi c’est le moment</h2>'
AV_H = '<span class="hand">Ils témoignent</span><h2 class="h2">Ce que disent les managers formés</h2>'
FIN_T = ('<h2>Ose prendre ta place de manager et libère ton potentiel !</h2><p>30 minutes pour faire le point sur ta situation : on identifie ce qui bloque vraiment, je te donne mon analyse directe, '
         'et on voit ensemble quelle formule peut t’aider à avancer.</p><p class="fin2-k">Pas de pression. Juste de l’efficacité !</p>')
BADGE = ('<a class="hb-badge" href="%s" aria-label="Faire l’audit offert"><svg viewBox="0 0 120 120" aria-hidden="true"><defs><path id="bdg" d="M60,60 m-44,0 a44,44 0 1,1 88,0 a44,44 0 1,1 -88,0"/></defs>'
         '<text><textPath href="#bdg">AUDIT OFFERT · 10 MINUTES ·</textPath></text></svg><span>→</span></a>') % AUDIT

# ---------- version B : pêche, éditorial ----------
B = BODY_A
B = swap(B, '<section class="h2o">', '''<section class="hb"><div class="wrap">
  <span class="hand">Formation en management · par Élodie Boyer</span>
  <h1>Ose prendre ta place <span class="hb-s">de manager</span></h1>
  <p class="lede">''' + LEDE + '''</p>
  <div class="ctas"><a class="btn" href="#formations">Découvrir les formations ''' + ARR + '''</a><a class="btn soft" href="''' + AUDIT + '''">Faire l’audit offert</a></div>
  <div class="hb-v"><img class="hb-p" src="''' + ORANGE + '''" alt="Élodie Boyer" width="640" height="640">
    <div class="hb-st l"><b>+10 ans</b>d’expérience terrain</div><div class="hb-st r"><b>+5 000</b>managers inscrits</div>''' + BADGE + '''</div>
</div></section>''')
B = B.replace(P.BAND, P.BAND + P.STATS_SECTION, 1)
B = swap(B, '<section class="room" id="moment">', '''<section class="room" id="moment"><div class="wrap pb">
  <div>''' + PAIN_H + '''<p class="sub">Je ne vais pas te convaincre avec des arguments bateau. Tu les vis au quotidien.</p></div>
  <ol class="pb-l">''' + ''.join('<li><span>%02d</span><p>%s</p></li>' % (i + 1, t) for i, t in enumerate(PAINS)) + '''</ol>
</div></section>''')
B = B.replace('<section class="room mint" id="audit">', '<section class="room aud-dark" id="audit">', 1)
B = swap(B, '<section class="room" id="formations">', '''<section class="room peach" id="formations"><div class="wrap">
  <span class="hand">Les formations</span><h2 class="h2">Comment travailler avec moi ?</h2>
  <p class="sub">Tu peux avancer marche par marche, ou faire tout le chemin avec moi pendant 12 semaines.</p>
  <div class="stairs">
    <article class="trk st"><span class="st-n">1</span><span class="trk-k">Ta posture · 3 modules</span><h3>Incarne ta posture</h3><p>Tu as le titre de manager, mais l’impression de faire semblant.</p><ul>''' + chip_list(INC) + '''</ul><div class="trk-p"><b>897 €</b></div><a class="btn soft" href="''' + FORM + '''">Découvrir</a></article>
    <article class="trk st"><span class="st-n">2</span><span class="trk-k">Ton équipe · 3 modules</span><h3>Booste ton équipe</h3><p>Ton équipe n’avance pas comme tu veux. Tes 1-to-1 et tes réunions ne servent à rien.</p><ul>''' + chip_list(BOO) + '''</ul><div class="trk-p"><b>897 €</b></div><a class="btn soft" href="''' + FORM + '''">Découvrir</a></article>
    <article class="trk st big"><span class="st-n">1+2</span><span class="trk-k">La transformation complète · 12 semaines</span><h3>Ose prendre ta place</h3><p>Personne ne t’a appris à manager. Moi si.</p><ul>''' + chip_list(OPT) + '''</ul>''' + RES + '''<div class="trk-p"><b>1 497 €</b><span>paiement en 2 fois possible</span></div><a class="btn" href="''' + FORM + '''">Découvrir la formation ''' + ARR + '''</a></article>
  </div>
</div></section>''')
B = B.replace('<section class="room peach" id="programme">', '<section class="room mint" id="programme">', 1)
B = swap(B, '<section class="room mint" id="avis">', '''<section class="room" id="avis"><div class="wrap">
  <div class="tb-h">''' + AV_H + '''<p class="sp-google big">''' + P.GOOGLE + '''</p></div>
  <div class="mas">''' + ''.join('<figure class="ms c%d"><blockquote>%s</blockquote><figcaption><b>%s</b> · %s%s</figcaption></figure>' % (
        i % 3, q, n, r, ('<span class="tm-g">%s Avis Google vérifié</span>' % P.GLOGO) if g else '') for i, (q, n, r, g) in enumerate(AVIS)) + '''</div>
</div></section>''')
B = B.replace('<section class="room" id="newsletter">', '<section class="room peach" id="newsletter">', 1)
B = swap(B, '<section class="fin2">', '''<section class="fin2 fb"><div class="wrap"><span class="hand">Travaillons ensemble</span>''' + FIN_T + '''
  <a class="btn rdvbtn big" href="''' + RDV + '''" target="_blank" rel="noopener">Je prends RDV avec Élodie ''' + ARR + '''</a></div></section>''')

# ---------- version C : orange, magazine ----------
C = BODY_A
C = swap(C, '<section class="h2o">', '''<section class="hc">
  <div class="hc-l"><div class="hc-in"><span class="hand">Formation en management · par Élodie Boyer</span>
    <h1>Ose prendre ta place de manager.</h1><p class="lede">''' + LEDE + '''</p>
    <div class="ctas"><a class="btn" href="#formations">Découvrir les formations ''' + ARR + '''</a><a class="btn hc-ghost" href="''' + AUDIT + '''">Faire l’audit offert</a></div></div></div>
  <div class="hc-r"><img src="''' + ARCH_T + '''" alt="Élodie Boyer" width="420" height="540"><p class="tag">On ne naît pas manager.<br><b>Ça s’apprend.</b></p></div>
</section>
<section class="hc-s"><div class="wrap"><ul class="h2o-s">''' + STATS + '''</ul></div></section>''')
C = swap(C, '<section class="room" id="moment">', '''<section class="room pc" id="moment"><div class="wrap">
  ''' + PAIN_H + '''<p class="sub">Je ne vais pas te convaincre avec des arguments bateau. Tu les vis au quotidien.</p>
  <div class="pc-g">''' + ''.join('<div class="pc-i"><span aria-hidden="true">?</span><p>%s</p></div>' % t for t in PAINS) + '''
    <div class="pc-i me"><img src="''' + TEAL + '''" alt="" width="64" height="64"><p>Les milliards de questions que tu te poses en rentrant le soir, je me les suis déjà posées.</p></div></div>
</div></section>''')
C = C.replace('<section class="room mint" id="audit">', '<section class="room peach" id="audit">', 1)
C = swap(C, '<section class="room" id="formations">', '''<section class="room" id="formations"><div class="wrap">
  <span class="hand">Les formations</span><h2 class="h2">Comment travailler avec moi ?</h2>
  <div class="rows">
    <article class="rw big"><div class="rw-a"><span class="trk-k">Le plus complet · 12 semaines</span><h3>Ose prendre ta place</h3><p>Personne ne t’a appris à manager. Moi si. Pas à tes côtés, avec toi.</p></div>
      <ul class="rw-b">''' + chip_list(OPT) + '''</ul><div class="rw-c"><b>1 497 €</b><span>paiement en 2 fois possible</span><a class="btn rdvbtn" href="''' + FORM + '''">Découvrir</a></div></article>
    <article class="rw"><div class="rw-a"><span class="trk-k">Ta posture · 3 modules</span><h3>Incarne ta posture</h3><p>Construire ta posture de manager.</p></div>
      <ul class="rw-b">''' + chip_list(INC) + '''</ul><div class="rw-c"><b>897 €</b><a class="btn soft" href="''' + FORM + '''">Découvrir</a></div></article>
    <article class="rw"><div class="rw-a"><span class="trk-k">Ton équipe · 3 modules</span><h3>Booste ton équipe</h3><p>Agir sur ton management individuel et collectif.</p></div>
      <ul class="rw-b">''' + chip_list(BOO) + '''</ul><div class="rw-c"><b>897 €</b><a class="btn soft" href="''' + FORM + '''">Découvrir</a></div></article>
  </div>
  <p class="eq-more">Bonus inclus dans chaque parcours : l’Atelier Stratégie Managériale trimestriel</p>
</div></section>''')
C = C.replace('<section class="room peach" id="programme">', '<section class="room mint" id="programme">', 1)
q0, n0, r0, _ = AVIS[0]
C = swap(C, '<section class="room mint" id="avis">', '''<section class="room peach" id="avis"><div class="wrap">
  <div class="tm-h"><div>''' + AV_H + '''</div><p class="sp-google big">''' + P.GOOGLE + '''</p></div>
  <figure class="fq-big"><blockquote>''' + q0 + '''</blockquote><figcaption><b>''' + n0 + '''</b> · ''' + r0 + '''</figcaption></figure>
  <div class="tg2">''' + ''.join(avis(*a) for a in AVIS[1:]) + '''</div>
</div></section>''')
C = swap(C, '<section class="fin2">', '''<section class="fc"><div class="wrap"><img src="''' + ARCH_T + '''" alt="Élodie Boyer" width="420" height="540">
  <div><span class="hand">Travaillons ensemble</span>''' + FIN_T + '''<a class="btn rdvbtn big" href="''' + RDV + '''" target="_blank" rel="noopener">Je prends RDV avec Élodie ''' + ARR + '''</a></div></div></section>''')

CSS_BC = '''<style>
/* ===== B ===== */
.hb{background:var(--peach);text-align:center;overflow:hidden;}
.hb .wrap{padding-block:64px 0;}
.hb h1{font-family:var(--display);font-weight:400;font-size:clamp(44px,6.6vw,92px);line-height:1;margin:12px auto 18px;max-width:14ch;color:var(--pine);}
.hb-s{display:block;font-family:var(--hand);font-weight:700;color:var(--ember-ink);font-size:1.05em;line-height:1;transform:rotate(-2deg);}
.hb .lede{margin-inline:auto;max-width:56ch;}
.hb .ctas{justify-content:center;margin-top:28px;}
.hb-v{position:relative;width:min(100%,430px);margin:46px auto 0;}
.hb-p{display:block;width:100%;height:auto;border-radius:50% 50% 0 0;transform:translateY(8%);margin-bottom:-6%;}
.hb-st{position:absolute;background:#fff;border-radius:18px;padding:12px 16px;font-size:13.5px;font-weight:700;line-height:1.3;box-shadow:0 16px 34px -18px rgba(29,42,40,.45);text-align:left;}
.hb-st b{display:block;font-family:var(--display);font-weight:400;font-size:26px;color:var(--pine);}
.hb-st.l{left:-110px;top:28%;transform:rotate(-4deg);} .hb-st.r{right:-110px;top:52%;transform:rotate(3deg);}
.hb-badge{position:absolute;right:-30px;top:-10px;width:120px;height:120px;border-radius:50%;background:var(--ember);color:#2B1304;display:grid;place-items:center;text-decoration:none;box-shadow:0 18px 30px -16px rgba(180,86,31,.8);}
.hb-badge svg{position:absolute;inset:0;width:100%;height:100%;animation:spin 18s linear infinite;}
.hb-badge text{font-size:12px;font-weight:800;letter-spacing:.14em;fill:#2B1304;}
.hb-badge span{font-size:28px;font-weight:800;}
@keyframes spin{to{transform:rotate(360deg);}}
@media (prefers-reduced-motion:reduce){.hb-badge svg{animation:none;}}
.pb{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:56px;align-items:start;}
.pb-l{list-style:none;margin:0;padding:0;border-top:2px solid var(--ink);}
.pb-l li{display:grid;grid-template-columns:70px minmax(0,1fr);gap:16px;align-items:baseline;padding:20px 0;border-bottom:1.5px solid var(--line);}
.pb-l span{font-family:var(--display);font-size:34px;color:var(--ember);}
.pb-l p{margin:0;font-family:var(--display);font-size:clamp(19px,2vw,23px);line-height:1.3;color:var(--ink);}
.aud-dark{background:var(--pine);} .aud-dark .aud{background:#0b5f64;box-shadow:none;color:#fff;}
.aud-dark .h2{color:#fff;} .aud-dark .sub{color:var(--on-pine-soft);} .aud-dark .sub b{color:#fff;} .aud-dark .hand{color:var(--ember);}
.stairs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;align-items:end;margin-top:44px;}
.st{position:relative;padding-top:44px;}
.st-n{position:absolute;top:-22px;left:22px;min-width:46px;height:46px;padding:0 12px;border-radius:999px;display:grid;place-items:center;background:var(--ember);color:#fff;font-family:var(--display);font-size:20px;}
.st .btn{margin-top:14px;justify-content:center;}
.st.big{background:var(--pine);border-color:var(--pine);color:#fff;}
.st.big .trk-k{color:var(--ember);} .st.big h3{color:#fff;font-size:32px;} .st.big p,.st.big .trk-p span{color:var(--on-pine-soft);} .st.big li{color:#fff;} .st.big circle{fill:var(--ember);} .st.big .trk-p b{color:#FFCFA3;}
.st.big .res{font-family:var(--hand);font-size:23px;line-height:1.2;color:#fff;margin-top:8px;} .st.big .res b{color:#FFCFA3;font-weight:700;}
.st.big .btn{background:var(--ember);color:#2B1304;border-color:#E27A33;}
.st.big .st-n{background:#FFCFA3;color:var(--pine);}
.tb-h{text-align:center;display:flex;flex-direction:column;align-items:center;} .tb-h .h2{margin-inline:auto;}
.mas{columns:3 280px;column-gap:18px;margin-top:36px;}
.ms{break-inside:avoid;margin:0 0 18px;padding:24px 24px 20px;background:var(--paper);border-radius:22px;border:1.5px solid var(--line);border-left:6px solid var(--teal);}
.ms.c1{border-left-color:var(--ember);} .ms.c2{border-left-color:var(--pine);}
.ms blockquote{margin:0 0 14px;font-size:16px;line-height:1.55;color:var(--ink);}
.ms figcaption{font-size:13.5px;color:var(--muted);} .ms figcaption b{color:var(--ink);}
.ms .tm-g{margin-top:10px;}
.fb{background:var(--pine);color:#fff;} .fb .hand{color:var(--ember);} .fb h2{color:#fff;} .fb p{color:var(--on-pine-soft);} .fb .fin2-k{color:#FFCFA3;}
.fb .btn.rdvbtn{background:var(--ember);color:#2B1304;border-color:#E27A33;}
.fb .btn.rdvbtn:hover{background:#FF9F66;color:#2B1304;}
/* ===== C ===== */
.hc{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);min-height:620px;}
.hc-l{background:var(--ember);display:flex;align-items:center;}
.hc-in{padding:64px max(20px,calc((100vw - var(--maxw)) / 2 + 20px));padding-right:56px;}
.hc .hand{color:var(--pine);}
.hc h1{font-family:var(--display);font-weight:400;font-size:clamp(44px,5.8vw,80px);line-height:1.02;margin:10px 0 20px;color:#fff;text-shadow:0 2px 0 rgba(150,60,10,.25);}
.hc .lede{color:#2B1304;font-size:19px;max-width:48ch;}
.hc .ctas{margin-top:28px;}
.hc .btn:not(.hc-ghost){background:var(--pine);color:#fff;border-color:var(--pine);}
.hc-ghost{background:transparent;color:#2B1304;border:2px solid #2B1304;box-shadow:none;}
.hc-r{position:relative;background:var(--teal);}
.hc-r img{display:block;width:100%;height:100%;object-fit:cover;object-position:center top;}
.hc-r .tag{left:-40px;bottom:60px;}
.hc-s{background:var(--pine);} .hc-s .h2o-s{border-top:0;padding:30px 0;}
.pc{background:var(--pine);color:#fff;} .pc .h2{color:#fff;} .pc .hand{color:var(--ember);} .pc .sub{color:var(--on-pine-soft);}
.pc-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:16px;margin-top:34px;}
.pc-i{display:flex;gap:14px;align-items:flex-start;padding:22px;border-radius:22px;background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.12);}
.pc-i > span{flex:none;display:grid;place-items:center;width:44px;height:44px;border-radius:50%;background:var(--ember);color:#2B1304;font-family:var(--display);font-size:24px;}
.pc-i p{margin:0;font-size:16.5px;line-height:1.45;color:#fff;}
.pc-i.me{background:#FFF1C9;border-color:#FFF1C9;} .pc-i.me p{color:var(--ink);font-family:var(--hand);font-size:22px;line-height:1.2;}
.pc-i.me img{width:52px;height:52px;border-radius:50%;object-fit:cover;flex:none;}
.rows{display:grid;gap:16px;margin-top:36px;}
.rw{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1.2fr) auto;gap:28px;align-items:center;padding:26px 28px;border-radius:26px;background:var(--paper);border:2px solid var(--line);}
.rw h3{font-family:var(--display);font-weight:400;font-size:28px;margin:4px 0 6px;} .rw p{margin:0;color:var(--muted);}
.rw-b{list-style:none;margin:0;padding:0;display:grid;gap:8px;}
.rw-b li{display:flex;gap:9px;font-size:15px;line-height:1.35;} .rw-b svg{flex:none;width:18px;height:18px;} .rw-b circle{fill:var(--teal);} .rw-b path{fill:none;stroke:#fff;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;}
.rw-c{display:flex;flex-direction:column;align-items:flex-end;gap:6px;text-align:right;min-width:190px;}
.rw-c b{font-family:var(--display);font-weight:400;font-size:36px;line-height:1;} .rw-c span{font-size:13px;color:var(--muted);} .rw-c .btn{margin-top:8px;}
.rw.big{background:var(--pine);border-color:var(--pine);color:#fff;} .rw.big h3{color:#fff;} .rw.big p,.rw.big .rw-c span{color:var(--on-pine-soft);}
.rw.big .trk-k{color:var(--ember);} .rw.big li{color:#fff;} .rw.big circle{fill:var(--ember);} .rw.big .rw-c b{color:#FFCFA3;}
.fq-big{margin:36px 0 0;padding:clamp(26px,4vw,48px);border-radius:30px;background:var(--pine);color:#fff;position:relative;}
.fq-big::before{content:"“";position:absolute;top:-10px;left:28px;font-family:var(--display);font-size:140px;line-height:1;color:var(--ember);}
.fq-big blockquote{margin:30px 0 16px;font-family:var(--display);font-size:clamp(22px,2.6vw,32px);line-height:1.3;}
.fq-big figcaption{color:var(--on-pine-soft);} .fq-big figcaption b{color:#FFCFA3;}
.tg2{display:flex;flex-wrap:wrap;justify-content:center;gap:16px;margin-top:18px;}
.tg2 > .tm{flex:1 1 280px;max-width:calc((100% - 32px) / 3);}
@media (max-width:1020px){.tg2 > .tm{max-width:100%;}}
.fc{background:var(--mint);} .fc .wrap{display:grid;grid-template-columns:auto minmax(0,1fr);gap:56px;align-items:center;padding-block:clamp(56px,7vw,90px);}
.fc img{width:min(32vw,300px);height:auto;border-radius:190px 190px 26px 26px;}
.fc h2{font-family:var(--display);font-weight:400;font-size:clamp(32px,4.2vw,52px);line-height:1.08;margin:8px 0 14px;}
.fc p{margin:0 0 8px;max-width:60ch;} .fc .fin2-k{font-family:var(--hand);font-size:26px;font-weight:700;color:var(--pine);} .fc .btn{margin-top:18px;}
@media (max-width:1020px){
  .hb-st.l{left:-20px;} .hb-st.r{right:-20px;} .hb-badge{right:0;}
  .pb,.hc,.rw,.fc .wrap{grid-template-columns:1fr;} .stairs{grid-template-columns:1fr;gap:40px;max-width:560px;margin-inline:auto;}
  .hc-r{height:440px;} .hc-r .tag{left:16px;bottom:24px;} .hc-in{padding:48px 20px;} .rw-c{align-items:flex-start;text-align:left;} .fc img{width:220px;}
}
@media (max-width:560px){.hb-v{width:250px;} .hb-st.l{left:-44px;top:18%;} .hb-st.r{right:-44px;} .hb-st{padding:9px 12px;font-size:12px;} .hb-st b{font-size:21px;} .hb-badge{width:96px;height:96px;right:-30px;top:-30px;}}
</style>
'''
for name, body, extra in (('A', BODY_A, ''), ('B', B, CSS_BC), ('C', C, CSS_BC)):
    html = head + CSS_A + extra + body + defs
    html = html.replace('<title>Ose prendre ta place · Accueil</title>', '<title>Accueil version %s · Ose prendre ta place</title>' % name, 1)
    open(S + 'home/accueil-%s.html' % name, 'w', encoding='utf-8').write(html)
    print(name, len(html))
