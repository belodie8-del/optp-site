"""Test: oseprendretaplace.fr/contact rebuilt with the same codes as the new site. Not deployed anywhere."""
exec(open('_pre.py', encoding='utf-8').read())
exec(open('_cssA.py', encoding='utf-8').read())
HOME = '@@SITE@@/'
TEL = '+33 6 79 35 34 41'
MAIL = 'contact@oseprendretaplace.fr'
LINKEDIN = 'https://www.linkedin.com/in/elodie-boyer-299891143/'
I = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'
IC_TEL = I % '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>'
IC_MAIL = I % '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>'
IC_CAL = I % '<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/><path d="M9 15l2 2 4-4"/>'
IC_IN = I % '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M8 11v5M8 8v.01M12 16v-5M12 13a2 2 0 0 1 4 0v3"/>'
IC_CLIP = I % '<path d="M21 11l-8.5 8.5a5 5 0 0 1-7-7L14 4a3.5 3.5 0 0 1 5 5l-8.5 8.5a2 2 0 0 1-3-3L15 7"/>'

BODY = '''<header class="top hx"><div class="wrap">
  <a href="''' + HOME + '''" aria-label="Accueil"><svg class="logo" viewBox="0 0 287 90" role="img" aria-label="EB Formation Consulting"><use href="#optplogo"/></svg></a>
  <nav class="nav" aria-label="Menu"><a href="''' + HOME + '''">Accueil</a><a href="''' + FORM + '''">Les formations</a><a href="''' + BLOG + '''">Blog</a><a href="''' + CONTACT + '''" aria-current="page">Contact</a><a class="btn wpnav" href="https://winterpack.oseprendretaplace.fr/"><span aria-hidden="true">❄</span> Winter Pack</a><a class="btn rdvbtn" href="''' + AUDIT + '''">Audit offert</a></nav>
</div></header>
<main id="top">
<section class="kch"><div class="wrap">
  <div class="kch-t"><span class="hand">Contacte-moi</span>
    <h1>Tu as des questions ou <em>un projet en tête ?</em></h1>
    <p class="lede">Une question sur les formations, besoin d’y voir plus clair ou envie d’échanger autour d’un sujet management ?</p>
    <p class="kch-s">Remplis le formulaire juste en dessous et raconte-moi ton besoin, je te répondrai avec plaisir.</p></div>
  <div class="kch-v"><img src="''' + ARCH_T + '''" alt="Élodie Boyer" width="420" height="540"><p class="kch-bub">Travaillons ensemble 💚</p></div>
</div></section>

<section class="room kcc" id="ecrire"><div class="wrap kcg">
  <form class="kcf" id="kf" novalidate>
    <h2>Écris-moi</h2>
    <div class="kcf-r"><label class="kfl"><span>Nom</span><input type="text" name="nom" autocomplete="name" required></label>
      <label class="kfl"><span>Email</span><input type="email" name="email" autocomplete="email" required></label></div>
    <label class="kfl"><span>Sujet</span><input type="text" name="sujet" placeholder="Une formation, un projet, une question…"></label>
    <label class="kfl"><span>Message</span><textarea name="message" rows="6" placeholder="Raconte-moi ton besoin" required></textarea></label>
    <label class="katt">''' + IC_CLIP + '''<span class="katt-t">Joindre un fichier <small>(facultatif)</small></span><input type="file" name="fichier"></label>
    <button class="btn rdvbtn big" type="submit">Envoyer ''' + ARR + '''</button>
    <p class="kcf-ok" role="status" hidden>Aperçu : sur ton site, c’est le formulaire de Systeme.io qui enverra le message.</p>
  </form>
  <aside class="kco2"><p class="kor"><span>ou</span></p>
    <p class="kco2-k">Par téléphone ou mail :</p>
    <a class="kct" href="tel:+33679353441"><span class="kct-i">''' + IC_TEL + '''</span><span><small>Téléphone</small><b>''' + TEL + '''</b></span></a>
    <a class="kct" href="mailto:''' + MAIL + '''"><span class="kct-i">''' + IC_MAIL + '''</span><span><small>Email</small><b>''' + MAIL + '''</b></span></a>
    <a class="kct rdv" href="''' + RDV + '''" target="_blank" rel="noopener"><span class="kct-i">''' + IC_CAL + '''</span><span><small>On fait le point ?</small><b>Je prends RDV 30 min avec Élodie</b></span></a>
    <a class="kct" href="''' + LINKEDIN + '''" target="_blank" rel="noopener"><span class="kct-i">''' + IC_IN + '''</span><span><small>LinkedIn</small><b>Élodie Boyer</b></span></a>
  </aside>
</div></section>

<section class="room ksc" id="raccourcis"><div class="wrap">
  <div class="ctr"><span class="hand">En attendant ma réponse</span><h2 class="h2">Et si tu commençais par là ?</h2></div>
  <div class="ksc-g">
    <a class="ksc-c" href="''' + AUDIT + '''"><span class="ksc-n">01</span><b>Fais l’audit offert</b><span>3 minutes en version express ou 10 minutes pour l’audit complet, avec ton plan d’action sur 3 semaines.</span><em>Commencer l’audit →</em></a>
    <a class="ksc-c" href="''' + FORM + '''"><span class="ksc-n">02</span><b>Découvre les formations</b><span>Ose Prendre Ta Place, Incarne ta posture ou Booste ton équipe.</span><em>Voir les formations →</em></a>
    <a class="ksc-c" href="''' + BLOG + '''"><span class="ksc-n">03</span><b>Lis le blog « OSE »</b><span>Le management, version terrain. Sans jargon, sans grande théorie.</span><em>Lire les articles →</em></a>
  </div>
</div></section>
</main>
<footer><div class="wrap"><span><b>Élodie Boyer</b> · Formatrice en management passionnée qui aide les managers à réaliser leur plein potentiel<br>© 2026 EB Formation Consulting · <span class="flg"><a href="@@SITE@@/politique-de-confidentialite">Politique de confidentialité</a> · <a href="@@SITE@@/conditions-utilisation">Conditions d’utilisation</a> · <a href="@@SITE@@/politique-cookies">Politique de cookies</a></span></span><nav aria-label="Liens"><a href="''' + HOME + '''">Accueil</a><a href="''' + FORM + '''">Les formations</a><a href="''' + BLOG + '''">Blog</a><span class="fso"><a href="https://www.linkedin.com/in/elodie-boyer-299891143/" target="_blank" rel="noopener" aria-label="LinkedIn · Élodie Boyer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M8 11v5M8 8v.01M12 16v-5M12 13a2 2 0 0 1 4 0v3"/></svg></a><a href="https://www.instagram.com/elodie_boyer_off_management/" target="_blank" rel="noopener" aria-label="Instagram · elodie_boyer_off_management"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5v.01"/></svg></a></span></nav></div></footer>
<script>(function(){var f=document.getElementById('kf');f.addEventListener('submit',function(e){e.preventDefault();f.querySelector('.kcf-ok').hidden=false;});
var a=f.querySelector('.katt input'),t=f.querySelector('.katt-t');a.addEventListener('change',function(){if(a.files.length)t.textContent=a.files[0].name;});})();</script>
'''

CSS_C = '''<style>
.nav a[aria-current="page"]{color:var(--pine);font-weight:800;}
.ctr{text-align:center;display:flex;flex-direction:column;align-items:center;}
/* hero */
.kch{background:var(--peach);overflow:hidden;}
.kch .wrap{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr);gap:56px;align-items:end;padding-block:80px 0;}
.kch-t{padding-bottom:72px;}
.kch h1{font-family:var(--display);font-weight:400;font-size:clamp(40px,5.2vw,70px);line-height:1.04;margin:10px 0 22px;color:var(--pine);}
.kch h1 em{font-style:normal;color:var(--ember-ink);}
.kch .lede{font-size:20px;line-height:1.55;color:var(--ink);max-width:50ch;margin:0 0 14px;}
.kch-s{font-size:17px;line-height:1.6;color:var(--muted);max-width:50ch;margin:0;}
.kch-v{position:relative;justify-self:center;width:min(100%,300px);}
.kch-v img{display:block;width:100%;height:auto;border-radius:150px 150px 0 0;}
.kch-bub{position:absolute;left:-70px;top:24%;margin:0;background:#fff;border-radius:20px 20px 20px 6px;padding:12px 18px;font-family:var(--hand);font-weight:700;font-size:24px;color:var(--pine);box-shadow:0 18px 30px -18px rgba(29,42,40,.5);transform:rotate(-4deg);white-space:nowrap;}
/* form + contacts */
main > .room.kcc{padding-top:clamp(64px,7vw,96px);padding-bottom:clamp(56px,6vw,84px);}
.kcg{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr);gap:48px;align-items:start;}
.kcf{background:#fff;border-radius:32px;padding:clamp(28px,4vw,44px);box-shadow:0 30px 60px -44px rgba(8,80,85,.8);border:1.5px solid var(--line);display:grid;gap:18px;}
.kcf h2{font-family:var(--display);font-weight:400;font-size:32px;margin:0 0 4px;color:var(--ink);}
.kcf-r{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;}
.kfl{display:flex;flex-direction:column;gap:7px;}
.kfl span{font-size:14px;font-weight:800;color:var(--pine);}
.kfl input,.kfl textarea{font:inherit;font-size:16px;color:var(--ink);background:var(--paper);border:2px solid var(--line);border-radius:16px;padding:14px 16px;transition:border-color .15s,box-shadow .15s;resize:vertical;}
.kfl input::placeholder,.kfl textarea::placeholder{color:#9aa3a1;}
.kfl input:focus,.kfl textarea:focus{outline:none;border-color:var(--teal);box-shadow:0 0 0 4px rgba(15,134,138,.15);}
.katt{display:flex;align-items:center;gap:10px;padding:12px 16px;border:2px dashed var(--line);border-radius:16px;cursor:pointer;color:var(--pine);font-weight:800;font-size:14.5px;position:relative;}
.katt:hover{border-color:var(--teal);} .katt svg{width:20px;height:20px;flex:none;} .katt small{font-weight:600;color:var(--muted);}
.katt input{position:absolute;inset:0;opacity:0;cursor:pointer;}
.katt:focus-within{outline:3px solid var(--ember);outline-offset:2px;}
.kcf .btn{justify-self:start;margin-top:4px;}
.kcf-ok{margin:0;padding:12px 16px;border-radius:14px;background:var(--mint);color:var(--pine);font-weight:700;font-size:14.5px;}
.kco2{display:flex;flex-direction:column;gap:14px;}
.kor{display:flex;align-items:center;gap:14px;margin:0 0 6px;font-family:var(--hand);font-weight:700;font-size:30px;color:var(--ember-ink);}
.kor::before,.kor::after{content:"";flex:1;height:1.5px;background:var(--line);}
.kco2-k{margin:0;font-weight:800;color:var(--ink);}
.kct{display:flex;align-items:center;gap:16px;padding:18px 20px;border-radius:22px;background:var(--mint);text-decoration:none;color:var(--ink);transition:transform .2s,box-shadow .2s;}
.kct:hover{transform:translateX(4px);box-shadow:0 16px 28px -22px rgba(8,80,85,.7);}
.kct:focus-visible{outline:3px solid var(--ember);outline-offset:3px;}
.kct-i{flex:none;display:grid;place-items:center;width:48px;height:48px;border-radius:14px;background:#fff;color:var(--teal);}
.kct-i svg{width:24px;height:24px;}
.kct small{display:block;font-size:12.5px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);}
.kct b{display:block;font-size:17px;color:var(--pine);word-break:break-word;}
.kct.rdv{background:var(--ember);} .kct.rdv .kct-i{color:var(--ember-ink);} .kct.rdv small{color:#5a2a0c;} .kct.rdv b{color:#2B1304;}
/* shortcuts */
.ksc{background:var(--mint);}
.ksc-g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;margin-top:44px;}
.ksc-c{display:flex;flex-direction:column;gap:10px;padding:28px 26px;border-radius:26px;background:#fff;text-decoration:none;color:var(--ink);transition:transform .2s,box-shadow .2s;}
.ksc-c:hover{transform:translateY(-5px);box-shadow:0 24px 40px -30px rgba(8,80,85,.7);}
.ksc-c:focus-visible{outline:3px solid var(--ember);outline-offset:4px;}
.ksc-n{font-family:var(--display);font-size:40px;line-height:1;color:var(--teal);opacity:.6;}
.ksc-c b{font-family:var(--display);font-weight:400;font-size:24px;color:var(--pine);}
.ksc-c span:not(.ksc-n){font-size:15.5px;line-height:1.55;color:var(--muted);}
.ksc-c em{margin-top:auto;padding-top:6px;font-style:normal;font-weight:800;color:var(--ember-ink);}
@media (max-width:1020px){.kch .wrap,.kcg{grid-template-columns:1fr;} .kch-t{padding-bottom:0;} .kch-v{width:min(100%,240px);} .kch-bub{left:-40px;} .ksc-g{grid-template-columns:1fr;}}
@media (max-width:560px){.kcf-r{grid-template-columns:1fr;} .kcf .btn{justify-self:stretch;justify-content:center;} .kch-bub{left:-24px;font-size:20px;}}
@media (prefers-reduced-motion:reduce){.kct,.ksc-c{transition:none;}}
</style>
'''
h = head.replace('<title>Ose prendre ta place · Accueil</title>', '<title>Contact · Ose prendre ta place</title>', 1)
open(S + 'home/contact-test.html', 'w', encoding='utf-8').write(h + CSS_A + CSS_C + BODY + defs)
print('ok')
