"""Test: oseprendretaplace.fr blog (listing page + article template) with the same codes as the new home page.
Real articles, images and categories taken from the current blog. Not deployed anywhere."""
import json, datetime, urllib.parse
exec(open('_pre.py', encoding='utf-8').read())
exec(open('_cssA.py', encoding='utf-8').read())
B = S + 'blog/'
HOME = 'https://oseprendretaplace.fr/'
BLOGROOT = 'https://oseprendretaplace.systeme.io'
MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
def fdate(ts):
    d = datetime.datetime.utcfromtimestamp(ts) + datetime.timedelta(hours=2)
    return '%d %s %d' % (d.day, MOIS[d.month - 1], d.year)
posts = json.load(open(B + 'posts.json', encoding='utf-8'))['posts']
for i, p in enumerate(posts):
    p['name'] = p['name'].strip(); p['img'] = img('blog/img/p%d_s.jpg' % (i + 1)); p['url'] = BLOGROOT + p['path']; p['date'] = fdate(p['dateTs'])
CATS = []
for p in posts:
    for c in p['categories']:
        if c['path'] not in [x[0] for x in CATS]: CATS.append((c['path'], c['name']))
CAT_TINT = {'posture-et-legitimite': 'c1', 'manager-son-equipe': 'c2', 'deleguer-et-motiver': 'c3', 'gestion-de-conflit': 'c4'}

def nav(cur):
    return ('<header class="top hx"><div class="wrap"><a href="' + HOME + '" aria-label="Accueil"><svg class="logo" viewBox="0 0 287 90" role="img" aria-label="EB Formation Consulting"><use href="#optplogo"/></svg></a>'
            '<nav class="nav" aria-label="Menu"><a href="' + HOME + '">Accueil</a><a href="' + FORM + '">Les formations</a><a href="' + BLOG + '" aria-current="page">Blog</a><a href="' + CONTACT + '">Contact</a>'
            '<a class="btn wpnav" href="https://winterpack.oseprendretaplace.fr/"><span aria-hidden="true">❄</span> Winter Pack</a><a class="btn rdvbtn" href="' + AUDIT + '">Audit offert</a></nav></div></header>')
def chips(p): return ''.join('<span class="cat %s">%s</span>' % (CAT_TINT.get(c['path'], 'c1'), c['name']) for c in p['categories'])
def card(p, extra=''):
    return ('<a class="bc" href="%s" data-cats="%s"%s><span class="bc-i"><img src="%s" alt=""></span><span class="bc-t"><span class="bc-m">%s<span class="bc-d">%s</span></span>'
            '<span class="bc-h">%s</span><span class="bc-x">%s</span><span class="bc-r">Lire l’article →</span></span></a>') % (
        p['url'], ' '.join(c['path'] for c in p['categories']), extra, p['img'], chips(p), p['date'], p['name'], p['description'])
FOOT = ('<footer><div class="wrap"><span><b>Élodie Boyer</b> · Formatrice en management passionnée qui aide les managers à réaliser leur plein potentiel<br>© 2026 EB Formation Consulting · <span class="flg"><a href="https://oseprendretaplace.fr/politique-de-confidentialite">Politique de confidentialité</a> · <a href="https://oseprendretaplace.fr/conditions-utilisation">Conditions d’utilisation</a> · <a href="https://oseprendretaplace.fr/politique-cookies">Politique de cookies</a></span></span>'
        '<nav aria-label="Liens"><a href="' + HOME + '">Accueil</a><a href="' + FORM + '">Les formations</a><a href="' + CONTACT + '">Contact</a><span class="fso"><a href="https://www.linkedin.com/in/elodie-boyer-299891143/" target="_blank" rel="noopener" aria-label="LinkedIn · Élodie Boyer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M8 11v5M8 8v.01M12 16v-5M12 13a2 2 0 0 1 4 0v3"/></svg></a><a href="https://www.instagram.com/elodie_boyer_off_management/" target="_blank" rel="noopener" aria-label="Instagram · elodie_boyer_off_management"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5v.01"/></svg></a></span></nav></div></footer>')
NEWSBOX = ('<section class="room" id="newsletter"><div class="wrap"><div class="nlb"><img src="' + ENV + '" alt="" width="345" height="385">'
           '<div><span class="hand">Tu as aimé cet article ?</span><h2>Reçois le prochain chaque lundi</h2>'
           '<p>Chaque lundi matin à 06h30, un conseil concret sur le management, dans ta boîte mail. Du terrain et du vrai. Rejoins les <b>5&nbsp;000 managers</b> qui lisent « Le Coup de Boost Managérial ».</p>'
           '<a class="btn rdvbtn" href="' + NEWS + '" target="_blank" rel="noopener">Je m’abonne à la newsletter ' + ARR + '</a></div></div></div></section>')

CSS_B = '''<style>
.nav a[aria-current="page"]{color:var(--pine);font-weight:800;}
.cat{display:inline-block;border-radius:999px;padding:5px 11px;font-size:12px;font-weight:800;letter-spacing:.02em;}
.cat.c1{background:var(--mint);color:var(--pine);} .cat.c2{background:var(--peach2);color:var(--ember-ink);} .cat.c3{background:#FFF1C9;color:#7a5a00;} .cat.c4{background:#EDE7FF;color:#4b3a8f;}
/* listing hero */
.bh{background:var(--mint);}
.bh .wrap{padding-block:88px 56px;display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:56px;align-items:end;}
.bh h1{font-family:var(--display);font-weight:400;font-size:clamp(40px,5.4vw,72px);line-height:1.02;margin:10px 0 18px;color:var(--pine);}
.bh h1 em{font-style:normal;font-family:var(--hand);font-weight:700;color:var(--ember-ink);font-size:1.08em;}
.bh .lede{font-size:19px;line-height:1.6;color:var(--ink);max-width:52ch;margin:0;}
.bh-n{background:#fff;border-radius:26px;padding:24px 26px;box-shadow:0 22px 40px -30px rgba(8,80,85,.7);}
.bh-n .hand{font-size:24px;} .bh-n p{margin:6px 0 14px;font-size:15.5px;line-height:1.5;color:var(--ink);} .bh-n b{color:var(--pine);}
/* filters */
.flt{display:flex;flex-wrap:wrap;gap:10px;margin:0 0 36px;}
.flt button{border:2px solid var(--line);background:#fff;color:var(--ink);border-radius:999px;padding:10px 18px;font:inherit;font-size:14.5px;font-weight:800;cursor:pointer;}
.flt button:hover{border-color:var(--teal);} .flt button[aria-pressed="true"]{background:var(--pine);border-color:var(--pine);color:#fff;}
.flt button:focus-visible{outline:3px solid var(--ember);outline-offset:2px;}
/* featured */
.ft{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);border-radius:32px;overflow:hidden;background:#fff;text-decoration:none;color:var(--ink);box-shadow:0 30px 60px -44px rgba(8,80,85,.8);margin-bottom:28px;transition:transform .25s;}
.ft:hover{transform:translateY(-4px);}
.ft-i{position:relative;min-height:340px;} .ft-i img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;}
.ft-tag{position:absolute;left:20px;top:20px;background:var(--ember);color:#2B1304;border-radius:999px;padding:7px 14px;font-size:12.5px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;}
.ft-t{padding:clamp(28px,4vw,48px);display:flex;flex-direction:column;justify-content:center;gap:14px;}
.ft-h{font-family:var(--display);font-size:clamp(28px,3vw,38px);line-height:1.12;color:var(--pine);}
.ft-x{font-size:17px;line-height:1.6;color:var(--muted);}
.ft-r{font-weight:800;color:var(--ember-ink);}
/* grid */
.bg3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:26px;}
.bc{display:flex;flex-direction:column;border-radius:26px;overflow:hidden;background:#fff;text-decoration:none;color:var(--ink);border:1.5px solid var(--line);transition:transform .25s,box-shadow .25s;}
.bc:hover{transform:translateY(-5px);box-shadow:0 26px 44px -32px rgba(8,80,85,.75);}
.bc[hidden]{display:none;}
.bc-i{aspect-ratio:582/408;overflow:hidden;background:var(--mint);} .bc-i img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .4s;}
.bc:hover .bc-i img{transform:scale(1.05);}
.bc-t{display:flex;flex-direction:column;gap:10px;padding:22px 22px 24px;flex:1;}
.bc-m{display:flex;flex-wrap:wrap;align-items:center;gap:6px 8px;}
.bc-d{font-size:12.5px;font-weight:700;color:var(--muted);}
.bc-h{font-family:var(--display);font-size:21px;line-height:1.22;color:var(--ink);}
.bc-x{font-size:15px;line-height:1.55;color:var(--muted);}
.bc-r{margin-top:auto;padding-top:6px;font-weight:800;font-size:14px;color:var(--pine);}
.bc:focus-visible,.ft:focus-visible{outline:3px solid var(--ember);outline-offset:4px;}
.empty{display:none;text-align:center;color:var(--muted);padding:30px 0;}
/* audit strip */
.as{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:20px 40px;margin-top:64px;padding:30px 36px;border-radius:28px;background:var(--peach);border:2px dashed rgba(255,145,77,.6);}
.as p{margin:0;font-family:var(--display);font-size:clamp(22px,2.4vw,28px);line-height:1.25;color:var(--pine);} .as small{display:block;margin-top:6px;font-family:var(--body);font-size:15px;color:var(--muted);}
main > #articles{padding-bottom:clamp(40px,5vw,64px);}
main > #newsletter{padding-top:clamp(24px,3vw,40px);}
/* newsletter box */
.nlb{display:grid;grid-template-columns:auto minmax(0,1fr);gap:clamp(28px,5vw,64px);align-items:center;padding:clamp(32px,5vw,60px);border-radius:34px;background:var(--pine);color:#fff;}
.nlb img{width:clamp(130px,16vw,190px);height:auto;transform:rotate(-6deg);}
.nlb .hand{color:var(--ember);} .nlb h2{font-family:var(--display);font-weight:400;font-size:clamp(30px,3.6vw,44px);line-height:1.1;margin:6px 0 14px;color:#fff;}
.nlb p{margin:0 0 22px;color:var(--on-pine-soft);line-height:1.65;max-width:56ch;} .nlb p b{color:#FFCFA3;}
/* article */
.ah{background:var(--peach);}
.ah .wrap{max-width:900px;padding-block:72px 0;text-align:center;}
.crumb{font-size:14px;color:var(--muted);margin:0 0 18px;} .crumb a{color:var(--pine);font-weight:800;text-decoration:none;}
.ah h1{font-family:var(--display);font-weight:400;font-size:clamp(34px,4.6vw,58px);line-height:1.08;margin:14px auto 18px;color:var(--pine);max-width:20ch;}
.ah-x{font-size:19px;line-height:1.6;color:var(--ink);max-width:56ch;margin:0 auto 22px;}
.ah-m{display:flex;align-items:center;justify-content:center;gap:12px;font-size:14.5px;color:var(--muted);}
.ah-m img{width:44px;height:44px;border-radius:50%;object-fit:cover;} .ah-m b{color:var(--ink);}
.ah-img{margin:44px auto 0;max-width:900px;border-radius:30px 30px 0 0;overflow:hidden;aspect-ratio:582/340;}
.ah-img img{width:100%;height:100%;object-fit:cover;display:block;}
.art{max-width:720px;margin:0 auto;padding-block:64px 24px;font-size:18.5px;line-height:1.75;color:var(--ink);}
.art p{margin:0 0 22px;}
.art .lead{font-size:21px;line-height:1.6;color:var(--pine);font-weight:700;}
.art h2{font-family:var(--display);font-weight:400;font-size:clamp(26px,2.8vw,34px);line-height:1.15;margin:48px 0 18px;color:var(--pine);}
.art h2::before{content:"";display:block;width:44px;height:5px;border-radius:5px;background:var(--ember);margin-bottom:16px;}
.art .short{font-family:var(--display);font-size:22px;line-height:1.45;margin:0 0 6px;}
.art .case{padding:24px 26px;border-radius:22px;background:var(--mint);margin:0 0 18px;}
.art .case b{color:var(--pine);} .art .case em{font-style:normal;font-weight:800;color:var(--ember-ink);}
.art figure{margin:36px 0;} .art figure img{width:100%;border-radius:24px;display:block;}
.art .key{margin:40px 0;padding:34px 36px;border-radius:28px;background:var(--pine);color:#fff;text-align:center;}
.art .key span{font-family:var(--hand);font-size:24px;color:var(--ember);} .art .key p{margin:8px 0 0;font-family:var(--display);font-size:clamp(24px,2.8vw,32px);line-height:1.25;color:#fff;}
.art .end{font-family:var(--hand);font-size:30px;color:var(--pine);}
.art mark{background:none;color:var(--pine);font-weight:800;box-shadow:inset 0 -.38em 0 rgba(255,145,77,.3);padding:0 2px;}
.share{max-width:720px;margin:0 auto;display:flex;flex-wrap:wrap;align-items:center;gap:10px;padding:18px 0 0;border-top:1.5px dashed var(--line);font-size:14.5px;color:var(--muted);}
.share a{border:2px solid var(--line);border-radius:999px;padding:8px 14px;font-weight:800;color:var(--pine);text-decoration:none;} .share a:hover{border-color:var(--teal);}
.aut{max-width:720px;margin:36px auto 0;display:grid;grid-template-columns:auto minmax(0,1fr);gap:24px;align-items:center;padding:28px 30px;border-radius:28px;background:var(--peach);}
.aut img{width:96px;height:96px;border-radius:50%;object-fit:cover;border:5px solid #fff;}
.aut b{display:block;font-family:var(--display);font-weight:400;font-size:24px;color:var(--ink);}
.aut p{margin:6px 0 12px;font-size:15.5px;line-height:1.55;color:var(--ink);}
.aut .ctas{display:flex;flex-wrap:wrap;gap:10px;} .aut .btn{padding:11px 20px;font-size:14px;}
@media (max-width:1020px){.bh .wrap,.ft,.nlb{grid-template-columns:1fr;} .bg3{grid-template-columns:repeat(2,minmax(0,1fr));} .ft-i{min-height:260px;}}
@media (max-width:620px){.bg3{grid-template-columns:1fr;} .art{font-size:17.5px;} .aut{grid-template-columns:1fr;text-align:center;} .aut img{margin:0 auto;} .aut .ctas{justify-content:center;} .as{padding:24px;}}
@media (prefers-reduced-motion:reduce){.bc,.bc-i img,.ft{transition:none;}}
</style>
'''

# ---------- listing page ----------
LIST = (nav('blog') + '<main id="top">'
  '<section class="bh"><div class="wrap"><div><span class="hand">Le blog « OSE »</span><h1>Le management, <em>version terrain.</em></h1>'
  '<p class="lede">Des conseils, des outils et du concret pour t’aider à décoder les situations du quotidien et avancer dans ton rôle de manager. Sans jargon, sans grande théorie.</p></div>'
  '<div class="bh-n"><span class="hand">Chaque lundi, 6h30</span><p>Un conseil concret dans ta boîte mail, comme <b>5&nbsp;000 managers</b>.</p><a class="btn rdvbtn" href="' + NEWS + '" target="_blank" rel="noopener">Je m’abonne ' + ARR + '</a></div></div></section>'
  '<section class="room" id="articles"><div class="wrap">'
  '<div class="flt" role="group" aria-label="Filtrer par thème"><button type="button" data-f="all" aria-pressed="true">Tous les articles</button>' +
  ''.join('<button type="button" data-f="%s" aria-pressed="false">%s</button>' % c for c in CATS) + '</div>'
  '<a class="ft" href="' + posts[0]['url'] + '"><span class="ft-i"><img src="' + posts[0]['img'] + '" alt=""><span class="ft-tag">Dernier article</span></span>'
  '<span class="ft-t"><span class="bc-m">' + chips(posts[0]) + '<span class="bc-d">' + posts[0]['date'] + '</span></span><span class="ft-h">' + posts[0]['name'] + '</span>'
  '<span class="ft-x">' + posts[0]['description'] + '</span><span class="ft-r">Lire l’article →</span></span></a>'
  '<div class="bg3">' + ''.join(card(p, ' data-first' if i == 0 else '') for i, p in enumerate(posts)) + '</div><p class="empty">Pas encore d’article dans ce thème.</p>'
  '<div class="as"><p>Et toi, tu en es où dans ton management ?<small>3 minutes en version express, 10 minutes pour l’audit complet. Des vraies questions, et un premier plan d’action. C’est offert.</small></p><a class="btn rdvbtn" href="' + AUDIT + '">Faire l’audit offert ' + ARR + '</a></div>'
  '</div></section>' + NEWSBOX.replace('Tu as aimé cet article ?', 'La newsletter').replace('Reçois le prochain chaque lundi', 'Le Coup de Boost Managérial') + '</main>' + FOOT +
  '''<script>(function(){
  var bs=[].slice.call(document.querySelectorAll('.flt button')), cards=[].slice.call(document.querySelectorAll('.bg3 .bc')), ft=document.querySelector('.ft'), em=document.querySelector('.empty');
  function apply(f){ var n=0; ft.hidden = f!=='all'; ft.style.display = f==='all' ? '' : 'none';
    cards.forEach(function(c){ var show = f==='all' ? !c.hasAttribute('data-first') : (' '+c.getAttribute('data-cats')+' ').indexOf(' '+f+' ')>-1; c.hidden=!show; if(show) n++; });
    em.style.display = n ? 'none' : 'block'; }
  bs.forEach(function(b){ b.addEventListener('click', function(){ bs.forEach(function(x){ x.setAttribute('aria-pressed', x===b ? 'true':'false'); }); apply(b.getAttribute('data-f')); }); });
  apply('all');
})();</script>''')

# ---------- article template (doliprane) ----------
P2 = posts[1]
INIMG = img('blog/img/in1_s.jpg')
ART = (nav('blog') + '<main id="top">'
  '<section class="ah"><div class="wrap"><p class="crumb"><a href="' + BLOG + '">← Le blog « OSE »</a></p>' + chips(P2) +
  '<h1>' + P2['name'] + '</h1><p class="ah-x">' + P2['description'] + '</p>'
  '<p class="ah-m"><img src="' + TEAL + '" alt=""><span><b>Élodie Boyer</b> · ' + P2['date'] + ' · 3 min de lecture</span></p>'
  '<div class="ah-img"><img src="' + P2['img'] + '" alt=""></div></div></section>'
  '<article class="wrap"><div class="art">'
  '<p class="lead">Ton collaborateur rate ses objectifs. Tu refais un point avec lui. Ça se passe bien. Et trois semaines après : même problème…</p>'
  '<p>Et si tu soignais le symptôme plutôt que la maladie ?</p>'
  '<h2>Le « réflexe doliprane »</h2>'
  '<p class="short">Quand tu as mal à la tête : tu prends un doliprane.<br>Tu ne cherches pas pourquoi tu as mal à la tête.<br>Tu veux juste que ça passe.</p>'
  '<p>Ce réflexe qu’on a tous, il existe aussi en management. Et la plupart du temps, <mark>on ne s’en rend même pas compte</mark>.</p>'
  '<h2>Le pansement managérial, c’est quoi ?</h2>'
  '<p>En management, on prescrit sans le savoir beaucoup de doliprane. <mark>On traite ce qu’on voit. Pas l’origine du problème.</mark></p>'
  '<div class="case"><p><b>Ton collaborateur n’atteint pas ses objectifs ?</b> Tu lui refais un point sur ses objectifs. <em>(Le doliprane.)</em></p><p style="margin:0">Mais la vraie question c’est : est-ce qu’il avait les moyens de les atteindre ? Les ressources. Le temps. Les compétences. Tu ne t’es pas assuré(e) qu’il avait tous les outils.</p></div>'
  '<div class="case"><p><b>Ton collaborateur démissionne ?</b> Tu organises son pot de départ. <em>(Le doliprane.)</em></p><p style="margin:0">Mais la vraie question c’est : est-ce que les signaux étaient là depuis longtemps et que personne n’a cherché l’origine ? Pour que ça ne se reproduise plus.</p></div>'
  '<p>Dans les deux cas, c’est ça l’origine de la douleur.</p>'
  '<figure><img src="' + INIMG + '" alt=""></figure>'
  '<h2>Soulager ou guérir ?</h2>'
  '<p>Le doliprane soulage. Mais il ne guérit pas.</p><p>Avant ta prochaine réaction face à un problème dans ton équipe, pose-toi une seule question :</p>'
  '<div class="key"><span>La seule question à te poser</span><p>Est-ce que je traite la cause ou la conséquence ?</p></div>'
  '<p class="end">C’est ça le vrai management 💚</p></div>'
  '<div class="share"><span>Partager l’article :</span><a href="https://www.linkedin.com/sharing/share-offsite/?url=' + urllib.parse.quote(P2['url'], safe='') + '" target="_blank" rel="noopener">LinkedIn</a><a href="mailto:?subject=' + urllib.parse.quote(P2['name']) + '&amp;body=' + urllib.parse.quote(P2['url'], safe='') + '">Par mail</a></div>'
  '<div class="aut"><img src="' + ARCH_T + '" alt="Élodie Boyer"><div><b>Élodie Boyer</b><p>Formatrice en management passionnée qui aide les managers à réaliser leur plein potentiel. Plus de 10 ans d’expérience terrain.</p>'
  '<div class="ctas"><a class="btn rdvbtn" href="' + AUDIT + '">Faire l’audit offert</a><a class="btn soft" href="' + FORM + '">Découvrir les formations</a></div></div></div></article>'
  '<section class="room" id="lire"><div class="wrap"><span class="hand">À lire aussi</span><h2 class="h2">D’autres articles qui pourraient te parler</h2><div class="bg3">' +
  ''.join(card(p) for p in [posts[3], posts[6], posts[0]]) + '</div></div></section>' + NEWSBOX + '</main>' + FOOT)

for name, body, title in (('blog-test.html', LIST, 'Le blog « OSE » · Ose prendre ta place'), ('article-test.html', ART, P2['name'] + ' · Le blog « OSE »')):
    h = head.replace('<title>Ose prendre ta place · Accueil</title>', '<title>%s</title>' % title, 1)
    open(S + 'home/' + name, 'w', encoding='utf-8').write(h + CSS_A + CSS_B + body + defs)
    print(name, len(h + CSS_A + CSS_B + body + defs))
