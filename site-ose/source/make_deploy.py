"""Turns the Winter Pack page fragment into a standalone site folder (index.html + legal pages) and a zip."""
import os, re, shutil, zipfile, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-optp-site/1386eaca-821b-50a5-926e-8bdc38c36a33/scratchpad/home')
import seo
R = '/home/user/optp-site/'
OUT = R + 'deploy-winter-pack/'
frag = open(R + 'winter-pack.html', encoding='utf-8').read()

i = frag.index('</style>') + len('</style>')
head_inner, body = frag[:i], frag[i:]
head_inner = head_inner.replace('<title>Winter Pack · Humain</title>', '')
head_inner = head_inner.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
DESC = '8 outils prêts à l’emploi pour tes managers : trames d’entretien annuel et de parcours professionnel (loi 2025), OTO, réunion d’équipe, objectifs. Dès 197 €.'
TITLE = 'Trames d’entretien annuel et de parcours professionnel · Winter Pack'
URL = 'https://winterpack.oseprendretaplace.fr/'
meta = ('<meta charset="UTF-8">\n<meta name="google-site-verification" content="vvfP6Ki-xjIGNlaZxGgeBjxDDMKPneN8TT4x25t-X7E" />\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<title>%(t)s</title>\n<meta name="description" content="%(d)s">\n'
        '<link rel="canonical" href="%(u)s">\n'
        '<meta property="og:url" content="%(u)s">\n<meta property="og:type" content="website">\n<meta property="og:locale" content="fr_FR">\n'
        '<meta property="og:site_name" content="EB Formation Consulting">\n'
        '<meta property="og:image" content="%(u)sog-image.jpg">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="627">\n<meta name="twitter:card" content="summary_large_image">\n'
        '<meta property="og:title" content="%(t)s">\n<meta property="og:description" content="%(d)s">\n') % {'t': TITLE, 'd': DESC, 'u': URL}
html = '<!DOCTYPE html>\n<html lang="fr">\n<head>\n' + meta + seo.wp_ld(body) + head_inner + '\n</head>\n<body>\n' + body + '\n</body>\n</html>\n'

if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)
open(OUT + 'index.html', 'w', encoding='utf-8').write(html)
open(OUT + 'robots.txt', 'w').write('User-agent: *' + chr(10) + 'Allow: /' + chr(10) + 'Sitemap: ' + URL + 'sitemap.xml' + chr(10))
open(OUT + 'sitemap.xml', 'w').write(seo.sitemap([URL]))
open(OUT + 'llms.txt', 'w', encoding='utf-8').write(seo.LLMS_WP)
for f in ['winter-pack-cgv.html', 'winter-pack-confidentialite.html', 'winter-pack-mentions-legales.html']:
    shutil.copy(R + f, OUT + f)

open(OUT + 'google6dff6d42b5b88ba4.html', 'w').write('google-site-verification: google6dff6d42b5b88ba4.html')

shutil.copy(R + 'winter-pack-og.jpg', OUT + 'og-image.jpg')

# images of the Ose prendre ta place pages (served at /ose/ for the Systeme.io code blocks)
os.makedirs(OUT + 'ose', exist_ok=True)
for f in os.listdir(R + 'site-ose/images-sio'):
    shutil.copy(R + 'site-ose/images-sio/' + f, OUT + 'ose/' + f)

zp = R + 'winter-pack-site.zip'
if os.path.exists(zp):
    os.remove(zp)
with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
    for dp, dn, fn in os.walk(OUT):
        for f in sorted(fn):
            full = os.path.join(dp, f); z.write(full, os.path.relpath(full, OUT))
print([ (f, os.path.getsize(OUT + f)) for f in sorted(os.listdir(OUT)) ], os.path.getsize(zp))
