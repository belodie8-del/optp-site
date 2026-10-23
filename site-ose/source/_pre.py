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
FORM = 'https://www.oseprendretaplace.fr/formations'
BLOG = 'https://oseprendretaplace.systeme.io/leblogose'
CONTACT = 'https://www.oseprendretaplace.fr/contact'
RDV = 'https://calendly.com/eb-formationconsulting/30min'
WPK = 'https://winterpack.oseprendretaplace.fr/'
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

