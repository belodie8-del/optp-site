"""Test copy of the formations page: each offer is titled by the visitor's situation (B) and a "Par où commencer ?" block
sends each situation to its offer (C). Works on the built page, so the real page is left as it is."""
import sys
SRC = '/home/user/optp-site/site-ose/formations.html'
OUT = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/-home-user-optp-site/1386eaca-821b-50a5-926e-8bdc38c36a33/scratchpad/form/formations-formules-test.html'
s = open(SRC, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:70], s.count(a))
    s = s.replace(a, b)

POC = '''<section class="room mint" id="par-ou-commencer"><div class="wrap">
  <div class="ctr"><span class="hand">Trouve ta formule</span><h2 class="h2">Par où commencer ?</h2>
    <p class="sub">Choisis la phrase qui te ressemble le plus aujourd’hui.</p></div>
  <div class="poc">
    <a class="poc-c" href="#prise-de-poste"><span class="trk-k">Prise de poste</span>
      <p class="poc-q">« Je viens de prendre mon poste de manager, ou j’ai encore l’impression de faire semblant. »</p>
      <span class="poc-f"><b>Incarne ta posture</b><span>3 modules · 6 semaines · 897 €</span><span class="poc-a" aria-hidden="true">→</span></span></a>
    <a class="poc-c" href="#management-equipe"><span class="trk-k">Management d’équipe</span>
      <p class="poc-q">« Mon équipe n’avance pas comme je veux. Mes 1-to-1 et mes réunions ne servent à rien. »</p>
      <span class="poc-f"><b>Booste ton équipe</b><span>3 modules · 6 semaines · 897 €</span><span class="poc-a" aria-hidden="true">→</span></span></a>
    <a class="poc-c dark" href="#parcours-complet"><span class="trk-k">Parcours complet</span>
      <p class="poc-q">« Je veux reprendre tout mon management, ma posture comme mon équipe, et être accompagné·e pendant 12 semaines. »</p>
      <span class="poc-f"><b>Ose Prendre Ta Place</b><span>6 modules · 12 semaines · 1 497 €</span><span class="poc-a" aria-hidden="true">→</span></span></a>
  </div>
  <p class="poc-n">Tu hésites encore ? <a href="https://calendly.com/eb-formationconsulting/30min" target="_blank" rel="noopener">On en parle 30 minutes</a>, et je te dis quelle formule te correspond.</p>
</div></section>

'''
CSS = '''
/* formations: "Par où commencer ?" and offers titled by situation */
.poc{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;margin-top:44px;}
.poc-c{display:flex;flex-direction:column;gap:14px;padding:28px 26px 24px;border-radius:26px;background:var(--paper);border:2px solid var(--line);color:var(--ink);text-decoration:none;box-shadow:0 24px 40px -34px rgba(8,80,85,.6);transition:transform .2s ease,box-shadow .2s ease;}
.poc-c:hover{transform:translateY(-4px);box-shadow:0 30px 50px -30px rgba(8,80,85,.55);}
.poc-c:focus-visible{outline:3px solid var(--ember);outline-offset:3px;}
.poc-q{margin:0;font-family:var(--display);font-size:21px;line-height:1.32;color:var(--pine);}
.poc-f{margin-top:auto;padding-top:16px;border-top:1.5px dashed var(--line);display:grid;grid-template-columns:minmax(0,1fr) auto;gap:2px 12px;align-items:center;}
.poc-f b{grid-column:1;font-weight:800;color:var(--ink);}
.poc-f span:not(.poc-a){grid-column:1;font-size:14.5px;color:var(--muted);}
.poc-a{grid-column:2;grid-row:1 / span 2;width:42px;height:42px;border-radius:50%;display:grid;place-items:center;background:var(--ember);color:#2B1304;font-weight:800;font-size:18px;}
.poc-c.dark{background:var(--pine);border-color:var(--pine);}
.poc-c.dark .trk-k{color:var(--ember);}
.poc-c.dark .poc-q,.poc-c.dark .poc-f b{color:#fff;}
.poc-c.dark .poc-f{border-top-color:rgba(255,255,255,.25);}
.poc-c.dark .poc-f span:not(.poc-a){color:var(--on-pine-soft);}
.poc-n{margin:32px auto 0;text-align:center;color:var(--muted);font-size:16.5px;max-width:60ch;}
.poc-n a{color:var(--teal);font-weight:800;}
.pk-n{margin:-8px 0 0;font-family:var(--hand);font-size:28px;line-height:1;color:var(--ember-ink);}
.oc h3.oc-t{margin-bottom:4px;}
.oc-n{margin:0 0 14px;font-family:var(--hand);font-size:32px;line-height:1;color:var(--ember);}
.oc-w{margin:0 0 22px;font-weight:700;color:var(--on-pine-soft);}
#prise-de-poste,#management-equipe,#parcours-complet{scroll-margin-top:110px;}
@media (max-width:860px){.poc{grid-template-columns:minmax(0,1fr);}}
'''
# C: the chooser, just before the offers; the hero button leads to it
rep('<section class="room" id="offres">', POC + '<section class="room" id="offres">')
rep('href="#offres">Découvrir les formules', 'href="#par-ou-commencer">Découvrir les formules')
# B: situation as the title, the offer's own name just under it
rep('<article class="oc"><div class="oc-a"><span class="trk-k">Ose Prendre Ta Place</span><h3>C’est la transformation complète !</h3>',
    '<article class="oc" id="parcours-complet"><div class="oc-a"><span class="trk-k">6 modules · 12 semaines</span><h3 class="oc-t">Parcours complet</h3>'
    '<p class="oc-n">Ose Prendre Ta Place</p><p class="oc-w">Pour toi si tu veux reprendre tout ton management, ta posture comme ton équipe. C’est la transformation complète !</p>')
rep('<article class="pk"><span class="trk-k">3 modules</span><h3>Incarne ta posture</h3><p class="pk-w">Construire ta posture de manager.</p>',
    '<article class="pk" id="prise-de-poste"><span class="trk-k">3 modules · 6 semaines</span><h3>Prise de poste</h3><p class="pk-n">Incarne ta posture</p>'
    '<p class="pk-w">Pour toi si tu viens de prendre ton poste de manager, ou si tu as encore l’impression de faire semblant.</p>')
rep('<article class="pk"><span class="trk-k">3 modules</span><h3>Booste ton équipe</h3><p class="pk-w">Agir concrètement sur ton management individuel et collectif.</p>',
    '<article class="pk" id="management-equipe"><span class="trk-k">3 modules · 6 semaines</span><h3>Management d’équipe</h3><p class="pk-n">Booste ton équipe</p>'
    '<p class="pk-w">Pour toi si ton équipe n’avance pas comme tu veux, et que tes 1-to-1 et tes réunions ne servent à rien.</p>')
# "pack" is the Winter Pack's word: the 3-module offers are "parcours", as on the home page
for a, b in [('les deux packs et Ose', 'les deux parcours de 3 modules et Ose'),
             ('Un pack, c’est 3 modules sur un sujet précis.', 'Un parcours, c’est 3 modules sur un sujet précis.'),
             ('Avec un pack, tu as', 'Avec un parcours de 3 modules, tu as'),
             ('Un pack te donne', 'Un parcours de 3 modules te donne'),
             ('Comment fonctionne un pack ?', 'Comment fonctionne un parcours de 3 modules ?'),
             ('de suivre un pack sur 6 semaines', 'de suivre un parcours de 3 modules sur 6 semaines')]:
    rep(a, b)
rep('Les packs et Ose Prendre Ta Place', 'Les parcours de 3 modules et Ose Prendre Ta Place', 2)
i = s.index('</style>')
s = s[:i] + CSS + s[i:]
rep('<title>Les formations · Ose prendre ta place</title>', '<title>Formations · test formules</title>')
open(OUT, 'w', encoding='utf-8').write(s)
print('ok', OUT)
