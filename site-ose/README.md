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
