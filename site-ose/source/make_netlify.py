"""Whole oseprendretaplace.fr site for Netlify (www.oseprendretaplace.fr): our pages as static files, images as files,
the contact form through Netlify Forms, and every other path (payment, thank-you, member area…) redirected to the
Systeme.io pages, which move to SIO_DOMAIN. Output: /home/user/optp-site/deploy-site-ose/ and site-ose-netlify.zip."""
import re, os, shutil, hashlib, base64, zipfile, html as H
R = '/home/user/optp-site/'
OUT = R + 'deploy-site-ose/'
ZIP = R + 'site-ose-netlify.zip'
SITE = 'https://www.oseprendretaplace.fr/'
SIO_DOMAIN = 'https://espace.oseprendretaplace.fr'   # the Systeme.io tunnels and member area move here
BLOG = 'https://oseprendretaplace.systeme.io/leblogose'
OWN = ['accueil', 'formations', 'contact', 'politique-de-confidentialite', 'conditions-utilisation', 'politique-cookies']
PAGES = [  # output file, source, path, title, description
 ('index.html', 'accueil-A.html', '', 'Ose prendre ta place · Formations en management · Élodie Boyer',
  'Une méthode concrète pour incarner une autorité naturelle, fédérer ton équipe et retrouver le plaisir de manager, même si tu n’as jamais été formé(e).'),
 ('formations.html', 'formations-test.html', 'formations', 'Les formations · Ose prendre ta place',
  'Ose Prendre Ta Place, Incarne ta posture, Booste ton équipe : les formations en management d’Élodie Boyer, pour les managers qui n’ont jamais été formés.'),
 ('contact.html', 'contact-test.html', 'contact', 'Contact · Ose prendre ta place',
  'Une question sur les formations, besoin d’y voir plus clair ou envie d’échanger autour d’un sujet management ? Écris à Élodie Boyer.'),
 ('politique-de-confidentialite.html', 'legal-politique-de-confidentialite.html', 'politique-de-confidentialite', 'Politique de confidentialité · Ose prendre ta place',
  'Comment EB Formation Consulting collecte, utilise et protège les données personnelles sur oseprendretaplace.fr.'),
 ('conditions-utilisation.html', 'legal-conditions-utilisation.html', 'conditions-utilisation', 'Conditions d’utilisation et mentions légales · Ose prendre ta place',
  'Mentions légales et conditions d’utilisation du site oseprendretaplace.fr, édité par Élodie Boyer, EB Formation Consulting.'),
 ('politique-cookies.html', 'legal-politique-cookies.html', 'politique-cookies', 'Politique de cookies · Ose prendre ta place',
  'À quoi servent les cookies sur oseprendretaplace.fr et comment les gérer ou les refuser.'),
]
if os.path.isdir(OUT): shutil.rmtree(OUT)
os.makedirs(OUT + 'img')

def host(m):
    uri = m.group(0)
    if len(uri) < 2500: return uri
    head, data = uri.split(',', 1)
    ext = {'image/jpeg': 'jpg', 'image/png': 'png', 'image/svg+xml': 'svg', 'image/webp': 'webp'}[head[5:].split(';')[0]]
    raw = base64.b64decode(data) if ';base64' in head else data.encode()
    name = hashlib.sha1(raw).hexdigest()[:12] + '.' + ext
    open(OUT + 'img/' + name, 'wb').write(raw)
    return '/img/' + name

def meta(path, title, desc, index=True):
    u = SITE + path
    return ('<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<meta name="google-site-verification" content="vvfP6Ki-xjIGNlaZxGgeBjxDDMKPneN8TT4x25t-X7E">\n'
            '<title>%(t)s</title>\n<meta name="description" content="%(d)s">\n' % {'t': H.escape(title), 'd': H.escape(desc)} +
            ('<link rel="canonical" href="%s">\n' % u if index else '<meta name="robots" content="noindex">\n') +
            '<meta property="og:type" content="website">\n<meta property="og:locale" content="fr_FR">\n<meta property="og:site_name" content="Ose prendre ta place · EB Formation Consulting">\n'
            '<meta property="og:url" content="%(u)s">\n<meta property="og:title" content="%(t)s">\n<meta property="og:description" content="%(d)s">\n'
            '<meta property="og:image" content="%(s)sog-image.jpg">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
            '<style>img{max-width:100%%;}[hidden]{display:none!important;}button,input,textarea{font:inherit;}</style>\n') % {'u': u, 't': H.escape(title), 'd': H.escape(desc), 's': SITE}

def build(src, path, title, desc, index=True, edit=None):
    s = open(src, encoding='utf-8').read()
    if edit: s = edit(s)
    s = re.sub(r'data:[^"\')\s]+', host, s)
    s = re.sub(r'href="https://www\.oseprendretaplace\.fr/(%s)?(?=[#"?])' % '|'.join(OWN),
               lambda m: 'href="/' + ('' if m.group(1) in (None, 'accueil') else m.group(1)), s)
    i = s.index('<header')
    head = s[:i]
    head = re.sub(r'<meta charset[^>]*>\s*|<meta name="viewport"[^>]*>\s*|<title>[^<]*</title>\s*|<meta name="claude:[^>]*>\s*', '', head)
    return '<!doctype html>\n<html lang="fr">\n<head>\n' + meta(path, title, desc, index) + head + '</head>\n<body>\n' + s[i:] + '\n</body>\n</html>\n'

def contact_form(s):
    """Netlify Forms instead of the preview form; the browser checks the required fields."""
    a = '<form class="kcf" id="kf" novalidate>'
    assert s.count(a) == 1
    s = s.replace(a, '<form class="kcf" id="kf" name="contact" method="POST" action="/merci" data-netlify="true" netlify-honeypot="bot-field" enctype="multipart/form-data">'
                  '<input type="hidden" name="form-name" value="contact"><p hidden><label>Ne pas remplir : <input name="bot-field"></label></p>')
    s, n = re.subn(r'<p class="kcf-ok" role="status" hidden>.*?</p>',
                   '<p class="kcf-rg">Tes informations servent uniquement à te répondre. Plus de détails dans la '
                   '<a href="https://www.oseprendretaplace.fr/politique-de-confidentialite">politique de confidentialité</a>.</p>', s)
    assert n == 1
    a = "f.addEventListener('submit',function(e){e.preventDefault();f.querySelector('.kcf-ok').hidden=false;});"
    assert s.count(a) == 1
    s = s.replace(a, '')
    s = s.replace('</style>', '.kcf-rg{margin:0;font-size:13.5px;line-height:1.5;color:var(--muted);}.kcf-rg a{color:var(--teal);font-weight:700;}\n</style>', 1)
    return s

def merci(s):
    a = s.index('<main id="top">'); b = s.index('</main>')
    return s[:a] + '''<main id="top">
<section class="kch"><div class="wrap">
  <div class="kch-t"><span class="hand">Message envoyé</span>
    <h1>Merci, <em>c’est bien reçu !</em></h1>
    <p class="lede">Je lis ton message et je te réponds rapidement.</p>
    <p class="kch-s">En attendant, tu peux faire l’audit offert ou découvrir les formations.</p>
    <p style="display:flex;flex-wrap:wrap;gap:12px;margin-top:28px"><a class="btn rdvbtn" href="https://auditmanagerial.oseprendretaplace.fr/">Faire l’audit offert</a>
      <a class="btn" href="https://www.oseprendretaplace.fr/formations" style="background:#fff;color:var(--pine);border:2px solid var(--line)">Voir les formations</a></p></div>
  <div class="kch-v"><img src="''' + re.search(r'<div class="kch-v"><img src="([^"]+)"', s).group(1) + '''" alt="Élodie Boyer" width="420" height="540"><p class="kch-bub">À très vite 💚</p></div>
</div></section>
</main>''' + s[b + len('</main>'):].replace("var f=document.getElementById('kf');", "var f=document.getElementById('kf');if(!f)return;")

for out, src, path, title, desc in PAGES:
    open(OUT + out, 'w', encoding='utf-8').write(build(src, path, title, desc, edit=contact_form if out == 'contact.html' else None))
open(OUT + 'merci.html', 'w', encoding='utf-8').write(build('contact-test.html', 'merci', 'Merci · Ose prendre ta place', 'Ton message est bien parti.', index=False, edit=merci))

rules = [('/accueil', '/index.html', 200)] + [('/' + p, '/%s.html' % p, 200) for p in OWN[1:] + ['merci']] + [
         ('/blog', BLOG, 301), ('/*', SIO_DOMAIN + '/:splat', 301)]
open(OUT + '_redirects', 'w').write(
    '# Pages of the new site\n' + ''.join('%-32s %-40s %d\n' % r for r in rules[:-2]) +
    '# Blog on Systeme.io\n' + '%-32s %-40s %d\n' % rules[-2] +
    '# Everything else (payment, thank-you pages, member area, …) stays on Systeme.io\n' + '%-32s %-40s %d\n' % rules[-1])
open(OUT + '_headers', 'w').write('/img/*\n  Cache-Control: public, max-age=31536000, immutable\n')
open(OUT + 'robots.txt', 'w').write('User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n' % SITE)
open(OUT + 'sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    ''.join('  <url><loc>%s%s</loc></url>\n' % (SITE, p) for p in [''] + OWN[1:]) + '</urlset>\n')
open(OUT + 'google6dff6d42b5b88ba4.html', 'w').write('google-site-verification: google6dff6d42b5b88ba4.html')
open(OUT + 'favicon.svg', 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#085055"/>'
    '<text x="32" y="44" text-anchor="middle" font-family="Georgia,serif" font-size="32" fill="#FF914D">EB</text></svg>')
if os.path.exists('og-site.jpg'): shutil.copy('og-site.jpg', OUT + 'og-image.jpg')
if os.path.exists(ZIP): os.remove(ZIP)
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(OUT):
        for f in sorted(files):
            z.write(os.path.join(root, f), os.path.relpath(os.path.join(root, f), OUT))
print(sorted(os.listdir(OUT)), len(os.listdir(OUT + 'img')), 'images', os.path.getsize(ZIP) // 1024, 'Ko')
