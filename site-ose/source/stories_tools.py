# one story per Winter Pack tool (texts from the Winter Pack page), inserted after the Winter Pack intro story
TD = [
 ('L’entretien de parcours professionnel', 'Un collaborateur qui ne se voit pas d’avenir chez toi finit par le chercher ailleurs.', 'PDF · à imprimer ou à remplir',
  [('Le cadre légal intégré', 'La trame rappelle ce que la loi impose, de l’accueil aux signatures.'), ('Un plan d’actions daté', 'Des actions concrètes, avec un point d’étape à 6 mois.')]),
 ('L’entretien annuel', 'L’entretien annuel évalue aussi le manager.', 'PDF · à imprimer ou à remplir',
  [('Deux regards comparés', 'Manager et collaborateur remplissent chacun leur exemplaire.'), ('Le management évalué aussi', 'Le collaborateur donne son avis sur son manager.')]),
 ('La réunion d’équipe', 'Une équipe qui ne sait pas ce qui compte ce mois-ci travaille sur tout, donc sur rien.', 'Notion',
  [('Des phrases pour ouvrir', 'Pour lancer la réunion et donner la parole à chacun.'), ('3 priorités pour le mois', 'Chaque réunion se termine sur un « qui fait quoi pour quand ».')]),
 ('La trame du OTO', 'Ce qu’un collaborateur ne dit pas en réunion, il le dit en tête-à-tête.', 'Notion',
  [('Les questions prêtes à poser', 'Pour chaque étape, les bonnes questions pour le faire parler.'), ('80 % de parole au collaborateur', 'C’est son moment, avec ses propres sujets.')]),
 ('Le tableau de bord des objectifs', 'Un objectif qu’on regarde une fois par an, c’est un vœu pieux.', 'Excel',
  [('Un onglet par collaborateur', 'Tous les objectifs de l’équipe au même endroit.'), ('Le suivi en un coup d’œil', 'Qui avance, et qui a besoin du manager.')]),
 ('Le calendrier des rituels', 'Le management ne s’improvise pas entre deux urgences.', 'Notion · Outlook et Gmail',
  [('Directement dans ton agenda', 'Le calendrier se transfère dans ton agenda, avec l’IA.'), ('Une idée pour chaque fête', 'Des activités à vivre avec ton équipe.')]),
 ('Les 10 commandements', 'Le document ne fait pas l’entretien, c’est le manager.', 'PDF',
  [('Tout tient sur une page', 'À relire en 2 minutes, juste avant l’entretien.'), ('Chaque commandement expliqué', 'Quoi faire, et pourquoi ça marche.')]),
 ('Le kit de survie verbal', 'Quand le manager intervient enfin, c’est trop tard : chacun a déjà pris position.', 'Notion',
  [('Les mots exacts', 'Pour chaque étape du conflit, la phrase à dire, mot pour mot.'), ('Le pourquoi de chaque phrase', 'Pour comprendre l’effet de ses mots et les adapter.')]),
]
_pos = [i for i, x in enumerate(ST) if x[0] == 'winter-1'][0] + 1
for k, (name, hook, fmt, pts) in enumerate(TD):
    body = (' <p class="hand">Winter Pack · outil %d/8</p>\n <h1 class="tn%s">%s</h1>\n <p class="hk">« %s »</p>\n'
            ' <div class="pv"><img src="wpap/t%d.jpg" alt=""><span class="fm">%s</span></div>\n <div class="pts">%s</div>') % (
        k + 1, ' long' if len(name) > 32 else '', name, hook, k + 1, fmt,
        ''.join('<div class="pt"><span class="ck2">✓</span><div><b>%s</b><span>%s</span></div></div>' % p for p in pts))
    ST.insert(_pos + k, ('outil-%d' % (k + 1), 'mint' if k % 2 else 'peach', body))
CSS_T = '''.tn{font-size:40px}
.tn.long{font-size:35px}
.hk{margin-top:8px;font-size:18px;line-height:1.4;font-weight:700;font-style:italic;color:var(--teal);max-width:32ch}
.pv{position:relative;margin-top:18px;width:100%;height:262px;background:#fff;border-radius:22px;padding:14px;box-shadow:0 30px 46px -32px rgba(8,80,85,.75);transform:rotate(-1.5deg);display:grid;place-items:center}
.pv img{max-width:100%;max-height:236px;object-fit:contain;border-radius:8px}
.fm{position:absolute;right:-8px;bottom:-14px;background:var(--pine);color:#fff;font-weight:800;font-size:15px;padding:8px 14px;border-radius:999px;transform:rotate(4deg);box-shadow:0 10px 18px -10px rgba(8,40,43,.7)}
.pts{margin-top:24px;width:100%;display:grid;gap:10px;text-align:left}
.pt{display:flex;gap:14px;align-items:flex-start;background:#fff;border-radius:18px;padding:12px 16px}
.ck2{flex:none;display:grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--ember);color:#2B1304;font-weight:800;font-size:16px;margin-top:2px}
.pt b{display:block;font-family:'Young Serif';font-weight:400;font-size:20px;color:var(--pine);line-height:1.2}
.pt span:not(.ck2){display:block;font-size:15px;line-height:1.35;color:var(--muted);margin-top:2px}
'''
