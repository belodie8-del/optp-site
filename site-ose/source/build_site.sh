#!/bin/sh
set -e
cd "$(dirname "$0")"
python3 make_home2.py >/dev/null
python3 - <<'P'
s=open('make_home2.py',encoding='utf-8').read()
a=s.index("BODY = '''"); b=s.index("CSS = '''"); c=s.index("html = head + CSS + BODY + defs")
open('_pre.py','w',encoding='utf-8').write(s[:a])
open('_bodyA.py','w',encoding='utf-8').write(s[a:b].replace("BODY = '''","BODY_A = '''",1))
open('_cssA.py','w',encoding='utf-8').write(s[b:c].replace("CSS = '''","CSS_A = '''",1))
P
python3 make_home3.py >/dev/null
cp accueil-A.html accueil-test.html
python3 make_formations.py >/dev/null
python3 make_blog.py >/dev/null
python3 make_contact.py >/dev/null
python3 anim.py accueil-A.html accueil-B.html accueil-C.html accueil-test.html formations-test.html blog-test.html article-test.html contact-test.html
python3 popup_home.py accueil-A.html accueil-B.html accueil-C.html accueil-test.html
python3 popup_home.py --block popup-winter-pack-systemeio.html
python3 make_blog_sio.py
python3 make_contact_sio.py >/dev/null
python3 make_legal.py >/dev/null
python3 anim.py contact-sio.html legal-politique-de-confidentialite.html legal-conditions-utilisation.html legal-politique-cookies.html
