"""Test v2: oseprendretaplace.fr home page, same design codes as the Winter Pack (palette, fonts, finish)
but its own layouts, and no Winter Pack mention. Not deployed anywhere."""
import base64, re, sys
S = '/tmp/claude-0/-home-user-optp-site/1386eaca-821b-50a5-926e-8bdc38c36a33/scratchpad/'
sys.path.insert(0, S + 'wp5')
import proof5 as P

wp = open('/home/user/optp-site/winter-pack.html', encoding='utf-8').read()
head = wp[:wp.index('<header')]
head = re.sub(r'<title>[^<]*</title>', '<title>Ose prendre ta place · Accueil</title>', head, 1)
head = '<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n' + head
defs = wp[wp.index('<svg width="0" height="0"'):]
defs = defs[:defs.index('</svg>') + len('</svg>')]
img = lambda f: 'data:image/jpeg;base64,' + base64.b64encode(open(S + f, 'rb').read()).decode()
ORANGE, TEAL = img('elodie-640.jpg'), img('elodie-teal-640.jpg')
ARCH_O, ARCH_T = img('home/elodie-arch-orange.jpg'), img('home/elodie-arch-teal.jpg')
POST_IMG = [img('home/blogimg/s%d.jpg' % i) for i in range(1, 5)]
news = open(S + 'site/logos/news.svg', encoding='utf-8').read().replace('width="884" height="425" viewBox="0 0 884 425"', 'width="345" height="385" viewBox="0 45 345 385"')
ENV = 'data:image/svg+xml;base64,' + base64.b64encode(news.encode()).decode()

AUDIT = 'https://auditmanagerial.oseprendretaplace.fr/'
FORM = '@@SITE@@/formations'
BLOG = 'https://oseprendretaplace.systeme.io/leblogose'
CONTACT = '@@SITE@@/contact'
RDV = 'https://calendly.com/eb-formationconsulting/30min'
WPK = 'https://winterpack.oseprendretaplace.fr/'
LINKEDIN = 'https://www.linkedin.com/in/elodie-boyer-299891143/'
INSTA = 'https://www.instagram.com/elodie_boyer_off_management/'
LOGO_LI = ('<svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="11" fill="#0A66C2"/>'
           '<path fill="#fff" d="M13 19h5v16h-5zM15.5 10.8a2.9 2.9 0 1 1 0 5.8 2.9 2.9 0 0 1 0-5.8zM21 19h4.8v2.2h.1c.7-1.3 2.3-2.6 4.8-2.6 5.1 0 6.1 3.4 6.1 7.7V35h-5v-7.8c0-1.9 0-4.3-2.6-4.3s-3 2-3 4.1V35h-5z"/></svg>')
LOGO_IG = ('<svg viewBox="0 0 48 48" aria-hidden="true"><defs><radialGradient id="soc-ig" cx="30%" cy="107%" r="150%"><stop offset="0" stop-color="#FDF497"/><stop offset=".05" stop-color="#FDF497"/>'
           '<stop offset=".45" stop-color="#FD5949"/><stop offset=".6" stop-color="#D6249F"/><stop offset=".9" stop-color="#285AEB"/></radialGradient></defs>'
           '<rect width="48" height="48" rx="12" fill="url(#soc-ig)"/><rect x="11" y="11" width="26" height="26" rx="8" fill="none" stroke="#fff" stroke-width="3"/>'
           '<circle cx="24" cy="24" r="6.2" fill="none" stroke="#fff" stroke-width="3"/><circle cx="31.6" cy="16.4" r="1.9" fill="#fff"/></svg>')
WP_AP = [img('home/wpap/s%d.jpg' % n) for n in (1, 2, 7)]
WP_TOOLS = ['L’entretien professionnel', 'L’entretien annuel', 'La réunion d’équipe', 'La trame du OTO',
            'Le tableau de bord des objectifs', 'Le calendrier des rituels', 'Les 10 commandements', 'Le kit de survie verbal']
NEWS = P.NEWS_URL
CHK = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M7.5 12.5l3 3 6-6.5"/></svg>'
ARR = '<span aria-hidden="true">→</span>'

PAINS = ['Tu rentres le soir en te demandant comment tu vas gérer la situation de demain.',
         'Tu cherches des réponses en cachette sur ChatGPT, et tu ne trouves que des réponses génériques qui ne connaissent ni ton équipe, ni ton contexte.',
         'Tu fais semblant de ne pas entendre ce qu’il se passe, parce que tu ne sais pas comment le gérer.',
         'Tu rejoues la scène de la réunion dans ta tête, en te disant que t’aurais dû dire autrement.',
         'Tu as peur de dire à ton N+1 que tu n’y arrives pas.']
MODULES = [('RESET', 'Arrête de deviner ce qu’on attend de toi'), ('La Lecture d’Équipe', 'Arrête de manager tout le monde pareil'), ('Posture & Crédibilité', 'Une autorité naturelle, sans crier'), ('Courage & Influence', 'Ose dire les choses, et que ça se passe bien'), ('L’Alliance Individuelle', 'Fais grandir chacun, sans tout porter seul(e)'), ('Le Collectif', 'Une équipe soudée, même quand ça secoue')]
KIT = ['Vidéos pédagogiques', 'Workbooks à compléter', 'Fiches outils', 'Feuilles de route Notion', 'Challenges', 'Quiz']
_I = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'
KIT_ICONS = [_I % '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="M10 9.5v5l4.5-2.5z"/>',
             _I % '<path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4"/><path d="M9 17l1-3 5-5 2 2-5 5z"/>',
             _I % '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h4"/>',
             _I % '<path d="M9 6h11M9 12h11M9 18h11"/><path d="M3.5 6l1.2 1.2 2-2.2M3.5 12l1.2 1.2 2-2.2M3.5 18l1.2 1.2 2-2.2"/>',
             _I % '<path d="M8 4h8v5a4 4 0 0 1-8 0z"/><path d="M8 6H5a3 3 0 0 0 3 4M16 6h3a3 3 0 0 1-3 4"/><path d="M12 13v4M9 20h6"/>',
             _I % '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.5v.4"/><path d="M12 17h.01"/>']
KIT_NOTE = {'Feuilles de route Notion': 'trames, checklists, modèles prêts à l’emploi'}
AVIS = [
 ("Excellente formation ! J’en ressors enrichie, confiante et pleinement motivée pour la suite. Un immense merci à Élodie pour son accompagnement de grande qualité. Son expertise, son expérience et surtout sa passion sont une véritable source d’inspiration. Je suis très reconnaissante d’avoir eu l’opportunité de croiser son chemin.", "Sandrine R.", "Responsable Administrative", False),
 ("Une formatrice au top, à l’écoute, solaire, enrichissante ! Il y a toujours une solution, et Élodie va la co-construire avec vous. Merci !!", "Élisa G.", "Responsable de Pôle", True),
 ("J’ai suivi le Pack Booste ton équipe avec l’accompagnement d’Élodie et ça a été un vrai déclic ! Le contenu de la formation est loin de ce que j’avais suivi jusqu’à aujourd’hui. Concret, pratique ! Élodie m’a donné des clés concrètes adaptées à ma situation. Je recommande +++", "Célia M.", "Futur Manager", True),
 ("J’ai pu accéder au module individuel pour renforcer mes compétences en management. Je sors de ce parcours avec des clés pour pouvoir suivre et accompagner au mieux mes collaborateurs. Une vraie valeur ajoutée par rapport aux autres formations.", "Anthony D.", "Dirigeant BTP", False),
 ("J’avais l’habitude de manager tout le monde de la même façon pendant des années. La matrice me permet aujourd’hui de savoir manager toutes les personnalités de mon équipe ! Les vidéos ne sont pas de la grande théorie déconnectée de la réalité, bien au contraire. Merci Élodie pour ces prises de conscience.", "Mégane J.", "Manager d’agence", False),
 ("J’ai suivi la formation digitale et j’ai été très agréablement surpris par la qualité du contenu ! Des outils concrets pour évoluer dans le domaine du management ! Merci à Élodie pour ces précieux conseils !", "Adrien S.", "Responsable Commercial", True),
]
POST_URLS = ['https://oseprendretaplace.systeme.io/leblogose/sachet-bonbons-management', 'https://oseprendretaplace.systeme.io/leblogose/annoncer-une-decision-difficile',
             'https://oseprendretaplace.systeme.io/leblogose/solitude-du-manager', 'https://oseprendretaplace.systeme.io/leblogose/manager-la-gen-z']
POSTS = ['Ce que 82 000 abonnés et des sachets de bonbons m’ont appris sur le management',
         '« Ils ont décidé que... » : le réflexe toxique du manager',
         'Tu te souviens de la dernière fois que tu as déjeuné avec ton équipe ?',
         'La Gen Z : l’éternel débat. Et si on changeait enfin d’angle ?']

def track(name, line, pitch, promise, mods, price, note):
    return ('<article class="trk"><span class="trk-k">3 modules</span><h3>%s</h3><p class="trk-w">%s</p><p>%s</p><ul>%s</ul>'
            '<p class="trk-pr">%s</p><div class="trk-p"><b>%s</b><span>%s</span></div></article>') % (
        name, line, pitch, ''.join('<li>%s<span>%s</span></li>' % (CHK, m) for m in mods), promise, price, note)
def avis(q, n, r, g):
    ver = ('<span class="tm-g">%s Avis Google vérifié</span>' % P.GLOGO) if g else ''
    return '<figure class="tm"><span class="tm-q" aria-hidden="true">“</span><blockquote>%s</blockquote><figcaption><span class="tm-i" aria-hidden="true">%s</span><span><b>%s</b>%s</span></figcaption>%s</figure>' % (
        q, ''.join(w[0] for w in n.replace('.', '').split()[:2]), n, r, ver)

STATS = ''.join('<li><b>%s</b><span>%s</span></li>' % x for x in P.STATS)

BODY = '''<header class="top hx"><div class="wrap">
  <a href="#top" aria-label="Accueil"><svg class="logo" viewBox="0 0 287 90" role="img" aria-label="EB Formation Consulting"><use href="#optplogo"/></svg></a>
  <nav class="nav" aria-label="Menu"><a href="#formations">Les formations</a><a href="''' + BLOG + '''">Blog</a><a href="''' + CONTACT + '''">Contact</a><a class="btn wpnav" href="https://winterpack.oseprendretaplace.fr/"><span aria-hidden="true">❄</span> Winter Pack</a><a class="btn rdvbtn" href="''' + AUDIT + '''">Audit offert</a></nav>
</div></header>
<main id="top">

<section class="h2o"><div class="wrap">
  <div class="h2o-t">
    <span class="hand">Formation en ligne · par Élodie Boyer</span>
    <h1>Ose prendre ta place <em>de manager<svg viewBox="0 0 300 24" aria-hidden="true" preserveAspectRatio="none"><path d="M4 16C60 6 150 4 296 12" /></svg></em></h1>
    <p class="lede">Une méthode concrète pour incarner une autorité naturelle, fédérer ton équipe et retrouver le plaisir de manager, même si tu n’as jamais été formé(e).</p>
    <div class="ctas"><a class="btn rdvbtn" href="#formations">Découvrir les formations ''' + ARR + '''</a><a class="btn ghost" href="''' + AUDIT + '''">Faire l’audit offert</a></div>
  </div>
  <div class="h2o-v">
    <div class="arch"><img src="''' + ARCH_O + '''" alt="Élodie Boyer" width="420" height="540"></div>
    <p class="tag">On ne naît pas manager.<br><b>Ça s’apprend.</b></p>
  </div>
</div>
<div class="wrap"><ul class="h2o-s">''' + STATS + '''</ul></div></section>

''' + P.BAND + '''
<section class="room" id="moment"><div class="wrap mo">
  <div class="mo-h"><span class="hand">On fait le point ?</span><h2 class="h2">Pourquoi c’est le moment</h2>
    <p class="sub">Je ne vais pas te convaincre avec des arguments bateau. Tu les vis au quotidien.</p>
    <p class="mo-me"><img src="''' + TEAL + '''" alt="" width="56" height="56"><span>Les milliards de questions que tu te poses en rentrant le soir, je me les suis déjà posées.</span></p></div>
  <div class="chatlist">''' + ''.join('<p class="bub%s">%s</p>' % (' r' if i % 2 else '', t) for i, t in enumerate(PAINS)) + '''</div>
</div></section>

<section class="room mint" id="audit"><div class="wrap">
  <div class="aud">
    <span class="hand">Audit offert</span><h2 class="h2 aud-h">Mon outil préféré (offert) pour transformer ton management</h2>
    <div class="aud-o">
      <a class="ao ex" href="''' + AUDIT + '''"><span class="ao-i" aria-hidden="true">⚡</span><span class="ao-k">Version express · 3 min</span><b>Mon profil en 3 minutes</b>
        <span class="ao-t">10 questions pour révéler ton <strong>style dominant</strong> et ton <strong>point de vigilance</strong>.</span><span class="ao-c">Commencer l’audit express →</span></a>
      <a class="ao co" href="''' + AUDIT + '''"><span class="ao-i" aria-hidden="true">✦</span><span class="ao-k">Audit complet · 10 min</span><b>Mon analyse détaillée</b>
        <span class="ao-t">31 questions : radar de maturité, forces, axes, et ton <strong>plan d’action sur 3 semaines</strong>.</span><span class="ao-c">Commencer l’audit complet →</span></a>
    </div>
    <p class="aud-n"><b>Des vraies questions. Un vrai diagnostic.</b> Et un premier plan d’action pour savoir exactement quoi changer dans ton management, dès maintenant.</p>
  </div>
</div></section>

<section class="room" id="formations"><div class="wrap">
  <span class="hand">Les formations</span>
  <h2 class="h2">Comment travailler avec moi ?</h2>
  <p class="sub">Deux parcours de 3 modules pour un besoin précis. Ou les deux réunis, avec moi à tes côtés pendant 12 semaines.</p>
  <div class="eq">''' + track('Incarne ta posture', 'Tu as le titre de manager, mais tu as encore l’impression de faire semblant.', 'Il est temps de poser pour de vrai ton autorité, ta posture et ta façon de communiquer.', 'Tout ce qu’il faut pour que la méthode devienne la tienne.', ['RESET', 'Lecture d’équipe', 'Posture & Crédibilité', '3 séances de coaching avec Élodie'], '897 €', 'le parcours') + '''
    <span class="eq-op" aria-hidden="true">+</span>''' + track('Booste ton équipe', 'Ton équipe n’avance pas comme tu veux. Tes 1-to-1 ne servent à rien et tes réunions non plus.', 'On repart de zéro sur tout ce qui fait qu’une équipe performe vraiment.', 'Tout ce qu’il faut pour que diriger une équipe devienne une évidence, pas une épreuve.', ['Courage & Influence', 'Alliance individuelle', 'Collectif', '3 séances de coaching avec Élodie'], '897 €', 'le parcours') + '''
    <span class="eq-op eq-eq" aria-hidden="true">=</span>
    <article class="trk big"><div class="bg-a"><span class="trk-k">La transformation complète · 12 semaines</span><h3>Ose prendre ta place</h3>
      <p class="trk-w">Personne ne t’a appris à manager. Moi si.</p><p>Pas à tes côtés, mais avec toi, sur les 6 compétences qui font un vrai manager, pendant 12 semaines.</p>
      <p class="res">Tu n’improvises plus. <b>Tu sais.</b><br>Tu n’esquives plus. <b>Tu oses.</b><br>Tu n’attends plus d’être légitime. <b>Tu l’es.</b></p></div>
      <div class="bg-b"><ul><li>''' + CHK + '''<span>Les 6 modules</span></li><li>''' + CHK + '''<span>6 séances de coaching individuel avec Élodie</span></li><li>''' + CHK + '''<span>Le groupe WhatsApp privé</span></li><li>''' + CHK + '''<span>Les lives exclusifs de la communauté</span></li></ul>
      <p class="trk-pr">Tout ce qu’il faut pour ne plus jamais te demander si tu es fait pour être manager.</p>
      <div class="trk-p"><b>1 497 €</b><span>paiement en 2 fois possible</span></div>
      <a class="btn" href="''' + FORM + '''">Découvrir la formation ''' + ARR + '''</a></div></article>
  </div>
  <p class="eq-more"><a href="''' + FORM + '''">Voir le détail des deux parcours ''' + ARR + '''</a> · Bonus inclus : l’Atelier Stratégie Managériale trimestriel, Manager, mais pour toi aussi.</p>
  <p class="fm-quote">« Passer enfin du savoir-faire au savoir-faire faire. »</p>
</div></section>

<section class="room peach" id="programme"><div class="wrap">
  <div class="pg-h"><span class="hand">Le programme</span>
  <h2 class="h2">6 modules pour construire ton management, étape par étape</h2>
  <p class="sub">De ta prise de posture à la dynamique de ton équipe, chaque module travaille une dimension concrète de ton rôle de manager.</p></div>
  <ol class="mods">''' + ''.join('<li><span class="mn">%02d</span><b>%s</b><span>%s</span></li>' % (i + 1, m, t) for i, (m, t) in enumerate(MODULES)) + '''</ol>
  <div class="kit2"><div class="kit2-h"><span class="hand">Le Kit du Manager</span>
      <h3>Pas seulement des vidéos. <em>Une vraie boîte à outils.</em></h3>
      <p>Des outils pour que la méthode ne reste pas dans ta tête, mais pour l’intégrer complètement à ton quotidien. Inclus dans chaque module :</p></div>
    <ul class="kit2-l">''' + ''.join('<li><span class="ki">%s</span><span><b>%s</b>%s</span></li>' % (KIT_ICONS[i], k, ('<small>%s</small>' % KIT_NOTE[k]) if k in KIT_NOTE else '') for i, k in enumerate(KIT)) + '''</ul></div>
</div></section>

<section class="room wpk" id="winter-pack"><div class="wpk-fl" aria-hidden="true">''' + ''.join('<i style="left:%d%%;top:%d%%;font-size:%dpx">❄</i>' % f for f in [(4, 12, 22), (14, 70, 14), (30, 8, 16), (47, 88, 12), (58, 6, 20), (73, 80, 15), (88, 14, 24), (95, 60, 13)]) + '''</div><div class="wrap wpk-g">
  <div class="wpk-t">
    <span class="hand">Nouveau cet hiver</span>
    <h2 class="h2">Winter Pack <span>L’Essentiel du Manager</span></h2>
    <p class="sub">8 outils prêts à l’emploi pour mener tes entretiens et tes rituels d’équipe avec une vraie méthode. Pour toi, ou pour tous les managers de ta PME.</p>
    <ul class="wpk-l">''' + ''.join('<li>' + CHK + '<span>%s</span></li>' % t for t in WP_TOOLS) + '''</ul>
    <div class="wpk-o">
      <a class="wpk-c" href="''' + WPK + '''#offre"><small>Pour un manager</small><b>Winter Pack Solo</b><span>197 €</span></a>
      <a class="wpk-c" href="''' + WPK + '''#offre"><small>Pour toute ta PME</small><b>Winter Pack PME</b><span>dès 490 €</span></a>
    </div>
    <p class="wpk-gift" data-wpk-gift>🎁 <span><b>Cadeau de lancement :</b> le kit d’invitation à l’entretien offert pour tout achat avant dimanche.</span></p>
    <a class="btn rdvbtn" href="''' + WPK + '''">Découvrir le Winter Pack ''' + ARR + '''</a>
  </div>
  <div class="wpk-v" aria-hidden="true">
    <img class="wpk-d d1" src="''' + WP_AP[1] + '''" alt="" width="520" height="735">
    <img class="wpk-d d2" src="''' + WP_AP[2] + '''" alt="" width="520" height="735">
    <img class="wpk-d d3" src="''' + WP_AP[0] + '''" alt="" width="520" height="735">
    <span class="wpk-st"><b>8</b>outils prêts<br>à l’emploi</span>
  </div>
</div>
<script>(function(){if(Date.now()>Date.UTC(2026,9,25,22,59,59)){var g=document.querySelector('[data-wpk-gift]');if(g)g.hidden=true;}})();</script>
</section>

<section class="room" id="elodie"><div class="wrap ab">
  <div class="ab-v"><img src="''' + ARCH_T + '''" alt="Élodie Boyer" width="420" height="540"><p class="ab-n"><b>Élodie Boyer</b>Formatrice en management passionnée qui aide les managers à réaliser leur plein potentiel</p></div>
  <div class="ab-t"><span class="hand">Hello, moi c’est Élodie !</span>
    <h2 class="h2">Formatrice en management</h2>
    <p class="ab-role">Fondatrice d’EB Formation Consulting et créatrice de Ose Prendre ta Place !</p>
    <ul class="ab-c"><li><b>+10 ans</b>d’expérience terrain</li><li><b>CNAM</b>Master en droit du travail</li><li><b>ESSEC</b>Certification management</li></ul>
    <p>Après plus de 12 ans à manager des équipes, j’ai eu un jour une envie folle : accompagner des managers ! Parce que les concepts théoriques des livres de management, c’est bien 2 secondes, mais la réalité est beaucoup plus complexe…</p>
    <p><b>Mes managers chouchous :</b> les experts qu’on vient de nommer managers. Ceux qui étaient les meilleurs dans leur métier et à qui personne n’a jamais appris à manager une équipe.</p>
    <p>Je m’attaque à des sujets qui font peur : recadrer un collaborateur, poser sa posture, animer une réunion qui sert vraiment à quelque chose, déléguer sans perdre le contrôle. Et je les rends accessibles, actionnables, humains.</p>
    <p class="ab-sign">Parce qu’on ne naît pas manager. Ça s’apprend. Et c’est exactement ce que je suis là pour faire. 💚</p></div>
</div>
<div class="wrap"><div class="why2">
  <div class="why2-a"><span class="hand">Pourquoi je peux te former ?</span>
    <p class="why2-q"><span aria-hidden="true">“</span>Parce que j’ai fait toutes les erreurs possibles.</p></div>
  <div class="why2-b"><p>J’ai été manager autoritaire, celle qui pense qu’un ordre bien donné suffit. Puis je suis passée à l’autre extrême : manager Bisounours, à dire oui à tout, à vouloir être aimée plutôt que respectée.</p>
    <p>Je ne te parle pas de théorie. Je te parle de douze ans à manager des équipes grandes, moyennes et petites, sur site, à distance, à l’échelle nationale. J’ai testé, je me suis plantée, j’ai recommencé.</p></div>
</div></div>
</section>

<section class="room mint" id="avis"><div class="wrap">
  <div class="tm-h"><div><span class="hand">Ils témoignent</span><h2 class="h2">Ce que disent les managers formés</h2></div><p class="sp-google big">''' + P.GOOGLE + '''</p></div>
  <div class="tms">''' + ''.join(avis(*a) for a in AVIS) + '''</div><p class="tm-hint">Fais défiler pour lire tous les avis →</p>
</div></section>

<section class="room" id="newsletter"><div class="wrap">
  <div class="nl"><img src="''' + ENV + '''" alt="" width="345" height="385">
    <div><span class="hand">La newsletter</span><h2>Le Coup de Boost Managérial</h2>
      <p class="nl-k">Conseils concrets, actionnables et utiles au quotidien</p>
      <p class="nl-s"><b>5 000</b> managers la lisent chaque lundi, depuis mars 2025.</p>
      <p>Chaque lundi matin à 06h30, tu ouvres ta boîte mail et tu trouves un conseil concret sur le management. Du terrain et du vrai. Un truc que tu peux appliquer dans la seconde avec ton équipe.</p>
      <p class="nl-h">Parce que manager au feeling, ça use. Et t’as mieux à faire que de réinventer la roue chaque matin.</p>
      <a class="btn" href="''' + NEWS + '''" target="_blank" rel="noopener">Je m’abonne ''' + ARR + '''</a></div></div>
</div></section>

<section class="room" id="blog"><div class="wrap">
  <div class="bg-h"><div><span class="hand">Le blog « OSE »</span><h2 class="h2">Le management, version terrain.</h2>
    <p class="sub">Des conseils, des outils et du concret pour t’aider à décoder les situations du quotidien et avancer dans ton rôle de manager. Sans jargon, sans grande théorie.</p></div>
    <a class="btn soft" href="''' + BLOG + '''">Découvrir tous les articles ''' + ARR + '''</a></div>
  <div class="posts2">''' + ''.join('<a class="pc2" href="%s"><span class="pc2-i"><img src="%s" alt="" width="640" height="480" loading="lazy"></span><span class="pc2-t"><span class="pc2-k">Article</span><span class="pc2-h">%s</span><span class="pc2-m">Lire l’article →</span></span></a>' % (POST_URLS[i], POST_IMG[i], p) for i, p in enumerate(POSTS)) + '''</div>
</div></section>

<section class="soc" id="reseaux"><div class="wrap">
  <div class="soc-h"><span class="hand">Restons connectés</span><h2 class="h2">Suis-moi sur les réseaux</h2></div>
  <div class="soc-g">
    <a class="soc-c" href="''' + LINKEDIN + '''" target="_blank" rel="noopener"><span class="soc-l">''' + LOGO_LI + '''</span>
      <span class="soc-t"><small>LinkedIn</small><b>Élodie Boyer</b><span>Mes posts sur le management, version terrain.</span></span><span class="soc-a">Me suivre <span aria-hidden="true">→</span></span></a>
    <a class="soc-c" href="''' + INSTA + '''" target="_blank" rel="noopener"><span class="soc-l">''' + LOGO_IG + '''</span>
      <span class="soc-t"><small>Instagram</small><b class="soc-hd">@elodie_<wbr>boyer_<wbr>off_<wbr>management</b><span>Des conseils management en format court.</span></span><span class="soc-a">Me suivre <span aria-hidden="true">→</span></span></a>
  </div>
</div></section>

<section class="fin2"><div class="wrap">
  <span class="hand">Travaillons ensemble</span>
  <h2>Ose prendre ta place de manager et libère ton potentiel !</h2>
  <p>30 minutes pour faire le point sur ta situation managériale : on identifie ce qui bloque vraiment, je te donne mon analyse directe, et on voit ensemble quelle formule peut t’aider à avancer.</p>
  <p class="fin2-k">Pas de pression. Juste de l’efficacité !</p>
  <a class="btn rdvbtn big" href="''' + RDV + '''" target="_blank" rel="noopener">Je prends RDV avec Élodie ''' + ARR + '''</a>
</div></section>
</main>
<footer><div class="wrap"><span><b>Élodie Boyer</b> · Formatrice en management passionnée qui aide les managers à réaliser leur plein potentiel<br>© 2026 EB Formation Consulting · <span class="flg"><a href="@@SITE@@/politique-de-confidentialite">Politique de confidentialité</a> · <a href="@@SITE@@/conditions-utilisation">Conditions d’utilisation</a> · <a href="@@SITE@@/politique-cookies">Politique de cookies</a></span></span><nav aria-label="Liens"><a href="''' + FORM + '''">Les formations</a><a href="''' + BLOG + '''">Blog</a><a href="''' + CONTACT + '''">Contact</a><span class="fso"><a href="https://www.linkedin.com/in/elodie-boyer-299891143/" target="_blank" rel="noopener" aria-label="LinkedIn · Élodie Boyer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M8 11v5M8 8v.01M12 16v-5M12 13a2 2 0 0 1 4 0v3"/></svg></a><a href="https://www.instagram.com/elodie_boyer_off_management/" target="_blank" rel="noopener" aria-label="Instagram · elodie_boyer_off_management"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5v.01"/></svg></a></span></nav></div></footer>
'''

CSS = '''<style>
/* header: plain white, orange CTA */
.hx .nav .rdvbtn{padding:11px 22px;}
/* hero: pine block, arch photo */
.h2o{background:var(--pine);color:#fff;overflow:hidden;position:relative;}
.h2o::before{content:"";position:absolute;right:-120px;top:-140px;width:520px;height:520px;border-radius:50%;background:rgba(255,255,255,.05);}
.h2o > .wrap:first-child{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:56px;align-items:end;padding-block:72px 40px;position:relative;}
.h2o .hand{color:var(--ember);}
.h2o h1{font-family:var(--display);font-weight:400;font-size:clamp(46px,6.4vw,84px);line-height:1;margin:10px 0 22px;color:#fff;}
.h2o h1 em{font-style:normal;color:var(--ember);position:relative;display:inline-block;white-space:nowrap;}
.h2o h1 em svg{position:absolute;left:0;right:0;bottom:-12px;width:100%;height:18px;}
.h2o h1 em path{fill:none;stroke:#FFCFA3;stroke-width:6;stroke-linecap:round;}
.h2o .lede{color:var(--on-pine-soft);font-size:19px;max-width:52ch;}
.h2o .ctas{margin-top:30px;}
.btn.ghost{background:transparent;color:#fff;border:2px solid rgba(255,255,255,.6);box-shadow:none;}
.btn.ghost:hover{background:rgba(255,255,255,.1);color:#fff;}
.h2o-v{position:relative;justify-self:center;width:min(100%,360px);}
.arch{border-radius:190px 190px 28px 28px;overflow:hidden;background:var(--ember);aspect-ratio:420/540;border:8px solid rgba(255,255,255,.12);}
.arch img{display:block;width:100%;height:100%;object-fit:cover;object-position:center top;}
.tag{position:absolute;left:-56px;bottom:46px;background:#FFF1C9;color:var(--ink);padding:14px 20px;border-radius:6px 6px 18px 6px;font-family:var(--hand);font-size:25px;line-height:1.1;transform:rotate(-4deg);box-shadow:0 18px 30px -16px rgba(0,0,0,.5);}
.tag b{color:var(--ember-ink);font-weight:700;}
.h2o-s{list-style:none;margin:0;padding:26px 0 34px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;border-top:1.5px dashed rgba(255,255,255,.22);}
.h2o-s li{display:flex;flex-direction:column;gap:4px;}
.h2o-s b{font-family:var(--display);font-weight:400;font-size:clamp(30px,3.4vw,42px);line-height:1;color:#FFCFA3;}
.h2o-s span{font-size:14.5px;color:var(--on-pine-soft);font-weight:700;}
/* moment: chat bubbles */
.mo{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:56px;align-items:start;}
.mo-me{display:flex;align-items:center;gap:14px;margin-top:26px;font-family:var(--hand);font-size:23px;line-height:1.15;color:var(--pine);}
.mo-me img{width:56px;height:56px;border-radius:50%;object-fit:cover;flex:none;}
.chatlist{display:flex;flex-direction:column;gap:14px;}
.bub{margin:0;max-width:88%;padding:16px 20px;background:var(--peach);border-radius:22px 22px 22px 6px;font-size:16.5px;line-height:1.45;color:var(--ink);box-shadow:0 10px 22px -18px rgba(29,42,40,.6);}
.bub.r{align-self:flex-end;background:var(--mint);border-radius:22px 22px 6px 22px;color:var(--pine);}
/* audit: split card with steps */
.aud{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:40px;align-items:center;background:#fff;border-radius:34px;padding:clamp(28px,4vw,52px);box-shadow:0 30px 60px -40px rgba(8,80,85,.6);}
.aud-t .btn{margin-top:22px;}
.aud-s{list-style:none;margin:0;padding:0;display:grid;gap:14px;counter-reset:a;}
.aud-s li{display:flex;gap:16px;align-items:flex-start;padding:18px 20px;border-radius:20px;background:var(--peach);}
.aud-s li:nth-child(2){background:#FFF1C9;} .aud-s li:nth-child(3){background:var(--peach2);}
.aud-s li > span{flex:none;display:grid;place-items:center;width:40px;height:40px;border-radius:50%;background:var(--ember);color:#fff;font-family:var(--display);font-size:20px;}
.aud-s b{display:block;font-family:var(--display);font-weight:400;font-size:22px;color:var(--ink);}
.aud-s div{font-size:15px;color:var(--muted);line-height:1.4;}
/* formations: the equation */
.eq{display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr) auto minmax(0,1.25fr);gap:14px;align-items:center;margin-top:40px;}
.eq-op{align-self:center;display:grid;place-items:center;width:50px;height:50px;border-radius:50%;background:var(--mint);color:var(--pine);font-family:var(--display);font-size:30px;}
.trk{display:flex;flex-direction:column;gap:10px;padding:26px 22px;border-radius:26px;background:var(--paper);border:2px solid var(--line);}
.trk-k{font-size:12.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--teal);}
.trk h3{font-family:var(--display);font-weight:400;font-size:26px;line-height:1.1;margin:0;}
.trk p{margin:0;color:var(--muted);font-size:15.5px;line-height:1.45;}
.trk ul{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:8px;}
.trk li{display:flex;gap:9px;align-items:flex-start;font-size:15px;line-height:1.35;}
.trk li svg{flex:none;width:18px;height:18px;margin-top:1px;} .trk circle{fill:var(--teal);} .trk path{fill:none;stroke:#fff;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;}
.trk-p{margin-top:auto;padding-top:12px;display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;}
.trk-p b{font-family:var(--display);font-weight:400;font-size:34px;color:var(--ink);}
.trk-p span{font-size:13.5px;color:var(--muted);}
.trk.big{background:var(--pine);border-color:var(--pine);color:#fff;padding:30px 28px;box-shadow:0 30px 50px -30px rgba(8,80,85,.9);}
.trk.big .trk-k{color:var(--ember);} .trk.big h3{font-size:32px;color:#fff;} .trk.big p,.trk.big .trk-p span{color:var(--on-pine-soft);}
.trk.big li{color:#fff;} .trk.big circle{fill:var(--ember);} .trk.big .trk-p b{color:#FFCFA3;}
.trk.big .res{margin-top:8px;font-family:var(--hand);font-size:23px;line-height:1.2;color:#fff;} .trk.big .res b{color:#FFCFA3;font-weight:700;}
.trk.big .btn{margin-top:14px;background:var(--ember);color:#2B1304;border-color:#E27A33;justify-content:center;}
.trk-w{font-weight:800;color:var(--pine)!important;}
.trk.big .trk-w{color:#fff!important;}
.trk-pr{font-family:var(--hand);font-size:21px!important;line-height:1.2!important;color:var(--ember-ink)!important;margin-top:4px!important;}
.trk.big .trk-pr{color:#FFCFA3!important;}
.fm-quote{margin:40px auto 0;text-align:center;font-family:var(--hand);font-weight:700;font-size:clamp(28px,3.2vw,38px);color:var(--pine);transform:rotate(-1.5deg);}
.ab-role{font-weight:800;color:var(--pine);margin:-6px 0 18px;}
.ab-sign{font-family:var(--hand);font-size:clamp(24px,2.6vw,30px);line-height:1.2;color:var(--pine);margin:6px 0 0!important;}
.ab-why{margin-top:30px;padding:26px 28px;border-radius:26px;background:var(--peach);}
.ab-why .ab-big{margin:6px 0 14px;font-size:clamp(24px,2.8vw,32px);}
.ab-why p{color:var(--ink);margin:0 0 12px;} .ab-why p:last-child{margin-bottom:0;}
.ab-v{align-self:start;position:sticky;top:110px;}
.ab-v .ab-c{flex-direction:column;align-items:flex-start;margin-top:18px;}
.nl-k{font-weight:800;color:var(--pine);margin-bottom:6px!important;}
.nl-h{font-family:var(--hand);font-size:23px;line-height:1.2;color:var(--ember-ink)!important;}
footer .wrap > span{line-height:1.6;}
footer .flg a{font-weight:600;text-decoration:underline;text-decoration-color:rgba(8,80,85,.25);text-underline-offset:3px;}
footer .flg a:hover,footer .flg a[aria-current]{color:var(--pine);text-decoration-color:currentColor;}
footer nav{align-items:center;}
footer .fso{display:inline-flex;gap:10px;}
footer .fso a{display:grid;place-items:center;width:38px;height:38px;border-radius:12px;background:var(--mint);color:var(--teal);transition:background .15s,color .15s;}
footer .fso a:hover{background:var(--teal);color:#fff;}
footer .fso a:focus-visible{outline:3px solid var(--ember);outline-offset:2px;}
footer .fso svg{width:20px;height:20px;}
/* header: Winter Pack button */
.top .nav .btn.wpnav{background:var(--pine);color:#fff;border:2px solid var(--pine);box-shadow:0 12px 22px -14px rgba(8,80,85,.9);padding:9px 18px;font-size:14.5px;gap:6px;}
.top .nav .btn.wpnav:hover{background:var(--teal);border-color:var(--teal);color:#fff;}
.top .nav .btn.wpnav span{font-size:15px;line-height:1;}
.top .nav .btn.wpnav:focus-visible{outline:3px solid var(--ember);outline-offset:3px;}
@media (max-width:640px){.top .wrap{gap:10px;} .top .nav{gap:8px;} .top .nav .btn.wpnav,.hx .nav .rdvbtn{padding:8px 12px;font-size:13px;white-space:nowrap;} .logo{height:28px;}}
@media (max-width:370px){.top .nav .btn.wpnav span{display:none;} .top .nav .btn.wpnav,.hx .nav .rdvbtn{padding:8px 10px;}}
/* home: Winter Pack section */
.wpk{position:relative;overflow:hidden;background:linear-gradient(180deg,#E4F5F6 0%,#F4FBFB 100%);}
.wpk-fl{position:absolute;inset:0;pointer-events:none;}
.wpk-fl i{position:absolute;font-style:normal;line-height:1;color:var(--teal);opacity:.22;}
.wpk-g{position:relative;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(36px,5vw,72px);align-items:center;}
.wpk .h2{margin-bottom:16px;}
.wpk .h2 span{display:block;font-family:var(--hand);font-weight:700;font-size:.62em;line-height:1.1;color:var(--ember-ink);margin-top:4px;}
.wpk-l{list-style:none;margin:6px 0 24px;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:9px 18px;}
.wpk-l li{display:flex;align-items:flex-start;gap:9px;font-size:15.5px;line-height:1.35;color:var(--ink);}
.wpk-l svg{flex:none;width:19px;height:19px;margin-top:1px;}
.wpk-l circle{fill:var(--teal);} .wpk-l path{fill:none;stroke:#fff;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;}
.wpk-o{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-bottom:18px;}
.wpk-c{display:flex;flex-direction:column;gap:2px;padding:16px 18px;border-radius:20px;background:#fff;border:2px solid #CDE9EB;text-decoration:none;color:var(--ink);transition:border-color .15s,transform .2s;}
.wpk-c:hover{border-color:var(--teal);transform:translateY(-2px);}
.wpk-c:focus-visible{outline:3px solid var(--ember);outline-offset:3px;}
.wpk-c small{font-size:12.5px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);}
.wpk-c b{font-family:var(--display);font-weight:400;font-size:21px;color:var(--pine);}
.wpk-c span{font-weight:800;font-size:18px;color:var(--ember-ink);}
.wpk-gift{display:flex;align-items:flex-start;gap:10px;margin:0 0 24px;padding:12px 16px;border-radius:16px;background:#FFF4EE;border:2px dashed var(--ember);font-size:15px;line-height:1.45;color:var(--ink);}
.wpk-gift b{color:var(--ember-ink);}
.wpk-v{position:relative;min-height:440px;}
.wpk-d{position:absolute;width:min(62%,300px);height:auto;border-radius:14px;border:6px solid #fff;box-shadow:0 30px 50px -30px rgba(8,80,85,.75);}
.wpk-d.d1{left:2%;top:10%;transform:rotate(-8deg);}
.wpk-d.d2{right:2%;top:6%;transform:rotate(7deg);}
.wpk-d.d3{left:50%;top:0;transform:translateX(-50%) rotate(-1deg);z-index:2;}
.wpk-st{position:absolute;z-index:3;right:2%;bottom:6%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;width:146px;height:146px;padding:16px;border-radius:50%;background:var(--pine);color:#fff;font-weight:800;font-size:13.5px;line-height:1.25;transform:rotate(8deg);box-shadow:0 18px 30px -16px rgba(8,40,43,.8);}
.wpk-st b{display:block;font-family:var(--display);font-weight:400;font-size:44px;line-height:1;color:var(--ember);}
@media (max-width:1020px){.wpk-g{grid-template-columns:1fr;} .wpk-v{order:-1;min-height:0;height:min(92vw,400px);max-width:480px;width:100%;margin-inline:auto;}}
@media (max-width:560px){.wpk-l{grid-template-columns:1fr;} .wpk-o{gap:10px;} .wpk-c{padding:14px;} .wpk-c small{font-size:11px;} .wpk-c b{font-size:17px;line-height:1.2;} .wpk-c span{font-size:16px;} .wpk .btn.rdvbtn{width:100%;justify-content:center;} .wpk-st{width:112px;height:112px;padding:12px;font-size:11.5px;} .wpk-st b{font-size:34px;}}
@media (prefers-reduced-motion:reduce){.wpk-c{transition:none;}}
/* home: social section */
.soc{background:var(--paper);}
.soc .wrap{padding-block:clamp(56px,6vw,84px);}
.soc-h{text-align:center;display:flex;flex-direction:column;align-items:center;margin-bottom:30px;}
.soc-h .h2{margin:6px 0 0;font-size:clamp(28px,3.2vw,38px);max-width:none;}
.soc-g{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;max-width:900px;margin-inline:auto;}
.soc-c{display:grid;grid-template-columns:64px minmax(0,1fr);grid-template-rows:auto auto;gap:6px 18px;align-items:center;padding:22px 24px;border-radius:26px;background:#fff;border:2px solid var(--line);text-decoration:none;color:var(--ink);box-shadow:0 22px 40px -34px rgba(8,80,85,.6);transition:transform .2s,border-color .2s,box-shadow .2s;}
.soc-c:hover{transform:translateY(-4px);border-color:#CDE9EB;box-shadow:0 26px 44px -30px rgba(8,80,85,.6);}
.soc-c:focus-visible{outline:3px solid var(--ember);outline-offset:4px;}
.soc-l{grid-row:span 2;display:block;width:64px;height:64px;}
.soc-l svg{display:block;width:100%;height:100%;}
.soc-t{display:flex;flex-direction:column;gap:2px;min-width:0;}
.soc-t small{font-size:12.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);}
.soc-t b{font-family:var(--display);font-weight:400;font-size:21px;line-height:1.2;color:var(--pine);overflow-wrap:anywhere;}
.soc-t b.soc-hd{font-size:18px;overflow-wrap:normal;}
.soc-t > span{font-size:15px;line-height:1.45;color:var(--muted);}
.soc-a{font-weight:800;font-size:15px;color:var(--ember-ink);}
.soc-a span{display:inline-block;transition:translate .2s;} .soc-c:hover .soc-a span{translate:4px 0;}
@media (max-width:760px){.soc-g{grid-template-columns:1fr;max-width:520px;}}
@media (max-width:420px){.soc-c{grid-template-columns:52px minmax(0,1fr);padding:18px;gap:6px 14px;} .soc-l{width:52px;height:52px;} .soc-t b{font-size:18px;} .soc-t b.soc-hd{font-size:16px;}}
@media (prefers-reduced-motion:reduce){.soc-c,.soc-a span{transition:none;}}


.eq-more{margin-top:26px;text-align:center;color:var(--muted);font-size:15px;}
.eq-more a{font-weight:800;color:var(--pine);}
/* programme: numbered tiles + kit */
.mods{list-style:none;margin:36px 0 0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;}
.mods li{display:flex;flex-direction:column;gap:4px;padding:22px 22px 20px;border-radius:22px;background:#fff;}
.mods .mn{font-family:var(--display);font-size:38px;line-height:1;color:var(--ember);}
.mods b{font-family:var(--display);font-weight:400;font-size:21px;margin-top:8px;}
.mods li > span:last-child{font-family:var(--hand);font-size:23px;line-height:1.15;color:var(--teal);margin-top:4px;}
.kit{margin-top:30px;display:flex;flex-wrap:wrap;align-items:center;gap:12px 18px;}
.kit p{margin:0;color:var(--ink);}
.kit ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:8px;}
.kit li{background:var(--pine);color:#fff;border-radius:999px;padding:7px 14px;font-size:14px;font-weight:700;}
/* about */
.ab{display:grid;grid-template-columns:minmax(0,.7fr) minmax(0,1.3fr);gap:60px;align-items:start;}
.ab-v img{display:block;width:100%;max-width:320px;aspect-ratio:420/540;border-radius:32px;object-fit:cover;transform:rotate(-3deg);box-shadow:0 30px 50px -30px rgba(8,80,85,.7);}
.ab-n{margin:22px 0 0;display:flex;flex-direction:column;font-size:14.5px;color:var(--muted);max-width:300px;}
.ab-n b{font-family:var(--display);font-weight:400;font-size:24px;color:var(--ink);}
.ab-big{font-family:var(--display);font-size:clamp(28px,3.4vw,40px);line-height:1.15;color:var(--pine);margin:8px 0 20px;}
.ab-t > p{color:var(--ink);max-width:62ch;margin:0 0 14px;}
.ab-c{list-style:none;margin:22px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:10px;}
.ab-c li{background:var(--mint);border-radius:999px;padding:9px 16px;font-size:14px;font-weight:700;}
.ab-c b{font-family:var(--display);font-weight:400;font-size:19px;color:var(--pine);margin-right:6px;}
/* testimonials: scroll row */
 .tm-h{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:16px;}
 .tm-h .sp-google.big{margin:0;}
 .tms{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(290px,1fr);gap:18px;margin-top:34px;overflow-x:auto;scroll-snap-type:x mandatory;padding:6px 4px 22px;}
.tm{scroll-snap-align:start;margin:0;display:flex;flex-direction:column;gap:14px;padding:26px 24px 22px;border-radius:26px;background:#fff;box-shadow:0 18px 36px -28px rgba(8,80,85,.7);}
.tm-q{font-family:var(--display);font-size:70px;line-height:.6;color:var(--ember);height:30px;}
.tm blockquote{margin:0;font-size:15.5px;line-height:1.55;color:var(--ink);}
.tm figcaption{margin-top:auto;display:flex;align-items:center;gap:12px;font-size:13.5px;color:var(--muted);}
.tm figcaption b{display:block;color:var(--ink);font-size:15px;}
.tm-i{flex:none;display:grid;place-items:center;width:42px;height:42px;border-radius:50%;background:var(--peach2);color:var(--ember-ink);font-family:var(--display);font-size:16px;}
.tm-g{display:flex;align-items:center;gap:7px;font-size:12.5px;font-weight:800;color:#3c4043;}
.tm-g .sp-g{width:16px;height:16px;}
.tm-hint{margin:4px 0 0;font-family:var(--hand);font-size:22px;color:var(--pine);text-align:right;}
/* newsletter: peach card */
.nl{display:grid;grid-template-columns:auto minmax(0,1fr);gap:clamp(24px,5vw,60px);align-items:center;background:var(--peach2);border-radius:34px;padding:clamp(26px,4vw,50px);}
.nl img{width:clamp(140px,18vw,210px);height:auto;transform:rotate(-6deg);}
.nl h2{font-family:var(--display);font-weight:400;font-size:clamp(30px,4vw,46px);line-height:1.08;margin:6px 0 12px;}
.nl p{margin:0 0 12px;color:var(--ink);max-width:56ch;}
.nl-s b{font-family:var(--display);font-weight:400;font-size:30px;color:var(--ember-ink);margin-right:4px;}
.nl .btn{margin-top:8px;}
/* blog: editorial list */
.bl{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:56px;align-items:start;}
.bl .btn{margin-top:20px;}
.bl-l{list-style:none;margin:0;padding:0;border-top:2px solid var(--ink);}
.bl-l a{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:18px;align-items:center;padding:20px 4px;border-bottom:1.5px solid var(--line);text-decoration:none;color:var(--ink);}
.bl-l a:hover .bt{color:var(--teal);} .bl-l a:hover .ba{transform:translateX(4px);}
.bn{font-family:var(--hand);font-weight:700;font-size:26px;color:var(--ember-ink);}
.bt{font-family:var(--display);font-size:clamp(19px,2vw,23px);line-height:1.2;transition:color .2s;}
.ba{font-size:20px;color:var(--pine);transition:transform .2s;}
/* blog: picture cards */
.bg-h{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:20px 40px;}
.bg-h .sub{margin-bottom:0;}
.posts2{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;margin-top:52px;}
.pc2{display:flex;flex-direction:column;text-decoration:none;color:var(--ink);background:#fff;border-radius:24px;overflow:hidden;box-shadow:0 22px 40px -30px rgba(8,80,85,.7);transition:transform .25s,box-shadow .25s;}
.pc2:hover{transform:translateY(-6px);box-shadow:0 30px 50px -30px rgba(8,80,85,.8);}
.pc2-i{display:block;aspect-ratio:4/3;overflow:hidden;background:var(--mint);}
.pc2-i img{display:block;width:100%;height:100%;object-fit:cover;transition:transform .4s;}
.pc2:hover .pc2-i img{transform:scale(1.05);}
.pc2-t{display:flex;flex-direction:column;gap:10px;padding:22px 22px 24px;flex:1;}
.pc2-k{font-family:var(--hand);font-weight:700;font-size:21px;line-height:1;color:var(--ember-ink);}
.pc2-h{font-family:var(--display);font-size:20px;line-height:1.25;}
.pc2-m{margin-top:auto;padding-top:6px;font-weight:800;font-size:14px;color:var(--pine);}
.pc2:focus-visible{outline:3px solid var(--ember);outline-offset:4px;}
@media (max-width:1020px){.posts2{grid-template-columns:repeat(2,minmax(0,1fr));}}
@media (max-width:560px){.posts2{grid-template-columns:1fr;gap:20px;}}
@media (prefers-reduced-motion:reduce){.pc2,.pc2-i img{transition:none;}}
/* audit card: title on top, steps in a row, text + button below */
.aud{display:block!important;}
.aud .aud-h{max-width:24ch;margin-bottom:34px;}
.aud-s{grid-template-columns:repeat(3,minmax(0,1fr));align-items:stretch;}
.aud-s li{flex-direction:column;gap:14px;}
.aud-f{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:20px 40px;margin-top:34px;padding-top:30px;border-top:1.5px dashed rgba(8,80,85,.18);}
.aud-f .sub{margin:0!important;max-width:58ch;}
.aud-f .btn{margin:0!important;}
.aud-dark .aud-f{border-top-color:rgba(255,255,255,.22);}
/* audit: the two real options */
.aud-o{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;}
.ao{display:flex;flex-direction:column;gap:8px;padding:26px 26px 24px;border-radius:24px;text-decoration:none;color:var(--ink);border-left:6px solid var(--ember);background:var(--peach);transition:transform .2s,box-shadow .2s;}
.ao.co{border-left-color:var(--teal);background:var(--mint);}
.ao:hover{transform:translateY(-4px);box-shadow:0 22px 36px -28px rgba(8,80,85,.7);}
.ao:focus-visible{outline:3px solid var(--ember);outline-offset:4px;}
.ao-i{font-size:24px;line-height:1;color:var(--ember);} .ao.co .ao-i{color:var(--teal);}
.ao-k{font-size:12.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--ember-ink);} .ao.co .ao-k{color:var(--teal);}
.ao b{font-family:var(--display);font-weight:400;font-size:26px;line-height:1.15;color:var(--ink);}
.ao-t{font-size:15.5px;line-height:1.55;color:var(--muted);} .ao-t strong{color:var(--ink);}
.ao-c{margin-top:auto;padding-top:8px;font-weight:800;color:var(--ember-ink);} .ao.co .ao-c{color:var(--pine);}
.aud-n{margin:28px 0 0;padding-top:24px;border-top:1.5px dashed rgba(8,80,85,.18);font-size:17px;line-height:1.6;color:var(--muted);} .aud-n b{color:var(--pine);}
.aud-dark .aud-n{color:var(--on-pine-soft);border-top-color:rgba(255,255,255,.22);} .aud-dark .aud-n b{color:#fff;}
@media (max-width:760px){.aud-o{grid-template-columns:1fr;}}
@media (prefers-reduced-motion:reduce){.ao{transition:none;}}
/* formations equation: the two parcours side by side, "=" then the complete one across */
.eq{grid-template-columns:minmax(0,1fr) auto minmax(0,1fr)!important;align-items:stretch!important;}
.eq-eq{grid-column:1/-1;justify-self:center;}
.trk.big{grid-column:1/-1;display:grid!important;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:20px 56px;padding:44px 48px!important;}
.bg-a,.bg-b{display:flex;flex-direction:column;gap:14px;}
.bg-b ul{margin-top:0!important;}
.trk.big .bg-b .btn{align-self:flex-start;}
.trk.big h3{font-size:clamp(32px,3.4vw,42px)!important;}
/* kit du manager */
.kit2{margin-top:56px;display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:40px 56px;align-items:center;padding:clamp(32px,5vw,60px);border-radius:34px;background:var(--pine);color:#fff;box-shadow:0 34px 60px -40px rgba(8,80,85,.9);position:relative;overflow:hidden;}
.kit2::after{content:"";position:absolute;right:-90px;bottom:-110px;width:280px;height:280px;border-radius:50%;background:rgba(255,255,255,.05);pointer-events:none;}
.kit2 .hand{color:var(--ember);font-size:30px;}
.kit2 h3{font-family:var(--display);font-weight:400;font-size:clamp(28px,3.2vw,40px);line-height:1.12;margin:8px 0 16px;color:#fff;}
.kit2 h3 em{font-style:normal;color:#FFCFA3;}
.kit2-h p{margin:0;color:var(--on-pine-soft);font-size:17px;line-height:1.6;max-width:44ch;}
.kit2-l{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;position:relative;z-index:1;}
.kit2-l li{display:flex;align-items:center;gap:14px;padding:16px 18px;border-radius:20px;background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.12);}
.kit2-l .ki{flex:none;display:grid;place-items:center;width:46px;height:46px;border-radius:14px;background:var(--ember);color:#2B1304;}
.kit2-l .ki svg{width:24px;height:24px;}
.kit2-l b{display:block;font-size:16px;font-weight:800;color:#fff;line-height:1.3;}
.kit2-l small{display:block;font-size:13px;color:var(--on-pine-soft);margin-top:2px;line-height:1.35;}
@media (max-width:1020px){.kit2{grid-template-columns:1fr;}}
@media (max-width:520px){.kit2-l{grid-template-columns:1fr;}}
/* about: intro row + full-width "why" band */
#elodie .ab{align-items:center!important;}
#elodie .ab-v{position:static!important;align-self:center!important;}
#elodie .ab-v img{max-width:340px;}
#elodie .ab-sign{line-height:1.25!important;margin-top:22px!important;}
#elodie .ab-c{flex-direction:row!important;flex-wrap:wrap;margin:0 0 26px!important;}
.why2{margin-top:clamp(56px,7vw,90px);display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:28px 64px;align-items:center;padding:clamp(32px,5vw,60px);border-radius:34px;background:var(--peach);border-left:8px solid var(--ember);}
.why2-q{position:relative;margin:10px 0 0;padding-left:44px;font-family:var(--display);font-size:clamp(28px,3.2vw,40px);line-height:1.15;color:var(--pine);}
.why2-q span{position:absolute;left:0;top:-8px;font-size:76px;line-height:1;color:var(--ember);}
.why2-b p{margin:0 0 16px;color:var(--ink);line-height:1.7;}
.why2-b p:last-child{margin-bottom:0;}
@media (max-width:1020px){.why2{grid-template-columns:1fr;} #elodie .ab-v{justify-self:center;text-align:center;} #elodie .ab-v img{margin-inline:auto;} #elodie .ab-n{margin-inline:auto;}}
/* titles: fewer lines */
main .room .h2{max-width:28ch;}
.pg-h{text-align:center;display:flex;flex-direction:column;align-items:center;}
.pg-h .h2{max-width:none;font-size:clamp(30px,3.6vw,46px);}
.pg-h .sub{max-width:62ch;margin-inline:auto;}
@media (max-width:560px){main .room .h2{font-size:30px;line-height:1.12;} .aud .aud-h{font-size:25px;} .pg-h .h2{font-size:25px;}}
/* pourquoi je peux te former */
.ab-why{border-left:6px solid var(--ember);}
.ab-why .ab-big{position:relative;line-height:1.2!important;margin:10px 0 18px!important;padding-left:38px;font-size:clamp(24px,2.6vw,30px);}
.ab-why .ab-big span{position:absolute;left:0;top:-6px;font-size:64px;line-height:1;color:var(--ember);}
/* final: orange */
.fin2{background:var(--ember);color:#2B1304;text-align:center;}
.fin2 .wrap{padding-block:clamp(56px,7vw,90px);max-width:860px;}
.fin2 .hand{color:#fff;font-size:30px;}
.fin2 h2{font-family:var(--display);font-weight:400;font-size:clamp(34px,4.6vw,56px);line-height:1.06;margin:8px 0 16px;}
.fin2 p{margin:0 auto 8px;max-width:60ch;font-size:18px;}
.fin2-k{font-family:var(--hand);font-size:26px;font-weight:700;}
.fin2 .btn.rdvbtn{margin-top:22px;background:var(--pine);color:#fff;border-color:var(--pine);box-shadow:0 18px 30px -16px rgba(8,40,43,.8);}
.fin2 .btn.rdvbtn:hover{background:#0a6166;color:#fff;}
/* more air between and inside sections */
main > .room{padding-block:clamp(96px,11vw,150px);}
main .room .h2{margin:10px 0 24px;}
main .room .sub{margin:0 0 14px;line-height:1.65;}
main .room .hand{margin-bottom:18px;}
.h2o > .wrap:first-child{padding-block:96px 56px;gap:72px;}
.h2o .lede{margin-bottom:6px;} .h2o .ctas{margin-top:38px;}
.h2o-s{padding:40px 0 52px;gap:24px;}
.sp-band{padding:28px 0;}
.mo{gap:80px;} .chatlist{gap:20px;} .bub{padding:20px 24px;}
.aud{gap:64px;padding:clamp(36px,5vw,68px);} .aud-s{gap:18px;} .aud-s li{padding:22px 24px;} .aud-t .btn{margin-top:30px;}
.eq{margin-top:64px;gap:20px;} .trk{padding:32px 26px;gap:14px;} .trk.big{padding:38px 32px;} .trk ul{gap:10px;margin-top:10px;}
.eq-more{margin-top:40px;} .fm-quote{margin-top:56px;}
.mods{margin-top:56px;gap:22px;} .mods li{padding:28px 26px 26px;} .kit{margin-top:44px;gap:16px 22px;}
.ab{gap:88px;} .ab-t > p{margin:0 0 20px;line-height:1.7;} .ab-role{margin:-4px 0 26px;} .ab-sign{margin-top:14px!important;}
.ab-why{margin-top:48px;padding:34px 36px;} .ab-why p{margin:0 0 16px;line-height:1.7;}
.ab-v .ab-c{margin-top:26px;gap:12px;}
.tm-h{gap:24px;} .tms{margin-top:48px;gap:24px;} .tm{padding:32px 28px 26px;gap:18px;} .tm-hint{margin-top:14px;}
.nl{padding:clamp(36px,5vw,72px);gap:clamp(32px,6vw,80px);} .nl p{margin:0 0 16px;line-height:1.65;} .nl h2{margin:8px 0 18px;} .nl .btn{margin-top:14px;}
.bl{gap:80px;} .bl .btn{margin-top:30px;} .bl-l a{padding:26px 6px;}
.fin2 .wrap{padding-block:clamp(80px,10vw,130px);} .fin2 h2{margin:12px 0 22px;} .fin2 p{margin-bottom:12px;} .fin2 .btn.rdvbtn{margin-top:32px;}
#blog{background:var(--peach);}
footer .wrap{padding-block:40px;}
@media (max-width:1020px){
  main > .room{padding-block:clamp(72px,14vw,100px);}
  .h2o > .wrap:first-child{padding-block:64px 40px;gap:48px;}
  .mo,.ab,.bl{gap:48px;} .aud{gap:40px;} .eq{gap:16px;}
}
@media (max-width:1020px){
  .h2o > .wrap:first-child,.mo,.aud,.ab,.bl{grid-template-columns:1fr;} .ab-v{position:static;}
  .h2o-v{width:min(100%,320px);} .tag{left:-20px;}
  .eq{grid-template-columns:1fr!important;max-width:560px;margin-inline:auto;} .eq-op{justify-self:center;}
  .trk.big{grid-template-columns:1fr;padding:32px 26px!important;} .aud-s{grid-template-columns:1fr;}
  .mods{grid-template-columns:repeat(2,minmax(0,1fr));}
  .h2o-s{grid-template-columns:repeat(2,minmax(0,1fr));}
}
@media (max-width:560px){
  .mods{grid-template-columns:1fr;} .nl{grid-template-columns:1fr;} .bub{max-width:96%;}
  .hx .nav .rdvbtn{padding:9px 16px;font-size:14px;}
}
</style>
'''
html = head + CSS + BODY + defs
open(S + 'home/accueil-test-v2.html', 'w', encoding='utf-8').write(html)
print(len(html))
