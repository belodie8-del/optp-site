BODY_A = '''<header class="top hx"><div class="wrap">
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

<section class="fin2"><div class="wrap">
  <span class="hand">Travaillons ensemble</span>
  <h2>Ose prendre ta place de manager et libère ton potentiel !</h2>
  <p>30 minutes pour faire le point sur ta situation managériale : on identifie ce qui bloque vraiment, je te donne mon analyse directe, et on voit ensemble quelle formule peut t’aider à avancer.</p>
  <p class="fin2-k">Pas de pression. Juste de l’efficacité !</p>
  <a class="btn rdvbtn big" href="''' + RDV + '''" target="_blank" rel="noopener">Je prends RDV avec Élodie ''' + ARR + '''</a>
</div></section>
</main>
<footer><div class="wrap"><span><b>Élodie Boyer</b> · Formatrice en management passionnée qui aide les managers à réaliser leur plein potentiel<br>© 2026 EB Formation Consulting · <span class="flg"><a href="https://www.oseprendretaplace.fr/politique-de-confidentialite">Politique de confidentialité</a> · <a href="https://www.oseprendretaplace.fr/conditions-utilisation">Conditions d’utilisation</a> · <a href="https://www.oseprendretaplace.fr/politique-cookies">Politique de cookies</a></span></span><nav aria-label="Liens"><a href="''' + FORM + '''">Les formations</a><a href="''' + BLOG + '''">Blog</a><a href="''' + CONTACT + '''">Contact</a><span class="fso"><a href="https://www.linkedin.com/in/elodie-boyer-299891143/" target="_blank" rel="noopener" aria-label="LinkedIn · Élodie Boyer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M8 11v5M8 8v.01M12 16v-5M12 13a2 2 0 0 1 4 0v3"/></svg></a><a href="https://www.instagram.com/elodie_boyer_off_management/" target="_blank" rel="noopener" aria-label="Instagram · elodie_boyer_off_management"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5v.01"/></svg></a></span></nav></div></footer>
'''

