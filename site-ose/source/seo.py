"""What Google and AI assistants read without seeing the page: structured data (JSON-LD) and llms.txt, for both sites.
Every fact comes from the pages themselves or from the legal notice; FAQ markup is read back from the final HTML, so it
always matches what visitors see."""
import json, re, html as H, datetime

MAIN = open(__file__.rsplit('/', 1)[0] + '/site_base.txt', encoding='utf-8').read().strip().rstrip('/') + '/'
WP = 'https://winterpack.oseprendretaplace.fr/'
BLOG = 'https://oseprendretaplace.systeme.io/leblogose'
AUDIT = 'https://auditmanagerial.oseprendretaplace.fr/'
LINKEDIN = 'https://www.linkedin.com/in/elodie-boyer-299891143/'
INSTA = 'https://www.instagram.com/elodie_boyer_off_management/'
MAIL = 'contact@oseprendretaplace.fr'
TODAY = datetime.date.today().isoformat()

ORG_ID, PERSON_ID = MAIN + '#organisation', MAIN + '#elodie-boyer'
ORG = {'@type': 'Organization', '@id': ORG_ID, 'name': 'EB Formation Consulting', 'alternateName': 'Ose prendre ta place',
       'url': MAIN, 'email': MAIL, 'founder': {'@id': PERSON_ID}}
PERSON = {'@type': 'Person', '@id': PERSON_ID, 'name': 'Élodie Boyer', 'jobTitle': 'Formatrice en management',
          'worksFor': {'@id': ORG_ID}, 'url': MAIN, 'sameAs': [LINKEDIN, INSTA],
          'knowsAbout': ['Management', 'Posture managériale', 'Formation de managers', 'Entretien annuel',
                         'Entretien de parcours professionnel', 'Rituels managériaux', 'Gestion de conflit']}
SITE = {'@type': 'WebSite', '@id': MAIN + '#site', 'url': MAIN, 'name': 'Ose prendre ta place',
        'inLanguage': 'fr-FR', 'publisher': {'@id': ORG_ID}}

def ld(*nodes):
    return ('<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': list(nodes)},
            ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + '</script>\n')

def _text(x):
    return H.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', x))).strip()

def faq(page_html, url, skip=()):
    """FAQPage from the page's own <details> questions (those whose question starts with a prefix in skip are left out)."""
    qa = []
    for m in re.finditer(r'<details[^>]*>\s*<summary[^>]*>(.*?)</summary>(.*?)</details>', page_html, re.S):
        q, a = _text(m.group(1)), _text(m.group(2))
        if q and a and not q.startswith(tuple(skip)):
            qa.append({'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}})
    return {'@type': 'FAQPage', '@id': url + '#faq', 'url': url, 'inLanguage': 'fr-FR', 'mainEntity': qa}

def _course(name, alt, anchor, desc, price, modules):
    return {'@type': 'Course', 'name': name, 'alternateName': alt, 'description': desc, 'url': MAIN + 'formations#' + anchor, 'inLanguage': 'fr',
            'provider': {'@id': ORG_ID}, 'coursePrerequisites': 'Aucun',
            'syllabusSections': [{'@type': 'Syllabus', 'name': m} for m in modules],
            'offers': {'@type': 'Offer', 'price': price, 'priceCurrency': 'EUR', 'category': 'Paid', 'url': MAIN + 'formations#offres'},
            'hasCourseInstance': {'@type': 'CourseInstance', 'courseMode': 'Online', 'instructor': {'@id': PERSON_ID}}}

COURSES = [
    _course('Ose Prendre Ta Place', 'Parcours complet', 'parcours-complet',
            'Formation en management en ligne : 6 modules et 6 séances de coaching individuel avec Élodie Boyer, sur 12 semaines, '
            'avec un groupe WhatsApp privé et des lives réservés aux managers du programme.', '1497',
            ['RESET', 'La Lecture d’Équipe', 'Posture & Crédibilité', 'Courage & Influence', 'L’Alliance Individuelle', 'Le Collectif']),
    _course('Incarne ta posture', 'Posture de manager', 'posture-de-manager',
            'Parcours de 3 modules pour les managers qui viennent de prendre leur poste ou qui ont encore l’impression de faire semblant : construire sa posture de manager, avec 3 séances de coaching individuel avec Élodie Boyer.', '897',
            ['RESET', 'La Lecture d’Équipe', 'Posture & Crédibilité']),
    _course('Booste ton équipe', 'Management d’équipe', 'management-equipe',
            'Parcours de 3 modules pour les managers dont l’équipe n’avance pas comme ils veulent : agir concrètement sur son management individuel et collectif, avec 3 séances de coaching '
            'individuel avec Élodie Boyer.', '897',
            ['Courage & Influence', 'L’Alliance Individuelle', 'Le Collectif']),
]

def main_ld(path, page_html):
    """JSON-LD for a page of the main site."""
    url = MAIN + path
    nodes = [SITE, ORG, PERSON]
    if path == 'formations':
        nodes += COURSES + [faq(page_html, url, skip=('Ce que tu vas travailler',))]
    return ld(*nodes)

WP_TOOLS = ['L’entretien de parcours professionnel', 'L’entretien annuel', 'La réunion d’équipe', 'La trame du OTO',
            'Le tableau de bord des objectifs', 'Le calendrier des rituels managériaux',
            'Les 10 commandements pour réussir ses entretiens', 'Le kit de survie verbal, spécial gestion de conflit']
WP_DESC = ('8 outils prêts à l’emploi pour les managers de PME : trames d’entretien annuel et d’entretien de parcours professionnel, '
           'trame du OTO, réunion d’équipe, tableau de bord des objectifs, calendrier des rituels managériaux, '
           '10 commandements pour réussir ses entretiens et kit de survie verbal pour la gestion de conflit. En PDF, sur Notion et sur Excel.')

def _offer(name, price, desc=None):
    o = {'@type': 'Offer', 'name': name, 'price': price, 'priceCurrency': 'EUR', 'availability': 'https://schema.org/InStock',
         'url': WP + '#offre', 'seller': {'@id': ORG_ID}}
    if desc: o['description'] = desc
    return o

def wp_ld(page_html):
    """JSON-LD for the Winter Pack page."""
    product = {'@type': 'Product', '@id': WP + '#winter-pack', 'name': 'Winter Pack · L’Essentiel du Manager',
               'description': WP_DESC, 'url': WP, 'image': WP + 'og-image.jpg', 'category': 'Outils de management pour PME',
               'brand': {'@type': 'Brand', 'name': 'EB Formation Consulting'},
               'offers': [_offer('Winter Pack Solo', '197', 'Pour un manager qui achète à titre personnel.'),
                          _offer('Winter Pack PME, jusqu’à 5 managers', '490'),
                          _offer('Winter Pack PME, jusqu’à 10 managers', '790'),
                          _offer('Winter Pack PME, jusqu’à 20 managers', '1190'),
                          _offer('Winter Pack PME + Prise en main', '1290', 'Le pack pour 10 managers et 2 h en visio avec les managers.'),
                          _offer('Winter Pack PME + Atelier', '2490', 'À partir de 2 490 € : le pack et une journée d’atelier en visio ou en présentiel, pour 10 managers.')]}
    page = {'@type': 'WebPage', '@id': WP + '#page', 'url': WP, 'inLanguage': 'fr-FR', 'about': {'@id': WP + '#winter-pack'},
            'author': {'@id': PERSON_ID}, 'publisher': {'@id': ORG_ID}, 'dateModified': TODAY}
    return ld(page, product, ORG, PERSON, faq(page_html, WP))

def sitemap(urls):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
            ''.join('  <url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (u, TODAY) for u in urls) + '</urlset>\n')

LLMS_MAIN = '''# Ose prendre ta place

> Formations en management en ligne, avec coaching individuel, pour les managers qui n’ont jamais été formés. Par Élodie Boyer, formatrice en management (EB Formation Consulting, France).

Élodie Boyer accompagne les managers, qu’ils viennent d’être nommés ou qu’ils managent depuis des années, sur leur posture, leur autorité naturelle, leur communication, leur équipe et leurs entretiens. Elle a accompagné des managers en laboratoire, pharmacie, intérim, coiffure et informatique. Les formations se suivent à distance : un module par semaine, puis une séance de coaching individuel sur Google Meet la semaine suivante.

## Formations

- [Ose Prendre Ta Place]({m}formations#parcours-complet) (parcours complet) : la formation complète. 6 modules (RESET, La Lecture d’Équipe, Posture & Crédibilité, Courage & Influence, L’Alliance Individuelle, Le Collectif) et 6 séances de coaching individuel sur 12 semaines, un groupe WhatsApp privé et des lives réservés aux managers du programme. 1 497 €, paiement en 2 fois possible.
- [Incarne ta posture]({m}formations#posture-de-manager) (posture de manager) : pour les managers qui viennent de prendre leur poste, ou qui ont encore l’impression de faire semblant. 3 modules (RESET, La Lecture d’Équipe, Posture & Crédibilité) et 3 séances de coaching individuel. 897 €.
- [Booste ton équipe]({m}formations#management-equipe) (management d’équipe) : pour les managers dont l’équipe n’avance pas comme ils veulent. 3 modules (Courage & Influence, L’Alliance Individuelle, Le Collectif) et 3 séances de coaching individuel. 897 €.
- Accès à la plateforme à vie. Les formations ne sont pas finançables par le CPF. L’inscription commence par un appel de 30 minutes.

## Outils

- [Winter Pack · L’Essentiel du Manager]({wp}) : 8 outils pour que tous les managers d’une PME mènent leurs entretiens avec la même méthode, dont les trames d’entretien annuel et d’entretien de parcours professionnel. Dès 197 €.
- [Audit managérial offert]({audit}) : un profil express en 3 minutes (style dominant et point de vigilance) ou un audit complet en 10 minutes (radar de maturité et plan d’action sur 3 semaines). Gratuit.

## Contenus

- [Le blog]({blog}) : articles sur le management au quotidien.
- Newsletter « Le Coup de Boost Managérial ».

## Contact

- [Page contact]({m}contact) · {mail}
- [LinkedIn]({li}) · [Instagram]({ig})
'''.format(m=MAIN, wp=WP, audit=AUDIT, blog=BLOG, mail=MAIL, li=LINKEDIN, ig=INSTA)

LLMS_WP = '''# Winter Pack · L’Essentiel du Manager

> 8 outils prêts à l’emploi pour que tous les managers d’une PME mènent leurs entretiens avec la même méthode : trames d’entretien annuel et d’entretien de parcours professionnel, OTO, réunion d’équipe, objectifs, rituels managériaux, gestion de conflit. Pour les PME sans SIRH, ou sans module entretiens. Conçu par Élodie Boyer, formatrice en management (EB Formation Consulting).

La trame d’entretien de parcours professionnel intègre la loi du 24 octobre 2025 : entretien dans l’année qui suit l’embauche puis tous les 4 ans, état des lieux récapitulatif tous les 8 ans. Les trames d’entretien annuel et de parcours professionnel existent en exemplaire manager et en exemplaire collaborateur, pour comparer les deux regards.

## Les 8 outils

{tools}

## Offres (paiement unique, sans abonnement)

- Winter Pack Solo : 197 €, pour un manager qui achète à titre personnel.
- Winter Pack PME : 490 € jusqu’à 5 managers, 790 € jusqu’à 10 managers, 1 190 € jusqu’à 20 managers. Au-delà, sur devis.
- Winter Pack PME + Prise en main : 1 290 €, le pack pour 10 managers et 2 h en visio avec les managers. Prise en charge OPCO possible.
- Winter Pack PME + Atelier : à partir de 2 490 €, le pack et une journée d’atelier en visio ou en présentiel, pour 10 managers.

Les outils sont dans un dossier Drive (PDF et tableur) et sur Notion, sans abonnement ni date d’expiration. Solo : le lien arrive par mail dès la validation du paiement. PME : les managers reçoivent leurs accès dans les 24 h après l’envoi de leurs adresses e-mail.

## Liens

- [Page du Winter Pack]({wp})
- [Conditions générales de vente]({wp}winter-pack-cgv.html)
- [Le site d’Élodie Boyer, formations en management]({m})
- Contact : {mail}
'''.format(wp=WP, m=MAIN, mail=MAIL, tools='\n'.join('- ' + t for t in WP_TOOLS))
