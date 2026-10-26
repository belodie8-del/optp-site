# Refonte du site oseprendretaplace.fr (essai)

Pages refaites avec les codes du Winter Pack (couleurs, polices, finitions), sans mention du Winter Pack.

- `accueil.html` : page d'accueil retenue (version A). Fichier autonome : les images et les polices sont incluses.
- `formations.html` : page Les formations (essai), avec tous les textes de la page actuelle.
- `blog.html` : page du blog (essai), avec les 7 articles et un filtre par thème.
- `blog-article-modele.html` : modèle de page article (exemple : « Combien de doliprane… »).
- `contact.html` : page Contact (essai). Le formulaire est un aperçu : sur le site, c'est celui de Systeme.io qui envoie les messages.
- `accueil-version-B.html`, `accueil-version-C.html` : les deux autres pistes proposées.
- `source/` : scripts qui génèrent les pages (`make_home2.py` pour l'accueil version A, `make_home3.py` pour B et C, `make_formations.py` pour la page Formations, `make_blog.py` pour le blog, `make_contact.py` pour la page Contact).
- `images/` : photos d'Élodie recadrées et visuels des articles du blog.

Rien n'est en ligne : le site actuel reste sur Systeme.io.

Animations : `source/anim.py` ajoute à chaque page les apparitions au défilement, les compteurs de chiffres, les surlignages qui se tracent et quelques effets au survol. Elles sont désactivées pour les visiteurs qui ont demandé moins d'animations sur leur appareil. `source/build_site.sh` régénère toutes les pages d'un coup.

Pop-up Winter Pack : intégré à la page d'accueil (`source/popup_home.py`). `popup-winter-pack-systemeio.html` est la version autonome à coller dans un bloc Code HTML de la page d'accueil actuelle sur Systeme.io. La ligne « Cadeau de lancement » disparaît seule après le dimanche 25 octobre 2026 à 23 h 59.

Mise en ligne : `systemeio/` contient les blocs à coller dans Systeme.io (accueil, formations, contact 1 et 2, blog 1 et 2, pop-up seul), générés par `source/export_sio.py`. Leurs images sont dans `images-sio/` et sont servies par le site Winter Pack à l'adresse https://winterpack.oseprendretaplace.fr/ose/ (copiées dans le ZIP par `make_deploy.py`).

Formules : `source/formules.py` titre chaque formule par la situation du manager (Posture de manager, Management d’équipe, Parcours complet), garde son nom juste en dessous, ajoute le bloc « Par où commencer ? » à la page Formations et appelle « parcours » les formules de 3 modules. `build_site.sh` l’applique après `anim.py`.

Référencement (Google et assistants IA) : `source/seo.py` ajoute aux pages des données structurées (organisation, Élodie Boyer, les 3 formations, le Winter Pack et ses offres, les FAQ relues sur la page même), écrit `llms.txt` (résumé du site pour les IA) et des plans de site datés. Il sert à `make_netlify.py` et au `make_deploy.py` du Winter Pack.

Pages légales : `politique-de-confidentialite.html`, `conditions-utilisation.html` et `politique-cookies.html`, générées par `source/make_legal.py` à partir des textes de `source/legal/*.md` (repris des documents du Drive). Le pied de page de toutes les pages renvoie vers ces 3 adresses et vers LinkedIn et Instagram.

Hébergement Netlify : `site-ose-netlify.zip` (contenu dans `deploy-site-ose/`, généré par `source/make_netlify.py`) contient tout le nouveau site, servi à l'adresse écrite dans `source/site_base.txt` (aujourd'hui https://oseprendretaplace-formation.netlify.app ; `source/rebase.py` l'injecte dans toutes les pages à la fin de `build_site.sh`). www.oseprendretaplace.fr reste chez Systeme.io (paiements, remerciements, espace membre, blog) : le fichier `_redirects` y renvoie les adresses inconnues, et seules les pages accueil, formations et contact du tunnel Systeme.io redirigent vers le nouveau site, avec les codes `systemeio/redirection-*.html` à coller dans leur code d'en-tête. Pour donner au site son propre nom de domaine plus tard : changer `site_base.txt`, relancer `build_site.sh`, `export_sio.py`, `make_netlify.py`.
