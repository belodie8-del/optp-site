"""Page listing the Systeme.io blocks of the new oseprendretaplace.fr site, with copy buttons and the steps per page."""
import html
D = '/home/user/optp-site/site-ose/systemeio/'
OUT = '/tmp/claude-0/-home-user-optp-site/1386eaca-821b-50a5-926e-8bdc38c36a33/scratchpad/home/codes-site-ose.html'
PAGES = [
 ('systeme', '1 · Préparer Systeme.io', 'espace.oseprendretaplace.fr',
  ['Dans Systeme.io, ajoute le domaine <b>espace.oseprendretaplace.fr</b> (Paramètres → Domaines personnalisés). Crée chez OVH l’enregistrement DNS que Systeme.io t’indique.',
   'Dans les réglages de chaque tunnel (paiements, remerciements, Winter Pack, cartable de rentrée, sprint…) et de l’espace membre, choisis le domaine espace.oseprendretaplace.fr.',
   'Vérifie que <b>espace.oseprendretaplace.fr/paiement-ose</b> s’ouvre bien. Ne passe pas à l’étape 3 avant : sinon les paiements ne fonctionneront plus.'],
  []),
 ('netlify', '2 · Mettre le site sur Netlify', 'site-ose-netlify.zip',
  ['Sur Netlify : Add new site → Deploy manually, puis glisse le fichier <b>site-ose-netlify.zip</b>.',
   'Dans Forms, clique sur « Enable form detection », puis redépose le même ZIP (c’est ce qui active le formulaire de contact).',
   'Dans Forms → Form notifications, ajoute une notification e-mail vers contact@oseprendretaplace.fr.',
   'Teste le site sur l’adresse provisoire xxx.netlify.app que Netlify te donne.'],
  []),
 ('domaine', '3 · Brancher www.oseprendretaplace.fr', 'chez OVH',
  ['Dans Netlify : Domain management → Add a domain → www.oseprendretaplace.fr.',
   'Dans Systeme.io, retire www.oseprendretaplace.fr de tes domaines personnalisés.',
   'Chez OVH, remplace la cible de l’enregistrement CNAME de « www » par l’adresse que Netlify affiche (xxx.netlify.app).',
   'Attends que le changement se propage (de quelques minutes à quelques heures). Netlify active le HTTPS tout seul.',
   'Teste : www.oseprendretaplace.fr/paiement-ose doit t’emmener sur la page de paiement, sur espace.oseprendretaplace.fr.'],
  []),
 ('blog', '4 · Le blog (reste sur Systeme.io)', 'oseprendretaplace.systeme.io/leblogose',
  ['Ouvre la mise en page du blog et garde l’élément « liste des articles » : il se met à jour seul.',
   'Supprime les autres sections. Au-dessus de la liste, ajoute un élément « Code HTML » avec le bloc 1.',
   'Sous la liste, ajoute un second élément « Code HTML » avec le bloc 2.'],
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
<p class="intro">Le site est hébergé sur Netlify. Toutes les adresses restent les mêmes : ce qui n’est pas une page du nouveau site (paiements, remerciements, espace membre…) est renvoyé automatiquement vers Systeme.io. Suis les étapes dans l’ordre.</p></header>
<div class="first"><p><b>Pourquoi l’étape 1 d’abord :</b> une adresse ne peut pointer que vers un seul hébergeur. Quand www passera sur Netlify, tes pages Systeme.io vivront sur espace.oseprendretaplace.fr, et Netlify y renverra tous les anciens liens.</p><p>Le blog utilise des images hébergées avec le Winter Pack : garde bien le dernier ZIP du Winter Pack en ligne.</p></div>
<nav class="toc" aria-label="Pages">''' + nav + '''</nav>
''' + secs + '''
<div class="tips"><h2>Bon à savoir</h2><ul>
<li>Ne supprime pas tes anciennes pages Systeme.io : les pages de paiement et de remerciement doivent continuer d’exister.</li>
<li>Les animations et le pop-up ne s’affichent pas dans l’éditeur. Vérifie sur la page publiée, en navigation privée.</li>
<li>Pour changer le nom espace.oseprendretaplace.fr, dis-le-moi avant l’étape 1 : je régénère le ZIP en 1 minute.</li>
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
