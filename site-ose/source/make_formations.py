"""Test: oseprendretaplace.fr/formations rebuilt with the same codes as the new home page (version A).
All the texts of the current page are kept. Not deployed anywhere."""
exec(open('_pre.py', encoding='utf-8').read())
exec(open('_cssA.py', encoding='utf-8').read())
head = head.replace('<title>Ose prendre ta place · Accueil</title>', '<title>Les formations · Ose prendre ta place</title>', 1)

HOME = 'https://www.oseprendretaplace.fr/accueil'
PAY_OSE = 'https://www.oseprendretaplace.fr/paiement-ose'
PAY_BOOSTE = 'https://www.oseprendretaplace.fr/paiement-packbooste'
PAY_INCARNE = 'https://www.oseprendretaplace.fr/paiement-packincarnetaposture'
CROSS = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M8.5 8.5l7 7M15.5 8.5l-7 7"/></svg>'
def ul(items, cls=''): return '<ul class="%s">%s</ul>' % (cls, ''.join('<li>%s<span>%s</span></li>' % (CHK, x) for x in items))

WHY_NOW = ['tu rentres le soir en te demandant <mark>comment tu vas gérer la situation de demain</mark>.',
           'tu cherches des réponses en cachette sur ChatGPT et que tu ne trouves jamais la bonne, juste <mark>des réponses génériques qui ne connaissent ni ton équipe, ni ton contexte</mark>.',
           't’en as marre de <mark>faire semblant de ne pas entendre</mark> ou de ne pas comprendre ce qu’il se passe, parce que tu ne sais pas comment le gérer.',
           'tu <mark>rejoues la scène de la réunion dans ta tête</mark>, en te disant que t’aurais dû dire autrement.',
           'tu as <mark>peur de dire à ton N+1 que tu n’y arrives pas</mark>, puisque si on t’a mis à ce poste, c’est qu’on te sentait capable.']
FOR_YES = ['Tu es manager, que tu viennes d’être nommé(e) ou que tu le sois depuis un moment, et personne ne t’a vraiment expliqué comment faire',
           'Tu es doué(e) dans ton métier, et c’est justement pour ça qu’on t’a mis à ce poste',
           'Tu es prêt(e) à ce que ça bouge en 12 semaines, pas dans deux ans',
           'Tu veux que je fasse avec toi, pas juste des vidéos à regarder seul']
FOR_NO = ['Tu n’as pas d’équipe à manager', 'Tu veux une solution miracle sans rien changer à ta façon de faire',
          'Tu n’es pas prêt(e) à remettre en question tes pratiques',
          'Tu as tendance à te déresponsabiliser (c’est toujours la faute de l’équipe, du contexte, de la direction, jamais la tienne)']
KIT_LINE = 'Le kit complet du manager (vidéos, workbooks, fiches outils, feuilles de route Notion, challenges, quiz…)'
OSE_ITEMS = ['Tous les modules !', '6 séances de coaching individuel en OTO avec Élodie', KIT_LINE, 'Accès à la plateforme à vie !',
             'Un groupe WhatsApp privé : pour ne jamais être seul face à une situation qui ne peut pas attendre.',
             'Des lives exclusifs pour la communauté, sur des sujets managériaux concrets (réservés uniquement aux managers qui suivent « Ose Prendre Ta Place »)']
MODS = [
 ('RESET', 'Arrête de deviner ce qu’on attend de toi', 'Ce module pose une bonne fois pour toutes ce qu’on attend vraiment de toi maintenant que t’as ce titre, pour que t’arrêtes de deviner.',
  ['Diagnostiquer ta posture actuelle grâce à un quiz', 'Repérer lesquelles de tes croyances sur le management sont fausses (et lesquelles sont justes) via un test',
   'Poser clairement le cadre de ta mutation d’expert à manager', 'Créer ton « nouveau contrat » : ce qu’on attend vraiment de toi, écrit noir sur blanc'],
  'Tu vas suivre : Le Mémo des Premières Semaines (podcast + repères pratiques)'),
 ('La Lecture d’Équipe', 'Arrête de manager tout le monde pareil', 'Ce module t’apprend à repérer ce qui fait avancer chaque personne de ton équipe, pour arrêter de manager tout le monde avec le même mode d’emploi.',
  ['Adapter ta posture selon la personne que tu as en face de toi grâce aux 4 postures (architecte, coach, partenaire, mentor)', 'Scanner rapidement le profil de chaque collaborateur grâce à un outil dédié',
   'Trouver le bon « match » entre ta posture et le profil de chaque collaborateur grâce à une méthode concrète', 'Repérer le piège du statut (croire qu’on a raison parce qu’on est le chef) grâce à un exercice concret',
   'Travailler sur tes propres angles morts de manager'], ''),
 ('Posture & Crédibilité', 'Une autorité naturelle, sans crier', 'Ce module t’apprend à construire une autorité naturelle, respectée, sans avoir besoin de crier ni de jouer un rôle.',
  ['Évaluer ton niveau d’autorité actuel grâce à un diagnostic', 'Construire une autorité naturelle (celle qu’on n’a pas besoin d’imposer) grâce à un cadre concret',
   'Développer une posture managériale solide grâce aux 5 piliers de la posture', 'Renforcer ta crédibilité grâce aux 5 piliers de la crédibilité managériale',
   'Développer ta solidité face à la pression grâce à un travail d’introspection', 'Ancrer durablement tes nouveaux réflexes grâce à un bonus de mise en pratique'], ''),
 ('Courage & Influence', 'Ose dire les choses, et que ça se passe bien', 'Ce module t’apprend à dire les choses au bon moment, à la bonne personne et par le bon canal, pour que ça sorte enfin… et que ça se passe bien.',
  ['Développer ton courage managérial pour oser dire les choses, même celles qui piquent, grâce à un cadre concret',
   'Comprendre pourquoi ton message n’arrive jamais exactement comme tu le souhaites grâce à un travail sur l’illusion de la communication',
   'Choisir le bon canal de communication selon la situation grâce à la stratégie des canaux'], ''),
 ('L’Alliance Individuelle', 'Fais grandir chacun, sans tout porter seul(e)', 'Chaque collaborateur a ses propres moteurs, ses propres freins, ses propres besoins du moment. Ce module te donne les outils pour construire une alliance solide avec chacun et manager avec précision.',
  ['Construire des objectifs que ton collaborateur s’approprie vraiment', 'Maîtriser l’art de la délégation pour te libérer du temps', 'Structurer tes rituels individuels (OTO)',
   'Piloter la performance individuelle de chaque collaborateur', 'Identifier ce qui motive vraiment chaque collaborateur avec la méthode du Portrait Motivationnel',
   'Choisir le bon outil pour désamorcer les tensions et les conflits'], ''),
 ('Le Collectif', 'Une équipe soudée, même quand ça secoue', 'Une équipe, ce n’est pas juste une somme d’individus. C’est un collectif avec ses propres dynamiques, ses tensions, ses rituels. Ce module te donne les outils pour le piloter autrement.',
  ['Choisir le bon format de réunion en fonction des résultats attendus', 'Activer l’intelligence collective de ton équipe pour gagner en performance',
   'Détecter les tensions, gérer les conflits collectifs et reconstruire la cohésion d’équipe après la crise', 'Annoncer une mauvaise nouvelle à ton équipe avec les bons mots',
   'Conduire le changement en engageant ton équipe'], ''),
]
STEPS = [('Contact', 'On s’appelle.', 'Trente minutes, toi et moi. Tu me racontes ce que tu vis. C’est le moment de savoir si on matche.'),
         ('Informations', 'On fait le tour.', 'On regarde ensemble quelle formule peut répondre à ta situation, ton équipe, ce qui ne fonctionne plus, ce que t’as déjà essayé.'),
         ('On se lance ?', 'Tu prends ton temps.', 'Aucune pression. Pas de « c’est maintenant ou jamais ». Tu prends le temps qu’il te faut pour décider.'),
         ('Tu dis OUIIII !', 'Et c’est parti.', 'Tes accès arrivent direct. Les modules, mon agenda, tout est là. Tu bloques ton premier créneau avec moi. Et la première semaine commence.')]
TRIED = ['Tu as demandé une formation à ton employeur, sans réponse concrète', 'Tu t’es noyé(e) dans les livres, podcasts et conseils contradictoires',
         'Tu as tenté des méthodes lues ici ou là, rien ne dure', 'Tu as l’impression de bricoler ton management au jour le jour',
         'Tu n’oses pas en parler à ton N+1 par peur de paraître « pas à la hauteur »', 'Et plus le temps passe, plus tu te sens seul(e) avec tes questions']
WORDS = [('« Sois bienveillant »', 'ok, mais personne t’a dit où s’arrête la bienveillance et où commence le laxisme.'),
         ('« Il faut que tu fasses preuve de leadership »', 'le mot est beau. Le mode d’emploi, lui, n’existe nulle part.'),
         ('« Travaille ta posture »', 'comme si ça s’apprenait en le décidant un matin, entre deux réunions.'),
         ('« Sois courageux »', 'facile à dire, quand c’est pas toi qui dois annoncer la mauvaise nouvelle.')]
BONUS = ['Ta stratégie managériale', 'Ton agenda managérial', 'Ta relation avec ton N+1', 'Comment te protéger']
FAQ = [
 ('C’est pour moi si je suis manager depuis longtemps ?', ['Oui. Que tu viennes d’être nommé ou que tu manages depuis plusieurs années, si tu te sens perdu dans ton management depuis quelque temps et que ce qui fonctionnait avant ne fonctionne plus, c’est exactement pour toi.']),
 ('Je suis manager débutant, est-ce que le programme est fait pour moi ?', ['Oui, c’est même le moment idéal. Poser les bonnes bases maintenant, c’est ce qui t’évite de passer des années à improviser. Tu n’as pas besoin d’expérience pour commencer. Tu as besoin d’un cadre et de quelqu’un pour t’aider à le construire. C’est exactement ce qu’on fait ensemble.']),
 ('Est-ce que ça marche pour mon secteur ?', ['Oui. J’ai accompagné des managers en laboratoire, pharmacie, intérim, coiffure, informatique. Le management pose les mêmes problèmes partout. Ce qui change, c’est ton contexte, et c’est exactement pour ça qu’on travaille sur ta vraie équipe, ton vrai conflit, ta vraie situation, pas sur un cas d’école.']),
 ('Quelle est la différence entre les deux packs et Ose Prendre Ta Place ?', ['<b>La profondeur.</b> Un pack, c’est 3 modules sur un sujet précis. Tu règles un pan de ton management, soit toi, soit ton équipe. Ose Prendre Ta Place, c’est les 6 modules. On ne laisse rien de côté.',
   '<b>Le suivi entre les séances.</b> Avec un pack, tu as tes séances de coaching et le kit manager. Avec Ose Prendre Ta Place, tu n’es jamais seul entre deux séances : le groupe WhatsApp privé, les lives exclusifs, et je corrige tes exercices personnellement.',
   '<b>Ce que tu repars avec.</b> Un pack te donne 3 compétences solides et applicables immédiatement, soit sur toi, soit sur ton équipe. Ose Prendre Ta Place te donne la transformation complète : ta posture, ton équipe, ta stratégie, ta relation avec ta hiérarchie. À la fin, tu ne te demandes plus si tu es fait pour ce poste. Tu le sais.']),
 ('Comment fonctionne un pack ?', ['Tu prends d’abord RDV avec moi pour qu’on analyse ta situation ensemble, je m’assure que c’est le bon moment pour toi et la bonne formule.',
   'Une fois que tu dis oui, tes accès arrivent directement sur la plateforme. Les modules, mon agenda, tout est là.',
   'Le rythme est simple. Semaine 1 : tu suis le module à ton rythme, quand tu veux. Semaine 2 : on se retrouve sur Google Meet pour ta séance de coaching, 1 h avec moi, sur ta vraie situation.',
   'Avant chaque séance, je t’envoie une fiche à remplir pour qu’on rentre directement dans le vif du sujet sans perdre de temps. Tu repars avec un plan d’action concret à appliquer dès le lendemain.',
   '<b>3 modules. 3 séances. 6 semaines.</b> Accès à vie à la plateforme, mises à jour incluses.']),
 ('Comment fonctionne Ose Prendre Ta Place ?', ['Même rythme, même fonctionnement : une semaine le module, une semaine le coaching, sur les 6 modules et 12 semaines au total.',
   'Mais Ose Prendre Ta Place, c’est plus qu’un accompagnement individuel. Entre les séances, tu n’es jamais seul.',
   'Un groupe WhatsApp privé réservé aux managers du programme pour poser tes questions et ne jamais rester bloqué. Des lives exclusifs que j’organise pour la communauté. L’Atelier Stratégie Managériale trimestriel. Et je corrige tes exercices, pas une IA, pas un assistant. Moi.',
   '<b>6 modules. 6 séances. 12 semaines.</b> Accès à vie à la plateforme, mises à jour incluses.']),
 ('Aurais-je accès à toi en live ?', ['Oui, pour toutes les formules. Les packs et Ose Prendre Ta Place incluent des séances de coaching individuel avec moi sur Google Meet. Ose Prendre Ta Place inclut en plus des lives exclusifs réservés aux managers du programme, et le groupe WhatsApp pour ne jamais être seul entre deux séances.']),
 ('Et si je n’ai pas le temps en ce moment ?', ['L’idéal est de suivre un pack sur 6 semaines et Ose Prendre Ta Place sur 12 semaines : c’est le rythme qui permet d’ancrer vraiment les changements dans ton quotidien. Mais le programme prend en compte tes contraintes : si tu as besoin d’étaler un peu plus, on s’adapte.']),
 ('Est-ce que le programme est finançable par le CPF ?', ['Non, le programme n’est pas finançable par le CPF. (J’espère un jour.)']),
 ('Est-ce que je peux payer en plusieurs fois ?', ['Oui. Les packs et Ose Prendre Ta Place sont disponibles en 2 fois.']),
 ('Combien de temps aurais-je accès à la plateforme ?', ['À vie, avec toutes les mises à jour incluses. Si j’améliore un module ou j’ajoute du contenu, tu y as accès automatiquement.']),
 ('Combien de temps je dois consacrer par semaine ?', ['Compte environ 30 minutes par jour. Une semaine tu suis le module à ton rythme, la semaine suivante tu as ta séance de coaching avec moi. C’est conçu pour s’intégrer dans ton quotidien de manager en activité, pas pour te rajouter une charge de travail.']),
 ('Et si ça ne correspond pas à ce que j’attendais ?', ['C’est exactement pour ça qu’on commence par un appel de 30 minutes, pour qu’on vérifie ensemble avant que tu t’engages. Si ce n’est pas le bon moment ou la bonne formule pour toi, je te le dirai.']),
]

def mod_card(i, m):
    name, tag, desc, items, extra = m
    grp = 'a' if i < 3 else 'b'
    return ('<article class="md g%s"><div class="md-top"><div class="md-h"><span class="md-n">%02d</span><div><span class="md-k">Module %d</span><h3>%s</h3><p class="md-t">%s</p></div></div>'
            '<p class="md-d">%s</p></div><details class="md-dt"><summary><span>Ce que tu vas travailler</span><span class="md-c">%d</span>'
            '<svg class="md-chv" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></summary>%s%s</details></article>') % (
            grp, i + 1, i + 1, name, tag, desc, len(items), ul(items, 'md-l'), ('<p class="md-x">%s</p>' % extra) if extra else '')
def pack(name, line, mods, price, pay):
    return ('<article class="pk"><span class="trk-k">3 modules</span><h3>%s</h3><p class="pk-w">%s</p>%s'
            '<p class="pk-bn">🎁 Bonus inclus : l’Atelier Stratégie Managériale trimestriel, Manager, mais pour toi aussi.</p>'
            '<div class="pk-f"><b>%s</b><a class="btn soft" href="%s">Je me lance !</a></div></article>') % (
        name, line, ul(['Accès aux 3 modules : ' + mods, '3 séances de coaching individuel en OTO avec Élodie', KIT_LINE, 'Accès à la plateforme à vie !'], 'pk-l'), price, pay)
def kit_html():
    return ('<div class="kit2"><div class="kit2-h"><span class="hand">Le Kit du Manager</span><h3>Pas seulement des vidéos. <em>Une vraie boîte à outils.</em></h3>'
            '<p>Des outils pour que la méthode ne reste pas dans ta tête, mais pour l’intégrer complètement à ton quotidien. Inclus dans chaque module :</p></div>'
            '<ul class="kit2-l">%s</ul></div>') % ''.join('<li><span class="ki">%s</span><span><b>%s</b>%s</span></li>' % (
                KIT_ICONS[i], k, ('<small>%s</small>' % KIT_NOTE[k]) if k in KIT_NOTE else '') for i, k in enumerate(KIT))

BODY = '''<header class="top hx"><div class="wrap">
  <a href="''' + HOME + '''" aria-label="Accueil"><svg class="logo" viewBox="0 0 287 90" role="img" aria-label="EB Formation Consulting"><use href="#optplogo"/></svg></a>
  <nav class="nav" aria-label="Menu"><a href="''' + HOME + '''">Accueil</a><a href="#offres" aria-current="page">Les formations</a><a href="''' + BLOG + '''">Blog</a><a href="''' + CONTACT + '''">Contact</a><a class="btn wpnav" href="https://winterpack.oseprendretaplace.fr/"><span aria-hidden="true">❄</span> Winter Pack</a><a class="btn rdvbtn" href="''' + AUDIT + '''">Audit offert</a></nav>
</div></header>
<main id="top">

<section class="fh"><div class="wrap">
  <div class="fh-t"><span class="hand">Ose prendre ta place · la formation</span>
    <h1>Personne ne t’a appris à manager. <em>Moi si.</em></h1>
    <p class="lede">Pas à tes côtés, mais avec toi. Je ne te donne pas un cours. Je travaille avec toi pendant 12 semaines. Pour que plus jamais tu ne te demandes si tu es fait pour être manager.</p>
    <div class="ctas"><a class="btn rdvbtn" href="#offres">Découvrir les formules ''' + ARR + '''</a><a class="btn ghost2" href="''' + RDV + '''" target="_blank" rel="noopener">On fait le point ?</a></div></div>
  <div class="fh-v"><div class="arch"><img src="''' + ARCH_O + '''" alt="Élodie Boyer" width="420" height="540"></div>
    <div class="fh-st"><b>12</b>semaines</div><div class="fh-st s2"><b>6</b>modules</div></div>
</div>
<div class="wrap"><ul class="fh-s"><li><b>6 séances</b><span>de coaching individuel avec moi, 1 h en visio à chaque fois</span></li><li><b>30 min</b><span>par jour : c’est le temps à prévoir</span></li><li><b>À vie</b><span>l’accès à la plateforme, mises à jour incluses</span></li></ul></div></section>

''' + P.BAND + '''
<section class="room mv3" id="moment"><div class="wrap">
  <div class="ctr"><span class="hand">On fait le point ?</span><h2 class="h2 mv3-h">5 raisons qui font que c’est <em>LE</em> moment</h2>
    <p class="sub">Je ne vais pas te convaincre avec des arguments bateau, parce que tu les vis au quotidien :</p></div>
  <ol class="mv3-l">''' + ''.join('<li class="%s"><span class="mv3-n" aria-hidden="true">%02d</span><p><span class="mv3-p">Parce que</span> %s</p></li>' % ('r' if i % 2 else 'l', i + 1, t) for i, t in enumerate(WHY_NOW)) + '''</ol>
  <div class="ctarow center"><a class="btn rdvbtn" href="''' + RDV + '''" target="_blank" rel="noopener">On en parle ? ''' + ARR + '''</a></div>
</div></section>

<section class="room mint" id="pour-toi"><div class="wrap">
  <div class="ctr"><span class="hand">C’est fait pour toi si :</span><h2 class="h2">Est-ce que « Ose Prendre Ta Place » est fait pour toi ?</h2></div>
  <div class="fit"><div class="fit-c yes"><h3>C’est fait pour toi si :</h3>''' + ul(FOR_YES, 'fit-l') + '''</div>
    <div class="fit-c no"><h3>Ce n’est <em>pas</em> fait pour toi si :</h3><ul class="fit-l">''' + ''.join('<li>%s<span>%s</span></li>' % (CROSS, x) for x in FOR_NO) + '''</ul></div></div>
</div></section>

<section class="room" id="qui"><div class="wrap aq">
  <div class="aq-a"><span class="hand">À qui s’adresse Ose Prendre Ta Place ?</span><h2 class="h2">Aux experts métiers qui sont passés managers</h2>
    <p class="sub">Que tu le sois depuis quelques semaines ou depuis plusieurs années.</p></div>
  <div class="aq-b"><p class="aq-big">Ceux qui étaient les meilleurs dans leur métier et à qui personne n’a jamais vraiment appris à manager une équipe.</p>
    <div class="aq-tags"><span>Peu importe ton secteur d’activité.</span><span>Peu importe que tu manages 1 ou 30 personnes.</span></div>
    <p>Si tu n’as jamais eu de vraie méthode pour manager et que ça se voit dans ton quotidien, ce programme est fait pour toi.</p></div>
</div></section>

<section class="room peach" id="former"><div class="wrap">
  <div class="why2 solo"><div class="why2-a"><span class="hand">Pourquoi je peux te former ?</span>
      <p class="why2-q"><span aria-hidden="true">“</span>Parce que j’ai fait toutes les erreurs possibles.</p>
      <img class="why2-p" src="''' + ARCH_T + '''" alt="Élodie Boyer" width="420" height="540"></div>
    <div class="why2-b"><p>J’ai été <mark>manager autoritaire</mark>, oui, vraiment. Celle qui pense qu’un ordre bien donné suffit. Puis je suis passée à l’autre extrême : <mark>manager Bisounours</mark>, à dire oui à tout, à vouloir que tout le monde m’aime plutôt que d’être respectée.</p>
      <p><b>Les milliards de questions que tu te poses en rentrant chez toi le soir, je me les suis déjà posées.</b> La boule au ventre en pensant au lendemain, aussi. Perdre le contrôle d’une réunion devant toute l’équipe, aussi. Ne pas te sentir légitime dans ton propre poste, aussi. Cacher tes angoisses derrière un sourire de façade en réunion, aussi.</p>
      <p class="why2-k">Je ne te parle pas de théorie. Je te parle de <mark>douze ans à manager des équipes</mark> grandes, moyennes, petites, sur site, à distance, à l’échelle nationale.</p>
      <p>J’ai testé, je me suis plantée, j’ai recommencé. Ce que je t’enseigne, ce n’est pas ce qu’on m’a appris dans un livre. <b>C’est ce que j’ai vécu, dans les deux sens, avant de trouver ce qui fonctionne vraiment.</b></p></div></div>
  <div class="obj"><span class="hand">Mon objectif ?</span><p>T’apporter tout ce qu’il y a de plus concret, pratique et utile pour ton quotidien.</p><p class="obj-b">Que tu n’aies plus jamais besoin de moi après.</p></div>
</div></section>

<section class="room" id="offres"><div class="wrap">
  <div class="ctr"><span class="hand">La formation complète</span><h2 class="h2">Tu es prêt·e pour la transformation ?</h2>
    <p class="sub">Ose Prendre Ta Place, c’est un parcours complet : 6 modules réunis dans une progression de 12 semaines, avec Élodie à tes côtés pour passer de la théorie à ta réalité de terrain. Tu avances sur l’ensemble de ton management : ta posture, ta façon de lire ton équipe, ton autorité, ta communication, l’individuel et le collectif.</p></div>
  <article class="oc"><div class="oc-a"><span class="trk-k">Ose Prendre Ta Place</span><h3>C’est la transformation complète !</h3>''' + ul(OSE_ITEMS, 'oc-l') + '''</div>
    <div class="oc-b"><p class="oc-k">Résultats de « Ose Prendre Ta Place » :</p>
      <p class="res">Tu n’improvises plus. <b>Tu sais.</b><br>Tu n’esquives plus. <b>Tu oses.</b><br>Tu n’attends plus d’être légitime. <b>Tu l’es.</b></p>
      <p class="oc-bn">🎁 <b>Bonus inclus :</b> l’Atelier Stratégie Managériale trimestriel, Manager, mais pour toi aussi.</p>
      <div class="oc-p"><b>1 497 €</b><span>paiement en 2 fois possible</span></div>
      <a class="btn rdvbtn big" href="''' + PAY_OSE + '''">Je me lance ! ''' + ARR + '''</a></div></article>
</div></section>

<section class="room mint" id="programme"><div class="wrap">
  <div class="pg-h"><span class="hand">Le programme</span><h2 class="h2">6 modules pour construire ton management, étape par étape</h2>
    <p class="sub">De ta prise de posture à la dynamique de ton équipe, chaque module travaille une dimension concrète de ton rôle de manager. Tu commences par poser les bases, comprendre ton équipe et affirmer ta posture. Puis tu apprends à communiquer, à manager chaque collaborateur et à faire avancer le collectif.</p>
    <p class="pg-q">Une progression pensée pour passer du « je fais comme je peux » à un management qui te ressemble et qui fonctionne sur le terrain.</p></div>
  <div class="mds"><div class="mds-c"><p class="mdg-t ga">Modules 1 à 3 · <b>Incarne ta posture</b></p>''' + ''.join(mod_card(i, m) for i, m in enumerate(MODS[:3])) + '''</div>
    <div class="mds-c"><p class="mdg-t gb">Modules 4 à 6 · <b>Booste ton équipe</b></p>''' + ''.join(mod_card(i + 3, m) for i, m in enumerate(MODS[3:])) + '''</div></div>
  ''' + kit_html() + '''
</div></section>

<section class="room" id="options"><div class="wrap">
  <div class="ctr"><span class="hand">Des options sur-mesure</span><h2 class="h2">Tu veux te concentrer sur un besoin précis ?</h2>
    <p class="sub">Tu n’as pas besoin de travailler les 6 modules ? La formation peut aussi se suivre en deux parcours de 3 modules, selon ce que tu veux travailler aujourd’hui.</p></div>
  <div class="pks">''' + pack('Incarne ta posture', 'Construire ta posture de manager.', 'RESET, Lecture d’équipe, Posture & Crédibilité', '897 €', PAY_INCARNE) + pack('Booste ton équipe', 'Agir concrètement sur ton management individuel et collectif.', 'Courage & Influence, Alliance individuelle, Collectif', '897 €', PAY_BOOSTE) + '''</div>
</div></section>

<section class="room peach" id="etapes"><div class="wrap">
  <div class="ctr"><span class="hand">Les étapes</span><h2 class="h2">Comment se passe l’inscription ?</h2></div>
  <ol class="stp">''' + ''.join('<li><span class="stp-n">%d</span><span class="stp-k">%s</span><h3>%s</h3><p>%s</p></li>' % (i + 1, k, h, t) for i, (k, h, t) in enumerate(STEPS)) + '''</ol>
  <div class="ctarow center"><a class="btn rdvbtn" href="''' + RDV + '''" target="_blank" rel="noopener">Je prends RDV avec Élodie ''' + ARR + '''</a></div>
</div></section>

<section class="room" id="elodie"><div class="wrap co">
  <img class="co-p" src="''' + ORANGE + '''" alt="Élodie Boyer" width="640" height="640">
  <span class="hand">Hello, moi c’est Élodie !</span>
  <p class="cq">« Ce n’est pas la plateforme qui te coache. <em>C’est moi.</em> »</p>
  <div class="co-g"><div class="co-c"><span class="co-k">Les vidéos</span><p>Il y a des vidéos, oui, pour t’apporter <b>le cadre et la méthode</b>. Parce que sans ça, tu apprends sur le tas, à l’usure, en te plantant, en recommençant, comme moi pendant des années. Le cadre et la méthode, c’est ce qui te fait gagner tout ce temps-là.</p>
      <p>Ils vont aussi te rendre <b>100 % autonome</b> pour que tu n’aies plus jamais besoin de moi.</p></div>
    <div class="co-c me"><span class="co-k">Avec moi</span><p>Mais le vrai travail, <b>celui qui fait la différence</b>, se fait avec moi, <b>sur ta situation à toi</b>, pas sur un scénario écrit six mois avant que tu t’inscrives.</p></div></div>
</div></section>

<section class="room mint" id="malgre"><div class="wrap tr">
  <div><span class="hand">Malgré tout ce que tu as déjà tenté…</span><h2 class="h2">Tu as déjà essayé, et ça ne tient pas.</h2></div>
  <ul class="tr-l">''' + ''.join('<li><span aria-hidden="true">✕</span>%s</li>' % t for t in TRIED) + '''</ul>
</div></section>

<section class="fin2"><div class="wrap">
  <span class="hand">Travaillons ensemble</span>
  <h2>Ose prendre ta place de manager et libère ton potentiel !</h2>
  <p>30 minutes pour faire le point sur ta situation managériale : on identifie ce qui bloque vraiment, je te donne mon analyse directe, et on voit ensemble quelle formule peut t’aider à avancer.</p>
  <p class="fin2-k">Pas de pression. Juste de l’efficacité.</p>
  <a class="btn rdvbtn big" href="''' + RDV + '''" target="_blank" rel="noopener">Je prends RDV avec Élodie ''' + ARR + '''</a>
</div></section>

<section class="room peach" id="avis"><div class="wrap">
  <div class="tm-h"><div><span class="hand">Ils témoignent</span><h2 class="h2">Ce que disent les managers qui ont suivi la formation</h2></div><p class="sp-google big">''' + P.GOOGLE + '''</p></div>
  <div class="tms">''' + ''.join(avis(*a) for a in AVIS) + '''</div><p class="tm-hint">Fais défiler pour lire tous les avis →</p>
</div></section>

<section class="room" id="mots"><div class="wrap">
  <div class="ctr"><p class="wq">« La bienveillance sans le cadre n’existe pas. Le cadre sans la bienveillance non plus. »</p>
    <p class="wtags"><span>Bienveillance</span><span>Leadership</span><span>Posture</span><span>Courage managérial</span></p>
    <p class="sub">Des mots qu’on te répète depuis que t’es manager. Personne ne t’a jamais dit ce qu’il faut faire, concrètement, pour les incarner.</p></div>
  <div class="wds">''' + ''.join('<figure class="wd"><blockquote>%s</blockquote><figcaption>%s</figcaption></figure>' % w for w in WORDS) + '''</div>
  <p class="wd-end">Avec moi, chaque mot devient une action. <b>Pas un concept de plus à afficher sur un post-it !</b></p>
</div></section>

<section class="room" id="bonus"><div class="wrap">
  <div class="bx"><div class="bx-a"><span class="bx-tag">🎁 Bonus exclusif · réservé aux managers du programme</span>
      <h2>Manager, mais pour toi aussi.</h2>
      <p>Parler de ton équipe, c’est bien. Mais si tu ne sais pas où tu vas, si ton agenda déborde, ou si ta relation avec ton N+1 te met en porte-à-faux chaque semaine, ta stratégie managériale ne tiendra jamais (même avec la meilleure équipe du monde).</p>
      <p>Alors, pour tous mes managers qui travaillent avec moi : en plus de tes modules et de ton coaching, tu as accès chaque trimestre à un atelier réservé aux managers du programme.</p></div>
    <div class="bx-b"><p class="bx-k">On y travaille ensemble :</p><ol>''' + ''.join('<li><span>%d</span>%s</li>' % (i + 1, b) for i, b in enumerate(BONUS)) + '''</ol><p class="bx-in">Inclus dans Ose Prendre Ta Place.</p></div></div>
  <p class="fm-quote">« Passer enfin du savoir-faire au savoir-faire faire. »</p>
</div></section>

<section class="room peach" id="faq"><div class="wrap fqw">
  <div><span class="hand">FAQ</span><h2 class="h2">Je réponds à tes questions</h2>
    <p class="sub">Si tu as encore des questions, c’est par ici :</p><a class="btn rdvbtn" href="''' + RDV + '''" target="_blank" rel="noopener">Je prends RDV avec Élodie ''' + ARR + '''</a></div>
  <div class="faq">''' + ''.join('<details class="fq"><summary>%s</summary><div class="fq-a">%s</div></details>' % (q, ''.join('<p>%s</p>' % x for x in a)) for q, a in FAQ) + '''</div>
</div></section>
</main>
<script>
(function(){
  var tops = [].slice.call(document.querySelectorAll('.md-top'));
  function even(){
    tops.forEach(function(t){ t.style.minHeight = ''; });
    if (window.innerWidth <= 1020) return;
    var h = 0;
    tops.forEach(function(t){ h = Math.max(h, t.getBoundingClientRect().height); });
    tops.forEach(function(t){ t.style.minHeight = Math.ceil(h) + 'px'; });
  }
  even();
  window.addEventListener('resize', even);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(even);
  window.addEventListener('load', even);
})();
</script>
<footer><div class="wrap"><span><b>Élodie Boyer</b> · Formatrice en management passionnée qui aide les managers à réaliser leur plein potentiel<br>© 2026 EB Formation Consulting · <span class="flg"><a href="https://www.oseprendretaplace.fr/politique-de-confidentialite">Politique de confidentialité</a> · <a href="https://www.oseprendretaplace.fr/conditions-utilisation">Conditions d’utilisation</a> · <a href="https://www.oseprendretaplace.fr/politique-cookies">Politique de cookies</a></span></span><nav aria-label="Liens"><a href="''' + HOME + '''">Accueil</a><a href="''' + BLOG + '''">Blog</a><a href="''' + CONTACT + '''">Contact</a><span class="fso"><a href="https://www.linkedin.com/in/elodie-boyer-299891143/" target="_blank" rel="noopener" aria-label="LinkedIn · Élodie Boyer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M8 11v5M8 8v.01M12 16v-5M12 13a2 2 0 0 1 4 0v3"/></svg></a><a href="https://www.instagram.com/elodie_boyer_off_management/" target="_blank" rel="noopener" aria-label="Instagram · elodie_boyer_off_management"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5v.01"/></svg></a></span></nav></div></footer>
'''

CSS_F = '''<style>
.nav a[aria-current="page"]{color:var(--pine);font-weight:800;}
.ctr{text-align:center;display:flex;flex-direction:column;align-items:center;}
.ctr .h2{max-width:24ch!important;margin-inline:auto;} .ctr .sub{max-width:68ch;margin-inline:auto;}
/* hero */
.fh{background:var(--peach);position:relative;overflow:hidden;}
.fh::before{content:"";position:absolute;left:-160px;bottom:-200px;width:520px;height:520px;border-radius:50%;background:rgba(255,145,77,.12);}
.fh > .wrap:first-child{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:72px;align-items:center;padding-block:96px 48px;position:relative;}
.fh h1{font-family:var(--display);font-weight:400;font-size:clamp(42px,5.8vw,78px);line-height:1.02;margin:12px 0 24px;color:var(--pine);}
.fh h1 em{font-style:normal;font-family:var(--hand);font-weight:700;color:var(--ember-ink);font-size:1.08em;display:inline-block;transform:rotate(-2deg);}
.fh .lede{font-size:19px;color:var(--ink);max-width:52ch;line-height:1.6;}
.fh .ctas{margin-top:36px;}
.btn.ghost2{background:transparent;color:var(--pine);border:2px solid var(--pine);box-shadow:none;}
.btn.ghost2:hover{background:var(--pine);color:#fff;}
.fh-v{position:relative;justify-self:center;width:min(100%,340px);}
.fh-v .arch{border-color:#fff;}
.fh-st{position:absolute;left:-64px;top:22%;background:#fff;border-radius:18px;padding:12px 18px;font-size:14px;font-weight:700;box-shadow:0 16px 34px -18px rgba(29,42,40,.45);transform:rotate(-4deg);}
.fh-st b{display:block;font-family:var(--display);font-weight:400;font-size:30px;line-height:1;color:var(--pine);}
.fh-st.s2{left:auto;right:-50px;top:62%;transform:rotate(3deg);}
.fh-s{list-style:none;margin:0;padding:34px 0 56px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;border-top:1.5px dashed rgba(8,80,85,.2);position:relative;}
.fh-s b{display:block;font-family:var(--display);font-weight:400;font-size:clamp(28px,3vw,38px);line-height:1;color:var(--ember-ink);}
.fh-s span{display:block;margin-top:6px;font-size:15px;font-weight:700;color:var(--muted);max-width:30ch;}
/* pourquoi c'est le moment: big alternating sentences */
main > .room.mv3{padding-top:clamp(64px,7vw,96px);}
.mv3-h{max-width:none!important;}
.mv3-h em{font-style:normal;color:var(--pine);text-decoration:underline;text-decoration-color:rgba(255,145,77,.55);text-decoration-thickness:5px;text-underline-offset:6px;}
.mv3-l{list-style:none;margin:56px auto 0;padding:0;max-width:980px;display:grid;gap:26px;}
.mv3-l li{position:relative;width:min(100%,640px);padding:30px 34px 30px 110px;border-radius:28px;background:var(--peach);}
.mv3-l li.r{margin-left:auto;background:var(--mint);}
.mv3-n{position:absolute;left:26px;top:22px;font-family:var(--display);font-size:62px;line-height:1;color:var(--ember);opacity:.55;}
.mv3-l li.r .mv3-n{color:var(--teal);opacity:.7;}
.mv3-l p{margin:0;font-family:var(--display);font-size:clamp(19px,1.9vw,23px);line-height:1.4;color:var(--ink);}
.mv3-l mark{background:none;color:var(--pine);font-weight:400;box-shadow:inset 0 -.32em 0 rgba(255,145,77,.2);padding:0 2px;}
.mv3-p{display:block;font-family:var(--hand);font-weight:700;font-size:25px;line-height:1;color:var(--teal);margin-bottom:8px;}

.mv3 .ctarow{margin-top:48px;}
/* highlights in "pourquoi je peux te former" */
.why2-b mark{background:none;color:var(--ink);font-weight:800;box-shadow:inset 0 -.45em 0 rgba(255,145,77,.38);padding:0 2px;}
.why2-b b{color:var(--pine);}
.why2-k{font-family:var(--display);font-size:clamp(20px,2vw,24px)!important;line-height:1.35!important;color:var(--pine)!important;}
.why2-k mark{font-weight:400!important;color:var(--pine)!important;}
/* fit */
.fit{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;margin-top:48px;}
.fit-c{padding:34px 32px;border-radius:28px;background:#fff;box-shadow:0 22px 40px -32px rgba(8,80,85,.7);}
.fit-c h3{font-family:var(--display);font-weight:400;font-size:26px;margin:0 0 20px;}
.fit-c.no h3 em{font-style:normal;color:#C2410C;text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:4px;}
.fit-l{list-style:none;margin:0;padding:0;display:grid;gap:14px;}
.fit-l li{display:flex;gap:12px;align-items:flex-start;font-size:16px;line-height:1.5;}
.fit-l svg{flex:none;width:22px;height:22px;margin-top:2px;}
.fit-c.yes circle{fill:var(--teal);} .fit-c path{fill:none;stroke:#fff;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;}
.fit-c.no{background:#FFF7F2;} .fit-c.no circle{fill:#E0663B;}
/* à qui */
.aq{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:72px;align-items:center;}
.aq-big{font-family:var(--display);font-size:clamp(24px,2.6vw,32px);line-height:1.25;color:var(--pine);margin:0 0 22px;}
.aq-tags{display:flex;flex-wrap:wrap;gap:10px;margin:0 0 22px;}
.aq-tags span{background:var(--mint);color:var(--pine);border-radius:999px;padding:9px 16px;font-weight:800;font-size:14.5px;}
.aq-b > p:last-child{margin:0;font-size:17px;line-height:1.65;}
/* pourquoi je peux te former (with photo) */
.why2.solo{margin-top:0;align-items:start;background:#fff;}
.why2-p{display:block;width:min(100%,200px);height:auto;aspect-ratio:420/540;object-fit:cover;margin-top:30px;border-radius:110px 110px 22px 22px;transform:rotate(-3deg);box-shadow:0 22px 34px -22px rgba(8,80,85,.6);}
.obj{margin-top:40px;text-align:center;padding:clamp(30px,4vw,48px);border-radius:30px;background:var(--pine);color:#fff;}
.obj .hand{color:var(--ember);}
.obj p{margin:6px auto 0;max-width:46ch;font-size:19px;color:var(--on-pine-soft);}
.obj-b{font-family:var(--display);font-size:clamp(26px,3vw,36px)!important;line-height:1.2;color:#fff!important;margin-top:14px!important;}
/* offre complète */
.oc{margin-top:52px;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:28px 56px;padding:clamp(32px,5vw,56px);border-radius:34px;background:var(--pine);color:#fff;box-shadow:0 34px 60px -40px rgba(8,80,85,.95);}
.oc .trk-k{color:var(--ember);} .oc h3{font-family:var(--display);font-weight:400;font-size:clamp(30px,3.4vw,42px);line-height:1.1;margin:6px 0 24px;color:#fff;}
.oc-l{list-style:none;margin:0;padding:0;display:grid;gap:12px;}
.oc-l li{display:flex;gap:12px;align-items:flex-start;font-size:16px;line-height:1.45;color:#fff;}
.oc-l svg{flex:none;width:20px;height:20px;margin-top:2px;} .oc-l circle{fill:var(--ember);} .oc-l path{fill:none;stroke:#2B1304;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;}
.oc-b{display:flex;flex-direction:column;justify-content:center;gap:14px;padding:30px;border-radius:26px;background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.14);}
.oc-k{margin:0;font-weight:800;color:#FFCFA3;}
.oc .res{margin:0;font-family:var(--hand);font-size:25px;line-height:1.25;color:#fff;} .oc .res b{color:#FFCFA3;font-weight:700;}
.oc-bn{margin:0;font-size:15px;color:var(--on-pine-soft);} .oc-bn b{color:#fff;}
.oc-p{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-top:4px;}
.oc-p b{font-family:var(--display);font-weight:400;font-size:48px;line-height:1;color:#FFCFA3;} .oc-p span{color:var(--on-pine-soft);font-size:14px;}
.oc .btn{align-self:flex-start;white-space:nowrap;}
@media (max-width:560px){.oc-b{padding:22px;} .oc .btn{align-self:stretch;justify-content:center;}}
/* programme */
.pg-q{font-family:var(--hand);font-size:clamp(23px,2.4vw,28px);line-height:1.2;color:var(--pine);max-width:46ch;margin:6px auto 0;}

.mdg-t{margin:0;text-align:center;padding:12px;border-radius:999px;font-size:15px;color:#fff;}
.mdg-t.ga{background:var(--teal);} .mdg-t.gb{background:var(--ember-ink);}
.mds{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin-top:48px;align-items:start;}
.mds-c{display:flex;flex-direction:column;gap:20px;}
.md-dt{margin-top:4px;border-radius:18px;background:var(--mint);}
.md.gb .md-dt{background:var(--peach);}
.md-dt summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:10px;padding:14px 18px;font-weight:800;font-size:15px;color:var(--pine);border-radius:18px;}
.md.gb .md-dt summary{color:var(--ember-ink);}
.md-dt summary::-webkit-details-marker{display:none;}
.md-dt summary:hover{background:rgba(15,134,138,.1);} .md.gb .md-dt summary:hover{background:rgba(255,145,77,.14);}
.md-dt summary:focus-visible{outline:3px solid var(--ember);outline-offset:2px;}
.md-c{display:grid;place-items:center;min-width:24px;height:24px;padding:0 7px;border-radius:999px;background:var(--teal);color:#fff;font-size:12.5px;}
.md.gb .md-c{background:var(--ember);color:#2B1304;}
.md-chv{margin-left:auto;width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;transition:transform .2s;}
.md-dt[open] .md-chv{transform:rotate(180deg);}
.md-dt[open] summary{border-bottom:1.5px dashed rgba(8,80,85,.18);border-radius:18px 18px 0 0;}
.md-dt .md-l{padding:16px 18px 18px;}
.md-dt .md-x{margin:0 18px 18px;background:#fff;}
@media (prefers-reduced-motion:reduce){.md-chv{transition:none;}}
.md{background:#fff;border-radius:26px;padding:28px 28px 26px;border-top:6px solid var(--teal);box-shadow:0 20px 36px -30px rgba(8,80,85,.7);}
.md.gb{border-top-color:var(--ember);}
.md-h{display:flex;gap:16px;align-items:flex-start;margin-bottom:14px;}
.md-n{flex:none;font-family:var(--display);font-size:44px;line-height:.9;color:var(--teal);} .md.gb .md-n{color:var(--ember);}
.md-k{font-size:12px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);}
.md h3{font-family:var(--display);font-weight:400;font-size:24px;line-height:1.15;margin:2px 0 2px;}
.md-t{margin:0;font-family:var(--hand);font-size:22px;color:var(--teal);} .md.gb .md-t{color:var(--ember-ink);}
.md-top{display:flex;flex-direction:column;}
.md-d{margin:0 0 16px;color:var(--ink);line-height:1.6;}
.md-l{list-style:none;margin:0;padding:0;display:grid;gap:9px;}
.md-l li{display:flex;gap:10px;align-items:flex-start;font-size:15px;line-height:1.45;color:var(--ink);}
.md-l svg{flex:none;width:18px;height:18px;margin-top:2px;} .md-l circle{fill:var(--teal);} .md.gb .md-l circle{fill:var(--ember);} .md-l path{fill:none;stroke:#fff;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;}
.md-x{margin:14px 0 0;padding:10px 14px;border-radius:14px;background:var(--mint);font-size:14.5px;font-weight:700;color:var(--pine);}
/* packs */
.pks{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;margin-top:48px;}
.pk{display:flex;flex-direction:column;gap:14px;padding:34px 32px;border-radius:28px;background:var(--paper);border:2px solid var(--line);}
.pk:first-child{border-top:6px solid var(--teal);} .pk:last-child{border-top:6px solid var(--ember);}
.pk h3{font-family:var(--display);font-weight:400;font-size:30px;margin:0;}
.pk-w{margin:0;font-weight:800;color:var(--pine);}
.pk-l{list-style:none;margin:4px 0 0;padding:0;display:grid;gap:10px;}
.pk-l li{display:flex;gap:10px;align-items:flex-start;font-size:15.5px;line-height:1.45;}
.pk-l svg{flex:none;width:19px;height:19px;margin-top:2px;} .pk-l circle{fill:var(--teal);} .pk-l path{fill:none;stroke:#fff;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;}
.pk-bn{margin:4px 0 0;padding:12px 16px;border-radius:16px;background:var(--peach);font-size:14.5px;color:var(--ember-ink);font-weight:700;}
.pk-f{margin-top:auto;padding-top:18px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;border-top:1.5px dashed var(--line);}
.pk-f b{font-family:var(--display);font-weight:400;font-size:40px;line-height:1;}
/* étapes */
.stp{list-style:none;margin:52px 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px;position:relative;}
.stp::before{content:"";position:absolute;left:12%;right:12%;top:28px;border-top:2.5px dashed rgba(180,86,31,.35);}
.stp li{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;gap:6px;padding:0 6px;}
.stp-n{display:grid;place-items:center;width:56px;height:56px;border-radius:50%;background:var(--ember);color:#fff;font-family:var(--display);font-size:24px;box-shadow:0 0 0 8px var(--peach);margin-bottom:10px;}
.stp li:last-child .stp-n{background:var(--pine);}
.stp-k{font-size:12.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--ember-ink);}
.stp h3{font-family:var(--display);font-weight:400;font-size:23px;margin:0;}
.stp p{margin:4px 0 0;color:var(--ink);font-size:15.5px;line-height:1.55;}
#etapes .ctarow{margin-top:48px;}
/* elodie coach: centered */
.co{display:flex;flex-direction:column;align-items:center;text-align:center;}
.co-p{width:150px;height:150px;border-radius:50%;object-fit:cover;border:6px solid #fff;box-shadow:0 18px 34px -18px rgba(8,80,85,.6);margin-bottom:18px;}
.co .cq{max-width:22ch;margin:6px auto 40px!important;}
.co-g{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:22px;text-align:left;width:100%;}
.co-c{padding:30px 32px;border-radius:26px;background:var(--mint);}
.co-c p{margin:0 0 14px;line-height:1.65;color:var(--ink);} .co-c p:last-child{margin:0;}
.co-c b{color:var(--pine);}
.co-k{display:inline-block;margin-bottom:12px;font-size:12.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--teal);}
.co-c.me{background:var(--pine);display:flex;flex-direction:column;justify-content:flex-start;}
.co-c.me .co-k{color:var(--ember);} .co-c.me p{font-family:var(--display);font-size:clamp(21px,2.2vw,26px);line-height:1.3;color:#fff;} .co-c.me b{color:#FFCFA3;font-weight:400;}
/* elodie coach */
.cq{font-family:var(--display);font-size:clamp(28px,3.2vw,40px);line-height:1.18!important;color:var(--pine);margin:10px 0 24px!important;}
.cq em{font-style:normal;color:var(--ember-ink);}
#elodie .ab{align-items:center!important;} #elodie .ab-v{position:static!important;align-self:center!important;} #elodie .ab-v img{max-width:320px;}
#elodie .ab-sign{line-height:1.3!important;}
/* malgré tout */
.tr{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:64px;align-items:center;}
.tr-l{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;}
.tr-l li{display:flex;gap:12px;align-items:flex-start;padding:18px 20px;border-radius:20px;background:#fff;font-size:15.5px;line-height:1.45;box-shadow:0 14px 26px -24px rgba(8,80,85,.7);}
.tr-l li span{flex:none;display:grid;place-items:center;width:26px;height:26px;border-radius:50%;background:var(--peach2);color:var(--ember-ink);font-size:13px;font-weight:800;}
.tr-l li:last-child{background:var(--pine);color:#fff;font-weight:800;} .tr-l li:last-child span{background:var(--ember);color:#2B1304;}
/* mots */
.wq{font-family:var(--display);font-size:clamp(26px,3.2vw,40px);line-height:1.2;color:var(--pine);max-width:30ch;margin:0 auto 22px;}
.wtags{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin:0 0 20px;}
.wtags span{border:2px solid var(--pine);color:var(--pine);border-radius:999px;padding:8px 16px;font-weight:800;font-size:14.5px;}
.wds{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px;margin-top:44px;}
.wd{margin:0;padding:26px 24px;border-radius:24px;background:#FFF1C9;box-shadow:0 18px 28px -24px rgba(29,42,40,.5);}
.wd:nth-child(2){background:var(--peach2);transform:rotate(1.2deg);} .wd:nth-child(3){background:var(--mint);transform:rotate(-1deg);} .wd:nth-child(4){background:#FFDCC7;transform:rotate(1.5deg);}
.wd:first-child{transform:rotate(-1.5deg);}
.wd blockquote{margin:0 0 12px;font-family:var(--hand);font-weight:700;font-size:23px;line-height:1.15;color:var(--ink);}
.wd figcaption{font-size:15px;line-height:1.5;color:var(--ink);}
.wd-end{margin:48px auto 0;text-align:center;font-size:clamp(19px,2vw,23px);max-width:52ch;color:var(--ink);} .wd-end b{color:var(--ember-ink);}
/* bonus */
.bx{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:40px 56px;align-items:center;padding:clamp(32px,5vw,60px);border-radius:34px;background:linear-gradient(135deg,var(--peach2),#FFF1C9);border:2px dashed var(--ember);}
.bx-tag{display:inline-block;background:var(--ember);color:#2B1304;border-radius:999px;padding:8px 16px;font-size:13px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;}
.bx h2{font-family:var(--display);font-weight:400;font-size:clamp(32px,4vw,50px);line-height:1.08;margin:18px 0 18px;color:var(--pine);}
.bx-a p{margin:0 0 14px;line-height:1.65;color:var(--ink);}
.bx-b{background:#fff;border-radius:26px;padding:28px;}
.bx-k{margin:0 0 14px;font-weight:800;color:var(--pine);}
.bx-b ol{list-style:none;margin:0;padding:0;display:grid;gap:12px;}
.bx-b li{display:flex;align-items:center;gap:12px;font-family:var(--display);font-size:20px;color:var(--ink);}
.bx-b li span{flex:none;display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--pine);color:#fff;font-size:16px;}
.bx-in{margin:18px 0 0;font-family:var(--hand);font-size:23px;color:var(--ember-ink);}
/* faq */
.fqw{display:grid;grid-template-columns:minmax(0,.7fr) minmax(0,1.3fr);gap:64px;align-items:start;}
.fqw > div:first-child{position:sticky;top:110px;} .fqw .btn{margin-top:8px;}
.fqw .faq{margin-top:0;max-width:none;}
.fq-a p b{color:var(--pine);}
@media (max-width:1020px){
  .fh > .wrap:first-child,.aq,.tr,.oc,.bx,.fqw,.fit,.pks,.co-g{grid-template-columns:1fr;}
  .fh > .wrap:first-child{padding-block:64px 36px;gap:48px;} .fh-st{left:-16px;} .fh-st.s2{right:-16px;}
  .fh-s{grid-template-columns:1fr;gap:18px;}
  .mds{grid-template-columns:1fr;}
  .stp{grid-template-columns:repeat(2,minmax(0,1fr));row-gap:40px;} .stp::before{display:none;}
  .wds{grid-template-columns:repeat(2,minmax(0,1fr));}
  .fqw > div:first-child{position:static;}
}
@media (max-width:560px){
  .tr-l,.wds,.stp{grid-template-columns:1fr;} .mv3-l li{padding:76px 22px 24px;} .mv3-n{left:22px;top:18px;font-size:46px;} .fit-c,.pk{padding:26px 22px;} .md{padding:24px 20px;}
  .fh-v{width:min(100%,260px);}
}
</style>
'''
html = head + CSS_A + CSS_F + BODY + defs
open(S + 'home/formations-test.html', 'w', encoding='utf-8').write(html)
print(len(html))
