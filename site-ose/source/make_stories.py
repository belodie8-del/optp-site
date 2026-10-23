"""Instagram stories (1080x1920) announcing the new site and the Winter Pack, in the site's style."""
exec(open('_pre.py', encoding='utf-8').read())
LOGO = '<svg class="lg" viewBox="0 0 287 90" aria-label="EB Formation Consulting"><use href="#optplogo"/></svg>'
LOGOW = '<svg class="lg lgw" viewBox="0 0 287 90" aria-label="EB Formation Consulting"><use href="#optplogo"/></svg>'
SNOW = ''.join('<i class="sn" style="left:%d%%;top:%d%%;font-size:%dpx;opacity:%.2f">❄</i>' % f for f in
               [(8, 9, 26, .35), (86, 7, 34, .3), (70, 20, 18, .25), (12, 40, 16, .22), (92, 46, 22, .28), (6, 70, 30, .25), (80, 78, 18, .3), (45, 6, 14, .25)])
def phone(src, cls=''):
    return '<div class="ph %s"><div class="ph-s"><img src="%s" alt=""></div></div>' % (cls, src)
def tick(t): return '<li><span class="ck">✓</span>%s</li>' % t
TOOLS = ['L’entretien professionnel', 'L’entretien annuel', 'La réunion d’équipe', 'La trame du OTO',
         'Le tableau de bord des objectifs', 'Le calendrier des rituels', 'Les 10 commandements', 'Le kit de survie verbal']
ST = [
('site-1', 'pine', '''<div class="top">''' + LOGOW + '''</div>
 <p class="hand o">Ça y est !</p>
 <h1 class="w">Mon nouveau site est <em>en ligne</em></h1>
 ''' + phone('../stories/m-site.jpg', 'big') + '''
 <span class="stk" style="right:52px;top:560px">Nouveau ✨</span>
 <p class="url w">www.oseprendretaplace.fr</p>'''),
('site-2', 'peach', '''<div class="top">''' + LOGO + '''</div>
 <p class="hand">Ce que tu vas y trouver</p>
 <h1>Tout pour oser prendre ta place de manager</h1>
 <div class="cards">
  <div class="cd"><span class="n">1</span><div><b>Mes formations</b><span>Ose Prendre Ta Place, Incarne ta posture, Booste ton équipe</span></div></div>
  <div class="cd"><span class="n">2</span><div><b>L’audit offert</b><span>Ton profil managérial en 3 minutes</span></div></div>
  <div class="cd"><span class="n">3</span><div><b>Le blog « OSE »</b><span>Le management, version terrain. Un nouvel article chaque semaine</span></div></div>
  <div class="cd wp"><span class="n">4</span><div><b>❄ Le Winter Pack</b><span>8 outils pour mener tes entretiens</span></div></div>
 </div>
 <p class="hand foot">Tout est au même endroit 💚</p>'''),
('site-3', 'mint', '''<div class="top">''' + LOGO + '''</div>
 <h1>Viens faire un tour</h1>
 <p class="sub">Les formations, l’audit offert, le blog et le Winter Pack, réunis sur un seul site.</p>
 ''' + phone('../stories/m-site-form.jpg', 'mid') + '''
 <p class="hand lk">Le lien est juste ici 👇</p>
 <div class="spot"></div>'''),
('winter-1', 'pine snow', SNOW + '''<div class="top">''' + LOGOW + '''</div>
 <p class="hand o">Nouveau · Winter Pack</p>
 <h1 class="w">L’hiver arrive. <em>Prépare tes managers.</em></h1>
 <p class="sub w">L’Essentiel du Manager : 8 outils pour que tes managers mènent leurs entretiens avec la même méthode.</p>
 <div class="fan"><img class="d1" src="wpap/s2.jpg" alt=""><img class="d2" src="wpap/s7.jpg" alt=""><img class="d3" src="wpap/s1.jpg" alt=""></div>
 <span class="stk big" style="right:30px;bottom:150px"><b>8</b>outils prêts<br>à l’emploi</span>'''),
('winter-2', 'white', '''<div class="top">''' + LOGO + '''</div>
 <p class="hand">Winter Pack · L’Essentiel du Manager</p>
 <h1>8 outils pour manager toute l’année</h1>
 <ol class="tl">''' + ''.join('<li><span class="n">%d</span>%s</li>' % (i + 1, t) for i, t in enumerate(TOOLS)) + '''</ol>
 <p class="fmt">En PDF, sur Notion et sur Excel, prêts à l’emploi</p>'''),
('winter-3', 'peach', '''<div class="top">''' + LOGO + '''</div>
 <p class="hand">Pour toi, ou pour toute ta PME</p>
 <h1>Choisis ton Winter Pack</h1>
 <div class="offs">
  <div class="of"><small>Pour un manager</small><b>Winter Pack Solo</b><em>197 €</em></div>
  <div class="of pme"><small>Pour toute ta PME</small><b>Winter Pack PME</b><em>dès 490 €</em></div>
 </div>
 <div class="gift">🎁 <span><b>Cadeau de lancement :</b> le kit d’invitation à l’entretien offert pour tout achat avant dimanche</span></div>
 <p class="hand lk">Le lien est juste ici 👇</p>
 <div class="spot"></div>'''),
]
CSS = '''<style>
:root{--pine:#085055;--teal:#0F868A;--ember:#FF914D;--ink-e:#B4561F;--peach:#FFF4EE;--peach2:#FFE7D8;--mint:#E4F5F6;--ink:#1D2A28;--muted:#5A6663}
*{box-sizing:border-box;margin:0}
body{background:#999;padding:20px;display:flex;flex-wrap:wrap;gap:20px;font-family:'Nunito Sans',sans-serif;color:var(--ink)}
.st{position:relative;width:540px;height:960px;overflow:hidden;padding:182px 44px 0;display:flex;flex-direction:column;align-items:center;text-align:center}
.st.pine{background:radial-gradient(circle at 85% 12%,#0F6A6E 0,var(--pine) 46%)}.st.peach{background:var(--peach)}.st.mint{background:var(--mint)}.st.white{background:#fff}
.sn{position:absolute;font-style:normal;color:#fff;line-height:1}
.top{position:absolute;top:122px;left:0;right:0;display:flex;justify-content:center}
.lg{width:128px;height:40px}
.lgw{filter:brightness(0) invert(1)}
.hand{font-family:'Caveat',cursive;font-weight:700;font-size:34px;line-height:1.1;color:var(--ink-e);transform:rotate(-2deg)}
.hand.o{color:var(--ember)}
h1{font-family:'Young Serif',Georgia,serif;font-weight:400;font-size:46px;line-height:1.08;color:var(--pine);margin-top:8px;text-wrap:balance}
h1 em{font-style:normal;color:var(--ember)}
.w{color:#fff}
h1.w em{color:var(--ember)}
.sub{margin-top:12px;font-size:19px;line-height:1.45;color:var(--muted);max-width:30ch}
.sub.w{color:rgba(255,255,255,.85)}
.ph{position:relative;background:#1b1b1b;border-radius:42px;padding:11px;box-shadow:0 40px 60px -30px rgba(0,0,0,.6)}
.ph-s{border-radius:32px;overflow:hidden}
.ph img{display:block;width:100%}
.ph.big{width:262px;margin-top:22px;transform:rotate(-3deg)}.ph.big .ph-s{height:360px}
.ph.mid{width:240px;margin-top:20px;transform:rotate(3deg)}.ph.mid .ph-s{height:310px}
.stk{position:absolute;z-index:3;background:#FFF1C9;color:var(--ink);font-family:'Caveat';font-weight:700;font-size:30px;padding:10px 20px;border-radius:8px 8px 22px 8px;transform:rotate(6deg);box-shadow:0 18px 28px -14px rgba(0,0,0,.5)}
.stk.big{display:flex;flex-direction:column;align-items:center;justify-content:center;width:140px;height:140px;border-radius:50%;background:var(--ember);color:#2B1304;font-family:'Nunito Sans';font-weight:800;font-size:19px;line-height:1.2;padding:0}
.stk.big b{font-family:'Young Serif';font-weight:400;font-size:50px;line-height:1}
.url{margin-top:22px;font-weight:800;font-size:23px;letter-spacing:.02em}
.cards{margin-top:22px;width:100%;display:grid;gap:12px;text-align:left}
.cd{display:flex;gap:16px;align-items:center;background:#fff;border-radius:22px;padding:13px 18px;box-shadow:0 20px 34px -26px rgba(8,80,85,.6)}
.cd .n,.tl .n{flex:none;display:grid;place-items:center;width:46px;height:46px;border-radius:50%;background:var(--ember);color:#2B1304;font-family:'Young Serif';font-size:26px}
.cd b{display:block;font-family:'Young Serif';font-weight:400;font-size:23px;color:var(--pine);line-height:1.15}
.cd span:not(.n){display:block;font-size:15px;line-height:1.35;color:var(--muted);margin-top:3px}
.cd.wp{background:var(--pine)}.cd.wp b{color:#fff}.cd.wp span:not(.n){color:rgba(255,255,255,.8)}.cd.wp .n{background:#fff;color:var(--pine)}
.foot{margin-top:18px;font-size:30px}
.lk{margin-top:16px;font-size:36px;color:var(--ink-e)}
.spot{height:120px}
.fan{position:relative;width:420px;height:300px;margin-top:22px}
.fan img{position:absolute;width:190px;border-radius:14px;border:6px solid #fff;box-shadow:0 30px 44px -26px rgba(0,0,0,.7)}
.fan .d1{left:0;top:40px;transform:rotate(-9deg)}.fan .d2{right:0;top:30px;transform:rotate(8deg)}.fan .d3{left:50%;top:0;transform:translateX(-50%) rotate(-1deg);z-index:2}
.tl{list-style:none;padding:0;margin-top:20px;width:100%;display:grid;gap:7px;text-align:left}
.tl li{display:flex;align-items:center;gap:14px;background:var(--mint);border-radius:16px;padding:5px 14px;font-weight:800;font-size:18px;color:var(--pine)}
.tl .n{width:34px;height:34px;font-size:18px}
.fmt{margin-top:10px;font-size:16px;font-weight:700;color:var(--muted)}
.offs{margin-top:22px;width:100%;display:grid;gap:16px}
.of{background:#fff;border:2.5px solid #CDE9EB;border-radius:24px;padding:16px 22px;text-align:left;display:grid;gap:2px}
.of small{font-size:15px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.of b{font-family:'Young Serif';font-weight:400;font-size:32px;color:var(--pine)}
.of em{font-style:normal;font-weight:800;font-size:28px;color:var(--ink-e)}
.of.pme{background:var(--pine);border-color:var(--pine)}.of.pme small{color:rgba(255,255,255,.75)}.of.pme b{color:#fff}.of.pme em{color:var(--ember)}
.gift{margin-top:14px;display:flex;gap:12px;align-items:flex-start;text-align:left;background:#fff;border:2.5px dashed var(--ember);border-radius:20px;padding:16px 18px;font-size:18px;line-height:1.4}
.gift b{color:var(--ink-e)}
</style>'''
html = '<!doctype html><meta charset="utf-8">' + CSS + ''.join('<div class="st %s" id="%s">%s</div>' % (cls, sid, body) for sid, cls, body in ST) + defs
open(S + 'home/stories.html', 'w', encoding='utf-8').write(html)
print('ok', [s[0] for s in ST])
