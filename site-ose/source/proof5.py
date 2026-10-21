"""Social proof added to the sales page: logos band, key figures, two post-it walls, newsletter band.
Applied last by build_all.py on winter-pack-5-humain.html."""
import base64, glob
S = '/tmp/claude-0/-home-user-optp-site/1386eaca-821b-50a5-926e-8bdc38c36a33/scratchpad/'
L = S + 'site/logos/'
BOOK = 'https://calendly.com/eb-formationconsulting/winter-pack'
NEWS_URL = 'https://urls.fr/noz8GK'

def logo(name, alt):
    f = glob.glob(L + '*' + name + '.svg')[0]
    t = open(f, encoding='utf-8').read().replace('fill="#FDFAF6"', 'fill="#085055"').replace('fill="#F6EDD9"', 'fill="#085055"')
    return '<img src="data:image/svg+xml;base64,%s" alt="%s">' % (base64.b64encode(t.encode()).decode(), alt)
LOGOS = ''.join('<li>%s</li>' % logo(n, a) for n, a in [('actua', 'Actua'), ('sos', 'SOS Oxygène'), ('eleven', 'Eleven Australia'), ('pigier', 'Pigier')])

# envelope only (crop of her newsletter illustration)
news = open(L + 'news.svg', encoding='utf-8').read()
news = news.replace('width="884" height="425" viewBox="0 0 884 425"', 'width="345" height="385" viewBox="0 45 345 385"')
NEWS_IMG = 'data:image/svg+xml;base64,' + base64.b64encode(news.encode()).decode()

STAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z"/></svg>'
STARS = '<span class="sp-stars" role="img" aria-label="5 étoiles sur 5">%s</span>' % (STAR * 5)
GLOGO = ('<svg class="sp-g" viewBox="0 0 48 48" aria-hidden="true"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/>'
         '<path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/>'
         '<path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/>'
         '<path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/></svg>')
VERIF = ('<span class="sp-ver">%s<span>Avis Google vérifié</span>'
         '<svg class="sp-ok" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M7.5 12.5l3 3 6-6.5"/></svg></span>') % GLOGO
GOOGLE = '%s%s<span class="sp-gt"><b>5/5</b> avis Google <span>sur la qualité des formations</span></span>' % (GLOGO, STARS)

# (quote, name, role, tint, tilt)
WALL = [
 ("Excellente formation ! J’en ressors enrichie, confiante et pleinement motivée pour la suite.", "Sandrine R.", "Responsable Administrative", 'y', 'l'),
 ("Une vraie valeur ajoutée par rapport aux autres formations.", "Anthony D.", "Dirigeant BTP", 'p', 'r'),
 ("Les vidéos ne sont pas de la grande théorie déconnectée de la réalité, bien au contraire.", "Mégane J.", "Manager d’agence", 'y', 'l2'),
 ("Il y a toujours une solution, et Élodie va la co-construire avec vous.", "Élisa G.", "Responsable de Pôle", 'y', 'l', True),
 ("Des outils concrets pour évoluer dans le domaine du management !", "Adrien S.", "Responsable Commercial", 'p', 'r2', True),
 ("Concret, pratique !", "Célia M.", "Futur Manager", 'y', 'r', True),
]
def note(q, n, r, tint, tilt, google=False):
    if len(q) < 30: tilt += ' short'
    return '<figure class="sp-note t-%s %s"><blockquote>%s</blockquote><figcaption><b>%s</b> · %s%s</figcaption></figure>' % (tint, tilt, q, n, r, VERIF if google else '')

STATS = [('+5 000', 'managers dans la newsletter'), ('+9 000', 'abonnés LinkedIn'), ('5/5', 'avis Google'), ('+10 ans', 'd’expérience terrain')]
STATS_SECTION = ('<section class="sp-stats" aria-label="Chiffres clés"><div class="wrap"><ul>%s</ul></div></section>\n\n'
  % ''.join('<li><b>%s</b><span>%s</span></li>' % x for x in STATS))

BAND = '<div class="sp-band"><div class="wrap"><div class="sp-logos"><p>Ils me font confiance</p><ul>%s</ul></div></div></div>\n\n' % LOGOS

WALL1 = ('<section class="room peach" id="avis"><div class="wrap">'
  '<span class="hand">Ils en parlent mieux que moi</span>'
  '<h2 class="h2">Ce qu’en disent les managers formés</h2>'
  '<p class="sp-google big">%s</p>'
  '<div class="sp-wall">%s</div>'
  '</div></section>\n\n') % (GOOGLE, ''.join(note(*w) for w in WALL[:3]))

WALL2 = '<div class="sp-wall sp-wall-in">%s</div>\n  ' % ''.join(note(*w) for w in WALL[3:])

NEWS_SECTION = ('<section class="news" id="newsletter"><div class="wrap">'
  '<img class="news-ill" src="%s" alt="" width="345" height="385">'
  '<div class="news-t"><span class="hand">La newsletter</span>'
  '<h2>Le Coup de Boost Managérial</h2>'
  '<p class="news-p">Chaque lundi à 6h30, mes conseils pour bien démarrer ta semaine de manager.</p>'
  '<p class="news-proof"><b>5 000</b><span>managers la lisent déjà chaque lundi</span></p>'
  '<a class="btn rdvbtn" href="%s" target="_blank" rel="noopener">Je m’abonne <span aria-hidden="true">→</span></a>'
  '</div></div></section>\n\n') % (NEWS_IMG, NEWS_URL)

CSS = '''<style>
.sp-stars{display:inline-flex;gap:2px;flex:none;}
.sp-stars svg{width:19px;height:19px;fill:var(--ember);}
.sp-google{margin:0;display:flex;align-items:center;gap:10px;font-size:15.5px;line-height:1.3;color:var(--ink);}
.sp-gt b{font-weight:800;color:var(--pine);font-size:17px;margin-right:2px;}
.sp-gt{display:block;}
.sp-google.big{width:fit-content;margin:18px 0 0;padding:9px 20px 9px 16px;border-radius:999px;background:#fff;box-shadow:0 12px 24px -18px rgba(29,42,40,.55);}
.sp-google.big .sp-stars svg{width:22px;height:22px;}
.sp-band{background:var(--paper);border-top:1.5px dashed rgba(8,80,85,.16);border-bottom:1.5px dashed rgba(8,80,85,.16);padding:18px 0;}
.sp-band .wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;}
.sp-logos{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px 28px;}
.sp-logos p{margin:0;font-family:var(--hand);font-weight:700;font-size:24px;line-height:1;color:var(--ember-ink);}
.sp-logos ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px 30px;}
.sp-logos li img{display:block;height:32px;width:auto;max-width:120px;object-fit:contain;opacity:.62;}
.sp-stats{background:var(--paper);border-top:1.5px dashed rgba(8,80,85,.16);border-bottom:1.5px dashed rgba(8,80,85,.16);padding:30px 0;}
.sp-stats ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:22px 18px;}
.sp-stats li{text-align:center;display:flex;flex-direction:column;align-items:center;gap:6px;}
.sp-stats li + li{border-left:1.5px dashed rgba(8,80,85,.16);}
.sp-stats b{font-family:var(--display);font-weight:400;font-size:clamp(34px,4.4vw,52px);line-height:1;color:var(--pine);}
.sp-stats li:nth-child(odd) b{color:var(--ember-ink);}
.sp-stats span{font-size:15.5px;font-weight:700;color:var(--muted);line-height:1.3;max-width:15ch;}
.sp-wall{display:grid;grid-template-columns:minmax(0,1fr);gap:38px 30px;margin-top:44px;padding:0 6px;}
@media (min-width:700px){.sp-wall{grid-template-columns:repeat(3,minmax(0,1fr));gap:30px 22px;}}
@media (min-width:700px) and (max-width:980px){.sp-note{padding:24px 18px 16px;} .sp-note blockquote{font-size:22px;} .sp-note.short blockquote{font-size:32px;}}
.sp-note{position:relative;margin:0;padding:26px 24px 18px;border-radius:4px 4px 20px 4px;box-shadow:0 22px 28px -22px rgba(29,42,40,.55);display:flex;flex-direction:column;justify-content:space-between;gap:14px;}
.sp-note.t-y{background:#FFF1C9;} .sp-note.t-p{background:#FFDCC7;}
.sp-note.l{transform:rotate(-1.8deg);} .sp-note.r{transform:rotate(1.6deg);} .sp-note.l2{transform:rotate(-1deg);} .sp-note.r2{transform:rotate(2.2deg);}
.sp-note::before{content:"";position:absolute;top:-11px;left:50%;width:84px;height:22px;margin-left:-42px;background:rgba(15,134,138,.25);transform:rotate(-3deg);border-radius:3px;}
.sp-note blockquote{margin:0;font-family:var(--hand);font-weight:700;font-size:26px;line-height:1.15;color:var(--ink);}
.sp-note.short blockquote{font-size:40px;line-height:1.05;}
.sp-note figcaption{font-size:14px;color:var(--muted);}
.sp-note figcaption b{color:var(--pine);}
#avis{padding-block:clamp(48px,5vw,72px);}
.sp-wall-in{margin-top:68px;margin-bottom:12px;}
.sp-g{width:20px;height:20px;flex:none;}
.sp-google .sp-g{width:24px;height:24px;}
.sp-ver{display:flex;align-items:center;gap:7px;margin-top:10px;font-size:12.5px;font-weight:800;letter-spacing:.01em;color:#3c4043;}
.sp-ver .sp-g{width:16px;height:16px;}
.sp-ok{width:16px;height:16px;flex:none;}
.sp-ok circle{fill:#1a73e8;} .sp-ok path{fill:none;stroke:#fff;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;}
.news{background:var(--pine);color:var(--on-pine);}
.news .wrap{display:grid;grid-template-columns:auto minmax(0,1fr);align-items:center;gap:clamp(24px,5vw,64px);padding-block:clamp(44px,5vw,68px);}
.news-ill{width:clamp(150px,20vw,230px);height:auto;transform:rotate(-5deg);filter:drop-shadow(0 16px 20px rgba(0,0,0,.28));}
.news .hand{color:var(--ember);font-size:30px;}
.news h2{font-family:var(--display);font-weight:400;font-size:clamp(32px,4.2vw,50px);line-height:1.08;margin:4px 0 12px;color:var(--on-pine);max-width:none;}
.news-p{margin:0 0 18px;font-size:19px;color:var(--on-pine-soft);max-width:46ch;}
.news-proof{display:flex;align-items:baseline;gap:12px;margin:0 0 24px;color:var(--on-pine);}
.news-proof b{white-space:nowrap;font-family:var(--display);font-weight:400;font-size:clamp(40px,5vw,56px);line-height:1;color:var(--ember);}
.news-proof span{font-size:17px;font-weight:700;}
@media (max-width:760px){
  .sp-stats ul{grid-template-columns:repeat(2,minmax(0,1fr));gap:26px 12px;}
  .sp-stats li:nth-child(3){border-left:0;}
  .sp-stats span{font-size:14.5px;}
  .news .wrap{grid-template-columns:1fr;text-align:left;}
  .news-ill{width:150px;}
  .sp-logos li img{height:26px;}
  .sp-google{font-size:14.5px;}
  .sp-note blockquote{font-size:24px;}
}
</style>
'''


def add_proof(s):
    # 1) logos band under the hero
    k = '<section class="room peach" id="constat">'
    assert s.count(k) == 1
    s = s.replace(k, BAND + k, 1)
    # 2) key figures right after "Qui je suis"; the creds keep only the two diplomas
    i = s.index('id="qui"'); e = s.index('</section>', i) + len('</section>')
    s = s[:e] + '\n\n' + STATS_SECTION.rstrip('\n') + s[e:]
    for old in ('<div><b>10 ans +</b>de terrain RH et management</div>', '<div><b>300</b>managers formés</div>'):
        assert s.count(old) == 1, old
        s = s.replace(old, '', 1)
    # 3) first three testimonials after "Tu en as besoin si", the other three (verified Google reviews) at the very bottom of "Le management au centre", under its RDV button
    i = s.index('id="besoin"'); e = s.index('</section>', i) + len('</section>')
    s = s[:e] + '\n\n' + WALL1.rstrip('\n') + s[e:]
    i = s.index('id="management"'); e = s.index('</section>', i)
    k = s.rindex('</div></section>', i, e + len('</section>'))
    s = s[:k] + '  ' + WALL2.strip() + '\n' + s[k:]
    # 4) newsletter band before the final call to action
    k = '<section class="room peach final">'
    assert s.count(k) == 1
    s = s.replace(k, NEWS_SECTION + k, 1)
    assert s.count('<style>') >= 1
    return s.replace('<style>', CSS + '<style>', 1)
