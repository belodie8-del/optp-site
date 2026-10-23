"""Legal pages of oseprendretaplace.fr (privacy, terms of use, cookies) with the codes of the new site.
Texts come from Élodie's Drive documents (legal/*.md, light markup). Output: legal-<slug>.html."""
import re, html as H
exec(open('_pre.py', encoding='utf-8').read())
exec(open('_cssA.py', encoding='utf-8').read())
HOME = 'https://oseprendretaplace.fr/'
MAIL = 'contact@oseprendretaplace.fr'
SITE = 'https://oseprendretaplace.fr/'
PAGES = [  # slug, md, short label, title, facts (En bref)
 ('politique-de-confidentialite', 'confidentialite', 'Confidentialité', 'Politique de confidentialité',
  [('Responsable du traitement', 'Élodie Boyer, EB Formation Consulting'), ('Données collectées', 'Nom, prénom, adresse mail'),
   ('Durée de conservation', '3 ans, puis effacement automatique'), ('Partage', 'Aucune donnée vendue, louée ou transmise à des tiers')]),
 ('conditions-utilisation', 'conditions', 'Conditions d’utilisation', 'Conditions d’utilisation et mentions légales',
  [('Éditrice du site', 'Élodie Boyer · SIRET 921 209 896 00023'), ('Adresse', '74 Grande Rue, 70100 Gray'),
   ('Contenus', 'Reproduction interdite sans accord exprès'), ('Supports de formation', 'Ni don, ni revente')]),
 ('politique-cookies', 'cookies', 'Cookies', 'Politique de cookies',
  [('À quoi ils servent', 'Sécurité, mesure d’audience, confort de navigation'), ('Ton choix', 'Refusables dans les réglages du navigateur'),
   ('Google Analytics', 'Désactivable sur tous les sites'), ('Une question ?', MAIL)]),
]
URL = {p[0]: SITE + p[0] for p in PAGES}
LEGAL_LINKS = ' · '.join('<a href="%s">%s</a>' % (URL[s], t) for s, t in
    [('politique-de-confidentialite', 'Politique de confidentialité'), ('conditions-utilisation', 'Conditions d’utilisation'), ('politique-cookies', 'Politique de cookies')])

def inline(t):
    t = H.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: '<a href="%s"%s>%s</a>' % (
        m.group(2), '' if m.group(2).startswith(SITE) else ' target="_blank" rel="noopener"', m.group(1)), t)
    t = re.sub(r'(?<![\w/:">])contact@oseprendretaplace\.fr', '<a href="mailto:%s">%s</a>' % (MAIL, MAIL), t)
    return t

def render(md):
    out, toc, lst, tbl, n = [], [], [], [], 0
    opened = False
    def flush():
        if lst: out.append('<ul>' + ''.join('<li>%s</li>' % x for x in lst) + '</ul>'); lst.clear()
        if tbl:
            rows = ''
            for head, cells in tbl:
                rows += '<tr>' + ''.join('<%s>%s</%s>' % ('th' if (head or i == 0) else 'td', c, 'th' if (head or i == 0) else 'td') for i, c in enumerate(cells)) + '</tr>'
            out.append('<div class="lg-tw"><table class="lg-tb">%s</table></div>' % rows); tbl.clear()
    for line in md.strip().split('\n'):
        if line.startswith('- '): lst.append(inline(line[2:])); continue
        if line.startswith('|'):
            head = line.startswith('|#')
            cells = [inline(c.strip()) for c in line.strip('|#').strip().strip('|').split('|')]
            tbl.append((head, cells)); continue
        flush()
        if line.startswith('## '):
            t = line[3:]; m = re.search(r'\s*\{#([\w-]+)\}$', t)
            n += 1; aid = m.group(1) if m else 'art-%d' % n
            t = t[:m.start()] if m else t
            k = re.match(r'(Article (\d+)\.|(\d+)\.)\s*(.*)', t)
            num, name = (k.group(2) or k.group(3)), k.group(4)
            if opened: out.append('</section>')
            opened = True
            out.append('<section class="lg-a" id="%s"><h2><span class="lg-n">%s</span>%s</h2>' % (aid, ('Article ' if k.group(2) else 'Partie ') + num, inline(name)))
            toc.append((aid, num, name))
        elif line.startswith('@@ Date de la dernière mise à jour'):
            pass  # already shown in the hero
        elif line.startswith('@@ '):
            out.append('<p class="lg-note">%s</p>' % inline(line[3:]))
        elif line.strip():
            out.append('<p>%s</p>' % inline(line))
    flush()
    # close the last article before the trailing notes
    body = '\n'.join(out)
    first_note = body.find('<p class="lg-note">')
    if first_note > 0: body = body[:first_note] + '</section>\n<div class="lg-notes">' + body[first_note:] + '</div>'
    else: body += '</section>'
    if not body.lstrip().startswith('<section'):  # intro text before the first article
        i = body.index('<section')
        body = '<div class="lg-intro">' + body[:i] + '</div>' + body[i:]
    return body, toc

def footer(cur=None):
    links = LEGAL_LINKS
    if cur: links = links.replace('href="%s"' % URL[cur], 'href="%s" aria-current="page"' % URL[cur])
    return ('<footer><div class="wrap"><span><b>Élodie Boyer</b> · Formatrice en management passionnée qui aide les managers à réaliser leur plein potentiel<br>'
            '© 2026 EB Formation Consulting · <span class="flg">' + links + '</span></span>'
            '<nav aria-label="Liens"><a href="' + HOME + '">Accueil</a><a href="' + FORM + '">Les formations</a><a href="' + BLOG + '">Blog</a><a href="' + CONTACT + '">Contact</a><span class="fso"><a href="https://www.linkedin.com/in/elodie-boyer-299891143/" target="_blank" rel="noopener" aria-label="LinkedIn · Élodie Boyer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M8 11v5M8 8v.01M12 16v-5M12 13a2 2 0 0 1 4 0v3"/></svg></a><a href="https://www.instagram.com/elodie_boyer_off_management/" target="_blank" rel="noopener" aria-label="Instagram · elodie_boyer_off_management"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5v.01"/></svg></a></span></nav></div></footer>')

def page(slug, mdname, short, title, facts):
    body, toc = render(open('legal/%s.md' % mdname, encoding='utf-8').read())
    tabs = ''.join('<a href="%s"%s>%s</a>' % (URL[s], ' aria-current="page"' if s == slug else '', lab) for s, _, lab, _, _ in PAGES)
    items = ''.join('<li><a href="#%s"><span>%s</span>%s</a></li>' % (a, n, H.escape(t, quote=False)) for a, n, t in toc)
    brief = ''.join('<li><small>%s</small><b>%s</b></li>' % (k, inline(v)) for k, v in facts)
    return '''<header class="top hx"><div class="wrap">
  <a href="''' + HOME + '''" aria-label="Accueil"><svg class="logo" viewBox="0 0 287 90" role="img" aria-label="EB Formation Consulting"><use href="#optplogo"/></svg></a>
  <nav class="nav" aria-label="Menu"><a href="''' + HOME + '''">Accueil</a><a href="''' + FORM + '''">Les formations</a><a href="''' + BLOG + '''">Blog</a><a href="''' + CONTACT + '''">Contact</a><a class="btn wpnav" href="https://winterpack.oseprendretaplace.fr/"><span aria-hidden="true">❄</span> Winter Pack</a><a class="btn rdvbtn" href="''' + AUDIT + '''">Audit offert</a></nav>
</div></header>
<main id="top">
<section class="lgh"><div class="wrap">
  <span class="hand">Informations légales</span>
  <h1>''' + title + '''</h1>
  <p class="lgh-m">Dernière mise à jour : 25/09/2025 · EB Formation Consulting</p>
  <nav class="lgt" aria-label="Pages légales">''' + tabs + '''</nav>
</div></section>
<section class="lgb"><div class="wrap lg-g">
  <aside class="lg-side"><nav class="lg-toc" aria-label="Sommaire"><p class="lg-toc-h">Sommaire</p><ol>''' + items + '''</ol></nav></aside>
  <div class="lg-main">
    <details class="lg-tocm"><summary>Sommaire <span>''' + str(len(toc)) + ''' parties</span></summary><ol>''' + items + '''</ol></details>
    <div class="lg-k"><p class="lg-k-h">En bref</p><ul>''' + brief + '''</ul></div>
    <article class="lg-x">''' + body + '''</article>
    <div class="lg-c"><div><p class="lg-c-h">Une question sur ces informations ?</p><p>Écris-moi à <a href="mailto:''' + MAIL + '''">''' + MAIL + '''</a>, je te réponds rapidement.</p></div>
      <a class="btn rdvbtn" href="''' + CONTACT + '''">Me contacter ''' + ARR + '''</a></div>
  </div>
</div></section>
</main>
''' + footer(slug) + '\n'

CSS_L = '''<style>
.lgh{background:var(--peach);}
.lgh .wrap{padding-block:clamp(56px,7vw,88px) clamp(36px,4vw,48px);}
.lgh h1{font-family:var(--display);font-weight:400;font-size:clamp(36px,4.6vw,58px);line-height:1.06;margin:8px 0 14px;color:var(--pine);max-width:20ch;text-wrap:balance;}
.lgh-m{margin:0;color:var(--muted);font-size:15.5px;}
.lgt{display:flex;flex-wrap:wrap;gap:10px;margin-top:28px;}
.lgt a{padding:10px 18px;border-radius:999px;background:#fff;border:1.5px solid var(--line);color:var(--pine);font-weight:800;font-size:14.5px;text-decoration:none;transition:border-color .15s,background .15s;}
.lgt a:hover{border-color:var(--teal);}
.lgt a[aria-current="page"]{background:var(--pine);border-color:var(--pine);color:#fff;}
.lgt a:focus-visible,.lg-toc a:focus-visible,.lg-x a:focus-visible{outline:3px solid var(--ember);outline-offset:3px;}
.lgb{background:var(--paper);}
.lg-g{display:grid;grid-template-columns:260px minmax(0,1fr);gap:clamp(32px,5vw,72px);align-items:start;padding-block:clamp(48px,6vw,80px) clamp(64px,8vw,104px);}
.lg-side{position:sticky;top:104px;max-height:calc(100vh - 128px);overflow:auto;}
.lg-toc-h{margin:0 0 12px;font-size:12.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);}
.lg-toc ol,.lg-tocm ol{list-style:none;margin:0;padding:0;display:grid;gap:2px;}
.lg-toc a,.lg-tocm a{display:grid;grid-template-columns:28px minmax(0,1fr);gap:6px;padding:7px 10px;border-radius:10px;color:var(--ink);text-decoration:none;font-size:14.5px;line-height:1.35;}
.lg-toc a span,.lg-tocm a span{color:var(--teal);font-weight:800;}
.lg-toc a:hover,.lg-tocm a:hover{background:var(--mint);}
.lg-toc a.on{background:var(--mint);color:var(--pine);font-weight:700;}
.lg-tocm{display:none;margin-bottom:24px;border:1.5px solid var(--line);border-radius:18px;padding:4px 8px;}
.lg-tocm summary{cursor:pointer;padding:12px 8px;font-weight:800;color:var(--pine);list-style-position:inside;}
.lg-tocm summary span{font-weight:600;color:var(--muted);margin-left:6px;}
.lg-tocm ol{padding-bottom:8px;}
.lg-main{min-width:0;max-width:760px;}
.lg-k{background:var(--mint);border-radius:26px;padding:24px 26px;margin-bottom:44px;}
.lg-k-h{margin:0 0 14px;font-family:var(--hand);font-weight:700;font-size:28px;line-height:1;color:var(--ember-ink);}
.lg-k ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;}
.lg-k li{background:#fff;border-radius:16px;padding:14px 16px;}
.lg-k small{display:block;font-size:12px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-bottom:4px;}
.lg-k b{display:block;color:var(--pine);font-size:15.5px;line-height:1.4;word-break:break-word;}
.lg-k b a{color:inherit;}
.lg-x{font-size:16.5px;line-height:1.72;color:var(--ink);}
.lg-x p{margin:0 0 14px;max-width:68ch;}
.lg-intro{padding:0 0 8px;margin-bottom:28px;border-bottom:2px dashed var(--line);}
.lg-intro p{font-size:18px;line-height:1.65;}
.lg-a{padding-top:30px;margin-top:6px;border-top:1.5px solid var(--line);scroll-margin-top:100px;}
.lg-a:first-of-type,.lg-intro + .lg-a{border-top:0;padding-top:0;}
.lg-a h2{font-family:var(--display);font-weight:400;font-size:clamp(23px,2.4vw,28px);line-height:1.2;margin:0 0 16px;color:var(--pine);text-wrap:balance;}
.lg-n{display:block;font-family:var(--body);font-size:12.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--ember-ink);margin-bottom:6px;}
.lg-x ul{list-style:none;margin:0 0 16px;padding:0;display:grid;gap:8px;max-width:68ch;}
.lg-x li{position:relative;padding-left:22px;}
.lg-x li::before{content:"";position:absolute;left:4px;top:.72em;width:7px;height:7px;border-radius:50%;background:var(--ember);}
.lg-x a{color:var(--teal);font-weight:700;text-decoration:underline;text-decoration-thickness:1.5px;text-underline-offset:3px;word-break:break-word;}
.lg-x a:hover{color:var(--pine);}
.lg-tw{overflow-x:auto;margin:4px 0 18px;max-width:68ch;}
.lg-tb{width:100%;border-collapse:collapse;font-size:15.5px;line-height:1.5;}
.lg-tb th,.lg-tb td{text-align:left;vertical-align:top;padding:11px 14px;border-bottom:1.5px solid var(--line);}
.lg-tb tr:first-child th,.lg-tb tr:first-child td{border-top:1.5px solid var(--line);}
.lg-tb th{width:38%;font-weight:800;color:var(--pine);background:var(--peach);}
.lg-tb tr:first-child th + th{background:var(--peach);}
.lg-notes{margin-top:36px;padding-top:22px;border-top:2px dashed var(--line);}
.lg-note{font-size:14px;line-height:1.6;color:var(--muted);margin:0 0 8px;}
.lg-c{margin-top:48px;display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;background:var(--peach);border-radius:26px;padding:26px 28px;}
.lg-c p{margin:0;color:var(--ink);font-size:16px;line-height:1.55;}
.lg-c a:not(.btn){color:var(--teal);font-weight:800;word-break:break-word;}
.lg-c-h{font-family:var(--display);font-size:22px !important;color:var(--pine) !important;margin-bottom:4px !important;}
.nav a[aria-current="page"]{color:var(--pine);font-weight:800;}
@media (max-width:900px){.lg-g{grid-template-columns:1fr;} .lg-side{display:none;} .lg-tocm{display:block;}}
@media (max-width:560px){.lg-k ul{grid-template-columns:1fr;gap:8px;} .lg-k{padding:20px 16px;margin-bottom:36px;} .lg-k li{padding:10px 14px;} .lg-k b{font-size:15px;} .lg-x{font-size:16px;} .lg-c{padding:22px 20px;} .lg-c .btn{width:100%;justify-content:center;} .lgt a{font-size:13.5px;padding:9px 14px;}}
@media (prefers-reduced-motion:reduce){.lgt a{transition:none;}}
</style>
'''
JS_L = '''<script>(function(){var l=[].slice.call(document.querySelectorAll('.lg-toc a'));if(!l.length)return;
var ss=l.map(function(a){return document.getElementById(a.getAttribute('href').slice(1));}),t=0;
function u(){t=0;var y=innerHeight*.3,k=-1;ss.forEach(function(s,i){if(s&&s.getBoundingClientRect().top<y)k=i;});l.forEach(function(a,i){a.classList.toggle('on',i===k);});}
addEventListener('scroll',function(){if(!t)t=requestAnimationFrame(u);},{passive:true});u();})();</script>
'''
if __name__ == '__main__':
    for slug, md, short, title, facts in PAGES:
        h = head.replace('<title>Ose prendre ta place · Accueil</title>', '<title>%s · Ose prendre ta place</title>' % title, 1)
        open(S + 'home/legal-%s.html' % slug, 'w', encoding='utf-8').write(h + CSS_A + CSS_L + page(slug, md, short, title, facts) + JS_L + defs)
    print('ok')
