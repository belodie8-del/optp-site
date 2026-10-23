"""Page to install the image signature: preview, copy of the clickable buttons, Gmail steps."""
import base64
D = lambda f: 'data:image/png;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
FORM = 'https://www.oseprendretaplace.fr/formations'
WP = 'https://winterpack.oseprendretaplace.fr/'
LI = 'https://www.linkedin.com/in/elodie-boyer-299891143/'
IG = 'https://www.instagram.com/elodie_boyer_off_management/'
def pill(href, txt, bg, fg):
    return ('<td style="background:%s;border-radius:16px;padding:7px 15px;"><a href="%s" style="font-family:Arial,Helvetica,sans-serif;font-size:13px;font-weight:bold;color:%s;text-decoration:none;white-space:nowrap;">%s</a></td>' % (bg, href, fg, txt))
SOCIAL = ('<td style="padding-left:14px;font-family:Arial,Helvetica,sans-serif;font-size:13px;white-space:nowrap;"><a href="%s" style="color:#0F868A;font-weight:bold;text-decoration:none;">LinkedIn</a>'
          '&nbsp;·&nbsp;<a href="%s" style="color:#0F868A;font-weight:bold;text-decoration:none;">Instagram</a></td>' % (LI, IG))
ROW = ('<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;margin-top:8px;"><tr>' + pill(FORM, 'Mes formations&nbsp;→', '#FF914D', '#2B1304')
       + '<td style="width:8px;"></td>' + pill(WP, '❄ Le Winter Pack&nbsp;→', '#085055', '#FFFFFF') + SOCIAL + '</tr></table>')
BAND = ('<table cellpadding="0" cellspacing="0" border="0" width="600" style="border-collapse:collapse;margin-top:6px;width:600px;"><tr>'
        '<td style="background:#085055;border-radius:14px;padding:11px 20px;font-family:Arial,Helvetica,sans-serif;color:#FFFFFF;">'
        '<a href="%s" style="color:#FFFFFF;text-decoration:none;"><span style="font-size:15px;font-weight:bold;">❄ Nouveau · Le Winter Pack</span>'
        '<span style="font-size:13px;">&nbsp;&nbsp;8 outils pour mener tes entretiens&nbsp;&nbsp;</span>'
        '<span style="font-size:13px;font-weight:bold;color:#FF914D;">Découvrir&nbsp;→</span></a></td></tr></table>'
        '<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;margin-top:8px;"><tr>' + pill(FORM, 'Mes formations&nbsp;→', '#FF914D', '#2B1304') + SOCIAL + '</tr></table>') % WP
VERS = [('1', 'Le bandeau vert', ROW), ('2', 'La carte pêche', ROW), ('3', 'La blanche épurée', BAND)]
secs = ''
for n, name, row in VERS:
    secs += ('<section id="v%s"><div class="sh"><h2>Version %s · %s</h2><span>Image : signature-mail-%s.png</span></div>'
             '<div class="mail"><img class="pv" src="%s" alt="Signature version %s" width="600"><div class="row" id="r%s">%s</div></div>'
             '<button type="button" class="copy" data-r="r%s">Copier les boutons cliquables</button></section>') % (n, n, name, n, D('signature-mail-%s.png' % n), n, n, row, n)
page = '''<title>Signature mail Élodie</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>
:root{--bg:#FFF4EE;--card:#FFFFFF;--ink:#1D2A28;--muted:#5A6663;--pine:#085055;--ember:#FF914D;--on-ember:#2B1304;--line:rgba(8,80,85,.14);--note:#E4F5F6}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#10201F;--card:#172B2A;--ink:#EAF3F2;--muted:#A9BDBB;--pine:#9FD9DA;--ember:#FF9E61;--line:rgba(255,255,255,.12);--note:#12302F;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#10201F;--card:#172B2A;--ink:#EAF3F2;--muted:#A9BDBB;--pine:#9FD9DA;--ember:#FF9E61;--line:rgba(255,255,255,.12);--note:#12302F;color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,'Segoe UI',sans-serif}
main{max-width:760px;margin:0 auto;padding-block:32px 56px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:26px}
h1{font-family:Georgia,serif;font-weight:400;font-size:clamp(26px,5vw,34px);margin:0;color:var(--pine)}
.intro{margin:4px 0 0;color:var(--muted)}
.toc{display:flex;flex-wrap:wrap;gap:8px}.toc a{border:1.5px solid var(--line);border-radius:999px;padding:7px 14px;font-weight:800;font-size:14px;color:var(--pine);text-decoration:none;background:var(--card)}
section{display:grid;gap:12px;min-width:0}
header,nav,.mail{min-width:0}
.sh{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 14px}.sh h2{font-family:Georgia,serif;font-weight:400;font-size:22px;margin:0;color:var(--pine)}.sh span{font-size:13px;color:var(--muted)}
.mail{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;overflow-x:auto}
.pv{display:block;width:600px;max-width:none;height:auto}
.copy{justify-self:start;font:inherit;font-weight:800;border:0;border-radius:999px;padding:12px 20px;min-height:44px;cursor:pointer;background:var(--ember);color:var(--on-ember)}
.copy.ok{background:var(--pine);color:#fff}
.copy:focus-visible,.toc a:focus-visible{outline:3px solid var(--pine);outline-offset:2px}
.steps{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 22px}
.steps h2{font-family:Georgia,serif;font-weight:400;font-size:21px;margin:0 0 8px;color:var(--pine)}
.steps ol{margin:0;padding-left:20px;display:grid;gap:6px}
.tip{background:var(--note);border-radius:14px;padding:14px 18px;font-size:15px;margin:0}
</style>
<main>
<header><h1>Ta signature de mail</h1><p class="intro">3 versions au choix. Chacune se compose d’une image (envoyée dans la conversation) et d’une ligne de boutons cliquables à copier ici.</p></header>
<nav class="toc" aria-label="Versions"><a href="#v1">Version 1</a><a href="#v2">Version 2</a><a href="#v3">Version 3</a><a href="#gmail">Installer dans Gmail</a></nav>
''' + secs + '''
<section class="steps" id="gmail"><h2>Installer dans Gmail</h2><ol>
<li>Enregistre sur ton ordinateur l’image de la version choisie (signature-mail-1, 2 ou 3.png).</li>
<li>Gmail : roue crantée → « Voir tous les paramètres » → onglet « Général » → « Signature » → « Créer », puis donne-lui un nom.</li>
<li>Dans la case de la signature, clique sur l’icône « Insérer une image » → « Importer » et choisis l’image.</li>
<li>Clique sur l’image : choisis la taille (« Moyenne » en général, pour qu’elle fasse à peu près la largeur d’un paragraphe).</li>
<li>Image toujours sélectionnée, clique sur l’icône « Lien » et colle <b>https://www.oseprendretaplace.fr</b>.</li>
<li>Place le curseur juste après l’image, appuie sur Entrée, puis colle les boutons copiés sur cette page (Ctrl+V, ou Cmd+V sur Mac).</li>
<li>Choisis cette signature pour les nouveaux e-mails et les réponses, puis « Enregistrer les modifications » tout en bas de la page.</li></ol></section>
<p class="tip">Envoie-toi un e-mail de test : clique sur l’image (ton site), puis sur chaque bouton, pour vérifier que tout s’ouvre bien.</p>
</main>
<script>
[].forEach.call(document.querySelectorAll('.copy'),function(b){b.addEventListener('click',function(){
  var el=document.getElementById(b.getAttribute('data-r'));
  function done(){b.textContent='Copié !';b.classList.add('ok');setTimeout(function(){b.textContent='Copier les boutons cliquables';b.classList.remove('ok');},2200);}
  function fallback(){try{var r=document.createRange();r.selectNodeContents(el);var s=getSelection();s.removeAllRanges();s.addRange(r);if(document.execCommand('copy')){done();return;}}catch(e){}b.textContent='Sélectionnés : fais Ctrl+C';}
  try{if(window.ClipboardItem&&navigator.clipboard&&navigator.clipboard.write){navigator.clipboard.write([new ClipboardItem({'text/html':new Blob([el.innerHTML],{type:'text/html'}),'text/plain':new Blob([el.innerText],{type:'text/plain'})})]).then(done,fallback);}else fallback();}catch(e){fallback();}
});});
</script>
'''
open('signature.html', 'w', encoding='utf-8').write(page)
print(len(page))
