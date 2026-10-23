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

Pages légales : `politique-de-confidentialite.html`, `conditions-utilisation.html` et `politique-cookies.html`, générées par `source/make_legal.py` à partir des textes de `source/legal/*.md` (repris des documents du Drive). Le pied de page de toutes les pages renvoie vers ces 3 adresses et vers LinkedIn et Instagram.
