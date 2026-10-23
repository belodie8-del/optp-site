"""Page listing the Systeme.io blocks of the new oseprendretaplace.fr site, with copy buttons and the steps per page."""
import html
D = '/home/user/optp-site/site-ose/systemeio/'
OUT = '/tmp/claude-0/-home-user-optp-site/1386eaca-821b-50a5-926e-8bdc38c36a33/scratchpad/home/codes-site-ose.html'
PAGES = [
 ('netlify', '1 · Mettre le site sur Netlify', 'site-ose-netlify.zip',
  ['Sur Netlify : Add new site → Deploy manually, puis glisse le fichier <b>site-ose-netlify.zip</b>.',
   'Dans Forms, clique sur « Enable form detection », puis redépose le même ZIP (c’est ce qui active le formulaire de contact).',
   'Dans Forms → Form notifications, ajoute une notification e-mail vers contact@oseprendretaplace.fr.',
   'Teste le site sur l’adresse provisoire xxx.netlify.app que Netlify te donne.'],
  []),
 ('domaine', '2 · Brancher oseprendretaplace.fr (sans www)', 'Netlify + OVH',
  ['Dans Netlify : Domain management → Add a domain → <b>oseprendretaplace.fr</b>. Netlify ajoute aussi www.oseprendretaplace.fr tout seul : <b>supprime cette ligne www</b>, car www reste chez Systeme.io.',
   'Chez OVH, dans ton domaine oseprendretaplace.fr : onglet « Redirection », supprime la redirection vers www si elle existe.',
   'Toujours chez OVH, onglet « Zone DNS » : modifie l’enregistrement <b>A</b> de oseprendretaplace.fr (aujourd’hui 213.186.33.5) et mets <b>75.2.60.5</b>. Ne touche pas à la ligne www.',
   'Attends que le changement se propage (de quelques minutes à quelques heures). Netlify active le HTTPS tout seul.',
   'Vérifie que <b>https://oseprendretaplace.fr</b> affiche bien le nouveau site avant de passer à l’étape 3.'],
  []),
 ('redirection', '3 · Rediriger les pages du site Systeme.io', 'tunnel « SITE »',
  ['À faire seulement quand l’étape 2 marche. Avant, la page tournerait en boucle.',
   'Pour chacune des 3 pages ci-dessous : Modifier la page → Paramètres → Tracking → « Modifier le code d’en-tête », colle le code, puis Sauvegarder.',
   'Ne mets ce code sur aucune autre page : ni paiement, ni remerciement, ni blog.'],
  [('Page d’accueil', 'www.oseprendretaplace.fr → oseprendretaplace.fr', 'redirection-accueil.html'),
   ('Page de vente (les formations)', 'www.oseprendretaplace.fr/formations → oseprendretaplace.fr/formations', 'redirection-formations.html'),
   ('Page de contact', 'www.oseprendretaplace.fr/contact → oseprendretaplace.fr/contact', 'redirection-contact.html')]),
 ('blog', '4 · Le blog (reste sur Systeme.io)', 'oseprendretaplace.systeme.io/leblogose',
  ['Pas de redirection sur le blog : il reste sur Systeme.io pour que tes nouveaux articles s’ajoutent tout seuls.',
   'Ouvre la mise en page du blog et garde l’élément « liste des articles ». Supprime les autres sections.',
   'Au-dessus de la liste, ajoute un élément « Code HTML » avec le bloc 1. Sous la liste, un second élément « Code HTML » avec le bloc 2.'],
  [('Bloc 1', 'Au-dessus de la liste des articles', 'blog-1.html'),
   ('Bloc 2', 'En dessous de la liste des articles', 'blog-2.html')]),
]
n = 0
nav = ''.join('<a href="#%s">%s</a>' % (k, t.split(' (')[0]) for k, t, *_ in PAGES)
secs = ''
for key, title, url, steps, blocks in PAGES:
    items = ''
    for label, where, f in blocks:
        n += 1
        code = open(D + f, encoding='utf-8').read()
        kb = round(len(code.encode('utf-8')) / 1024)
        items += ('<div class="blk"><div class="bh"><div><h3>%s</h3><p>%s · %d Ko</p></div>'
                  '<button type="button" class="copy" data-t="c%d">Copier le code</button></div>'
                  '<textarea id="c%d" readonly spellcheck="false" aria-label="%s, %s">%s</textarea></div>') % (
            label, where, kb, n, n, html.escape(title), label, html.escape(code))
    secs += ('<section id="%s"><div class="sh"><h2>%s</h2><span class="url">%s</span></div><ol class="steps">%s</ol>%s</section>'
             % (key, title, url, ''.join('<li>%s</li>' % s for s in steps), items))

page = '''<title>Codes du site Ose</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Young+Serif&family=Nunito+Sans:opsz,wght@6..12,400..800&display=swap">
<style>
/* Layout: one narrow column, a step card per page, code blocks with a copy button */
:root{--bg:#FFF4EE;--card:#FFFFFF;--ink:#1D2A28;--muted:#5A6663;--pine:#085055;--teal:#0F868A;--ember:#FF914D;--on-ember:#2B1304;--line:rgba(8,80,85,.14);--code:#F4FAFA;--note:#E4F5F6;
  --display:'Young Serif',Georgia,serif;--body:'Nunito Sans',system-ui,-apple-system,'Segoe UI',sans-serif;--mono:ui-monospace,Menlo,Consolas,monospace;}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#10201F;--card:#172B2A;--ink:#EAF3F2;--muted:#A9BDBB;--pine:#9FD9DA;--teal:#5CC3C6;--ember:#FF9E61;--on-ember:#2B1304;--line:rgba(255,255,255,.12);--code:#0F1B1A;--note:#12302F;color-scheme:dark;}}
:root[data-theme="dark"]{--bg:#10201F;--card:#172B2A;--ink:#EAF3F2;--muted:#A9BDBB;--pine:#9FD9DA;--teal:#5CC3C6;--ember:#FF9E61;--on-ember:#2B1304;--line:rgba(255,255,255,.12);--code:#0F1B1A;--note:#12302F;color-scheme:dark;}
*{box-sizing:border-box;}
body{background:var(--bg);color:var(--ink);font:16px/1.6 var(--body);}
main{max-width:860px;margin:0 auto;padding-block:36px 64px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:28px;}
h1{font-family:var(--display);font-weight:400;font-size:clamp(28px,5vw,38px);line-height:1.15;margin:0;color:var(--pine);text-wrap:balance;}
.intro{margin:8px 0 0;color:var(--muted);max-width:62ch;}
.first{background:var(--note);border-radius:18px;padding:18px 20px;display:grid;gap:6px;}
.first b{color:var(--pine);}
.first p{margin:0;}
.toc{display:flex;flex-wrap:wrap;gap:8px;}
.toc a{border:1.5px solid var(--line);border-radius:999px;padding:7px 14px;font-weight:800;font-size:14px;color:var(--pine);text-decoration:none;background:var(--card);}
.toc a:hover{border-color:var(--teal);}
.toc a:focus-visible,.copy:focus-visible{outline:3px solid var(--ember);outline-offset:2px;}
section{display:grid;gap:12px;scroll-margin-top:16px;}
.sh{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 14px;}
h2{font-family:var(--display);font-weight:400;font-size:24px;margin:0;color:var(--pine);}
.url{font-family:var(--mono);font-size:13px;color:var(--muted);}
.steps{margin:0;padding-left:22px;display:grid;gap:4px;color:var(--ink);}
.blk{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px;min-width:0;}
.bh{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:10px;}
h3{font-size:16px;margin:0;}
.bh p{margin:0;font-size:14px;color:var(--muted);}
.copy{font:inherit;font-weight:800;font-size:15px;border:0;border-radius:999px;padding:10px 18px;background:var(--ember);color:var(--on-ember);cursor:pointer;min-height:44px;}
.copy.ok{background:var(--teal);color:#fff;}
textarea{display:block;width:100%;height:96px;resize:vertical;border:1px solid var(--line);border-radius:10px;background:var(--code);color:var(--ink);font:12px/1.45 var(--mono);padding:10px;}
.tips{background:var(--card);border:1px dashed var(--line);border-radius:16px;padding:16px 20px;}
.tips h2{font-size:20px;margin-bottom:6px;}
.tips ul{margin:0;padding-left:20px;display:grid;gap:4px;}
</style>
<main>
<header><h1>Mettre le nouveau site en ligne</h1>
<p class="intro">Le nouveau site vit sur Netlify, à l’adresse oseprendretaplace.fr. www.oseprendretaplace.fr reste chez Systeme.io : paiements, remerciements, espace membre et blog continuent de marcher sans rien changer. Suis les étapes dans l’ordre.</p></header>
<div class="first"><p><b>Le principe :</b> le nouveau site est sur oseprendretaplace.fr. Les 3 anciennes pages du site Systeme.io (accueil, formations, contact) renvoient vers lui, et tout le reste ne bouge pas.</p><p>Le blog utilise des images hébergées avec le Winter Pack : garde bien le dernier ZIP du Winter Pack en ligne.</p></div>
<nav class="toc" aria-label="Pages">''' + nav + '''</nav>
''' + secs + '''
<div class="tips"><h2>Bon à savoir</h2><ul>
<li>Ne supprime pas tes anciennes pages Systeme.io : les pages de paiement et de remerciement doivent continuer d’exister.</li>
<li>Les animations et le pop-up ne s’affichent pas dans l’éditeur. Vérifie sur la page publiée, en navigation privée.</li>
<li>Pour revenir à l’ancien site à tout moment : retire le code d’en-tête des 3 pages Systeme.io.</li>
</ul></div>
</main>
<script>
[].forEach.call(document.querySelectorAll('.copy'), function(b){
  b.addEventListener('click', function(){
    var t = document.getElementById(b.getAttribute('data-t'));
    function done(){ b.textContent = 'Copié !'; b.classList.add('ok'); setTimeout(function(){ b.textContent = 'Copier le code'; b.classList.remove('ok'); }, 2200); }
    function fallback(){ t.focus(); t.select(); try { if (document.execCommand('copy')) { done(); return; } } catch (e) {} b.textContent = 'Texte sélectionné : Ctrl+C'; }
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t.value).then(done, fallback); else fallback();
  });
});
</script>
'''
open(OUT, 'w', encoding='utf-8').write(page)
print(len(page))
