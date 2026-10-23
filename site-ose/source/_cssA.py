CSS_A = '''<style>
/* header: plain white, orange CTA */
.hx .nav .rdvbtn{padding:11px 22px;}
/* hero: pine block, arch photo */
.h2o{background:var(--pine);color:#fff;overflow:hidden;position:relative;}
.h2o::before{content:"";position:absolute;right:-120px;top:-140px;width:520px;height:520px;border-radius:50%;background:rgba(255,255,255,.05);}
.h2o > .wrap:first-child{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:56px;align-items:end;padding-block:72px 40px;position:relative;}
.h2o .hand{color:var(--ember);}
.h2o h1{font-family:var(--display);font-weight:400;font-size:clamp(46px,6.4vw,84px);line-height:1;margin:10px 0 22px;color:#fff;}
.h2o h1 em{font-style:normal;color:var(--ember);position:relative;display:inline-block;white-space:nowrap;}
.h2o h1 em svg{position:absolute;left:0;right:0;bottom:-12px;width:100%;height:18px;}
.h2o h1 em path{fill:none;stroke:#FFCFA3;stroke-width:6;stroke-linecap:round;}
.h2o .lede{color:var(--on-pine-soft);font-size:19px;max-width:52ch;}
.h2o .ctas{margin-top:30px;}
.btn.ghost{background:transparent;color:#fff;border:2px solid rgba(255,255,255,.6);box-shadow:none;}
.btn.ghost:hover{background:rgba(255,255,255,.1);color:#fff;}
.h2o-v{position:relative;justify-self:center;width:min(100%,360px);}
.arch{border-radius:190px 190px 28px 28px;overflow:hidden;background:var(--ember);aspect-ratio:420/540;border:8px solid rgba(255,255,255,.12);}
.arch img{display:block;width:100%;height:100%;object-fit:cover;object-position:center top;}
.tag{position:absolute;left:-56px;bottom:46px;background:#FFF1C9;color:var(--ink);padding:14px 20px;border-radius:6px 6px 18px 6px;font-family:var(--hand);font-size:25px;line-height:1.1;transform:rotate(-4deg);box-shadow:0 18px 30px -16px rgba(0,0,0,.5);}
.tag b{color:var(--ember-ink);font-weight:700;}
.h2o-s{list-style:none;margin:0;padding:26px 0 34px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;border-top:1.5px dashed rgba(255,255,255,.22);}
.h2o-s li{display:flex;flex-direction:column;gap:4px;}
.h2o-s b{font-family:var(--display);font-weight:400;font-size:clamp(30px,3.4vw,42px);line-height:1;color:#FFCFA3;}
.h2o-s span{font-size:14.5px;color:var(--on-pine-soft);font-weight:700;}
/* moment: chat bubbles */
.mo{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:56px;align-items:start;}
.mo-me{display:flex;align-items:center;gap:14px;margin-top:26px;font-family:var(--hand);font-size:23px;line-height:1.15;color:var(--pine);}
.mo-me img{width:56px;height:56px;border-radius:50%;object-fit:cover;flex:none;}
.chatlist{display:flex;flex-direction:column;gap:14px;}
.bub{margin:0;max-width:88%;padding:16px 20px;background:var(--peach);border-radius:22px 22px 22px 6px;font-size:16.5px;line-height:1.45;color:var(--ink);box-shadow:0 10px 22px -18px rgba(29,42,40,.6);}
.bub.r{align-self:flex-end;background:var(--mint);border-radius:22px 22px 6px 22px;color:var(--pine);}
/* audit: split card with steps */
.aud{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:40px;align-items:center;background:#fff;border-radius:34px;padding:clamp(28px,4vw,52px);box-shadow:0 30px 60px -40px rgba(8,80,85,.6);}
.aud-t .btn{margin-top:22px;}
.aud-s{list-style:none;margin:0;padding:0;display:grid;gap:14px;counter-reset:a;}
.aud-s li{display:flex;gap:16px;align-items:flex-start;padding:18px 20px;border-radius:20px;background:var(--peach);}
.aud-s li:nth-child(2){background:#FFF1C9;} .aud-s li:nth-child(3){background:var(--peach2);}
.aud-s li > span{flex:none;display:grid;place-items:center;width:40px;height:40px;border-radius:50%;background:var(--ember);color:#fff;font-family:var(--display);font-size:20px;}
.aud-s b{display:block;font-family:var(--display);font-weight:400;font-size:22px;color:var(--ink);}
.aud-s div{font-size:15px;color:var(--muted);line-height:1.4;}
/* formations: the equation */
.eq{display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr) auto minmax(0,1.25fr);gap:14px;align-items:center;margin-top:40px;}
.eq-op{align-self:center;display:grid;place-items:center;width:50px;height:50px;border-radius:50%;background:var(--mint);color:var(--pine);font-family:var(--display);font-size:30px;}
.trk{display:flex;flex-direction:column;gap:10px;padding:26px 22px;border-radius:26px;background:var(--paper);border:2px solid var(--line);}
.trk-k{font-size:12.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--teal);}
.trk h3{font-family:var(--display);font-weight:400;font-size:26px;line-height:1.1;margin:0;}
.trk p{margin:0;color:var(--muted);font-size:15.5px;line-height:1.45;}
.trk ul{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:8px;}
.trk li{display:flex;gap:9px;align-items:flex-start;font-size:15px;line-height:1.35;}
.trk li svg{flex:none;width:18px;height:18px;margin-top:1px;} .trk circle{fill:var(--teal);} .trk path{fill:none;stroke:#fff;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;}
.trk-p{margin-top:auto;padding-top:12px;display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;}
.trk-p b{font-family:var(--display);font-weight:400;font-size:34px;color:var(--ink);}
.trk-p span{font-size:13.5px;color:var(--muted);}
.trk.big{background:var(--pine);border-color:var(--pine);color:#fff;padding:30px 28px;box-shadow:0 30px 50px -30px rgba(8,80,85,.9);}
.trk.big .trk-k{color:var(--ember);} .trk.big h3{font-size:32px;color:#fff;} .trk.big p,.trk.big .trk-p span{color:var(--on-pine-soft);}
.trk.big li{color:#fff;} .trk.big circle{fill:var(--ember);} .trk.big .trk-p b{color:#FFCFA3;}
.trk.big .res{margin-top:8px;font-family:var(--hand);font-size:23px;line-height:1.2;color:#fff;} .trk.big .res b{color:#FFCFA3;font-weight:700;}
.trk.big .btn{margin-top:14px;background:var(--ember);color:#2B1304;border-color:#E27A33;justify-content:center;}
.trk-w{font-weight:800;color:var(--pine)!important;}
.trk.big .trk-w{color:#fff!important;}
.trk-pr{font-family:var(--hand);font-size:21px!important;line-height:1.2!important;color:var(--ember-ink)!important;margin-top:4px!important;}
.trk.big .trk-pr{color:#FFCFA3!important;}
.fm-quote{margin:40px auto 0;text-align:center;font-family:var(--hand);font-weight:700;font-size:clamp(28px,3.2vw,38px);color:var(--pine);transform:rotate(-1.5deg);}
.ab-role{font-weight:800;color:var(--pine);margin:-6px 0 18px;}
.ab-sign{font-family:var(--hand);font-size:clamp(24px,2.6vw,30px);line-height:1.2;color:var(--pine);margin:6px 0 0!important;}
.ab-why{margin-top:30px;padding:26px 28px;border-radius:26px;background:var(--peach);}
.ab-why .ab-big{margin:6px 0 14px;font-size:clamp(24px,2.8vw,32px);}
.ab-why p{color:var(--ink);margin:0 0 12px;} .ab-why p:last-child{margin-bottom:0;}
.ab-v{align-self:start;position:sticky;top:110px;}
.ab-v .ab-c{flex-direction:column;align-items:flex-start;margin-top:18px;}
.nl-k{font-weight:800;color:var(--pine);margin-bottom:6px!important;}
.nl-h{font-family:var(--hand);font-size:23px;line-height:1.2;color:var(--ember-ink)!important;}
footer .wrap > span{line-height:1.6;}
footer .flg a{font-weight:600;text-decoration:underline;text-decoration-color:rgba(8,80,85,.25);text-underline-offset:3px;}
footer .flg a:hover,footer .flg a[aria-current]{color:var(--pine);text-decoration-color:currentColor;}
footer nav{align-items:center;}
footer .fso{display:inline-flex;gap:10px;}
footer .fso a{display:grid;place-items:center;width:38px;height:38px;border-radius:12px;background:var(--mint);color:var(--teal);transition:background .15s,color .15s;}
footer .fso a:hover{background:var(--teal);color:#fff;}
footer .fso a:focus-visible{outline:3px solid var(--ember);outline-offset:2px;}
footer .fso svg{width:20px;height:20px;}
/* header: Winter Pack button */
.top .nav .btn.wpnav{background:var(--pine);color:#fff;border:2px solid var(--pine);box-shadow:0 12px 22px -14px rgba(8,80,85,.9);padding:9px 18px;font-size:14.5px;gap:6px;}
.top .nav .btn.wpnav:hover{background:var(--teal);border-color:var(--teal);color:#fff;}
.top .nav .btn.wpnav span{font-size:15px;line-height:1;}
.top .nav .btn.wpnav:focus-visible{outline:3px solid var(--ember);outline-offset:3px;}
@media (max-width:640px){.top .wrap{gap:10px;} .top .nav{gap:8px;} .top .nav .btn.wpnav,.hx .nav .rdvbtn{padding:8px 12px;font-size:13px;white-space:nowrap;} .logo{height:28px;}}
@media (max-width:370px){.top .nav .btn.wpnav span{display:none;} .top .nav .btn.wpnav,.hx .nav .rdvbtn{padding:8px 10px;}}
/* home: Winter Pack section */
.wpk{position:relative;overflow:hidden;background:linear-gradient(180deg,#E4F5F6 0%,#F4FBFB 100%);}
.wpk-fl{position:absolute;inset:0;pointer-events:none;}
.wpk-fl i{position:absolute;font-style:normal;line-height:1;color:var(--teal);opacity:.22;}
.wpk-g{position:relative;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(36px,5vw,72px);align-items:center;}
.wpk .h2{margin-bottom:16px;}
.wpk .h2 span{display:block;font-family:var(--hand);font-weight:700;font-size:.62em;line-height:1.1;color:var(--ember-ink);margin-top:4px;}
.wpk-l{list-style:none;margin:6px 0 24px;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:9px 18px;}
.wpk-l li{display:flex;align-items:flex-start;gap:9px;font-size:15.5px;line-height:1.35;color:var(--ink);}
.wpk-l svg{flex:none;width:19px;height:19px;margin-top:1px;}
.wpk-l circle{fill:var(--teal);} .wpk-l path{fill:none;stroke:#fff;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;}
.wpk-o{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-bottom:18px;}
.wpk-c{display:flex;flex-direction:column;gap:2px;padding:16px 18px;border-radius:20px;background:#fff;border:2px solid #CDE9EB;text-decoration:none;color:var(--ink);transition:border-color .15s,transform .2s;}
.wpk-c:hover{border-color:var(--teal);transform:translateY(-2px);}
.wpk-c:focus-visible{outline:3px solid var(--ember);outline-offset:3px;}
.wpk-c small{font-size:12.5px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);}
.wpk-c b{font-family:var(--display);font-weight:400;font-size:21px;color:var(--pine);}
.wpk-c span{font-weight:800;font-size:18px;color:var(--ember-ink);}
.wpk-gift{display:flex;align-items:flex-start;gap:10px;margin:0 0 24px;padding:12px 16px;border-radius:16px;background:#FFF4EE;border:2px dashed var(--ember);font-size:15px;line-height:1.45;color:var(--ink);}
.wpk-gift b{color:var(--ember-ink);}
.wpk-v{position:relative;min-height:440px;}
.wpk-d{position:absolute;width:min(62%,300px);height:auto;border-radius:14px;border:6px solid #fff;box-shadow:0 30px 50px -30px rgba(8,80,85,.75);}
.wpk-d.d1{left:2%;top:10%;transform:rotate(-8deg);}
.wpk-d.d2{right:2%;top:6%;transform:rotate(7deg);}
.wpk-d.d3{left:50%;top:0;transform:translateX(-50%) rotate(-1deg);z-index:2;}
.wpk-st{position:absolute;z-index:3;right:2%;bottom:6%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;width:146px;height:146px;padding:16px;border-radius:50%;background:var(--pine);color:#fff;font-weight:800;font-size:13.5px;line-height:1.25;transform:rotate(8deg);box-shadow:0 18px 30px -16px rgba(8,40,43,.8);}
.wpk-st b{display:block;font-family:var(--display);font-weight:400;font-size:44px;line-height:1;color:var(--ember);}
@media (max-width:1020px){.wpk-g{grid-template-columns:1fr;} .wpk-v{order:-1;min-height:0;height:min(92vw,400px);max-width:480px;width:100%;margin-inline:auto;}}
@media (max-width:560px){.wpk-l{grid-template-columns:1fr;} .wpk-o{gap:10px;} .wpk-c{padding:14px;} .wpk-c small{font-size:11px;} .wpk-c b{font-size:17px;line-height:1.2;} .wpk-c span{font-size:16px;} .wpk .btn.rdvbtn{width:100%;justify-content:center;} .wpk-st{width:112px;height:112px;padding:12px;font-size:11.5px;} .wpk-st b{font-size:34px;}}
@media (prefers-reduced-motion:reduce){.wpk-c{transition:none;}}
/* home: audit section, real report preview */
#audit .a5-h{text-align:center;display:flex;flex-direction:column;align-items:center;}
#audit .a5-h .sub{text-align:center;margin-inline:auto;max-width:52ch;}
.a5-g{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:26px;margin:48px auto 0;max-width:900px;}
.a5-c{position:relative;margin:0;display:flex;flex-direction:column;background:#fff;border-radius:26px;padding:14px 14px 18px;box-shadow:0 30px 50px -36px rgba(8,80,85,.75);}
.a5-i{height:300px;overflow:hidden;border-radius:16px;border:1px solid rgba(8,80,85,.08);background:#FCFAF8;}
.a5-i img{display:block;width:100%;height:100%;object-fit:cover;object-position:top left;transition:transform 4s ease;}
.a5-i.fit img{object-fit:contain;object-position:center;}
.a5-c:hover .a5-i img{transform:scale(1.04);}
.a5-n{position:absolute;z-index:2;top:-14px;left:-10px;display:grid;place-items:center;width:44px;height:44px;border-radius:50%;background:var(--ember);color:#2B1304;font-family:var(--display);font-size:22px;box-shadow:0 10px 20px -10px rgba(180,86,31,.8);}
.a5-c figcaption{display:flex;flex-direction:column;align-items:flex-start;gap:8px;padding:14px 6px 0;}
.a5-c figcaption b{font-family:var(--display);font-weight:400;font-size:21px;line-height:1.2;color:var(--pine);}
.a5-b{font-size:12px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;padding:5px 10px;border-radius:999px;background:var(--peach2);color:var(--ember-ink);} .a5-b.co{background:#CDE9EB;color:var(--pine);}
.a5-cta{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:14px 18px;margin-top:8px;}
.a5-sec{background:#fff;color:var(--pine);border:2px solid var(--pine);padding:17px 30px;font-size:17px;}
.a5-sec:hover{background:var(--pine);color:#fff;}
.a5-cta a:focus-visible{outline:3px solid var(--ember);outline-offset:3px;}
.a5-note{margin:22px 0 0;text-align:center;font-family:var(--hand);font-weight:700;font-size:22px;color:var(--ember-ink);}
@media (max-width:760px){.a5-g{grid-template-columns:1fr;max-width:480px;} .a5-i{height:260px;}}
@media (max-width:560px){.a5-cta .btn{width:100%;justify-content:center;}}
@media (prefers-reduced-motion:reduce){.a5-i img{transition:none;}}

/* home: social section */
.soc{background:var(--paper);}
.soc .wrap{padding-block:clamp(56px,6vw,84px);}
.soc-h{text-align:center;display:flex;flex-direction:column;align-items:center;margin-bottom:30px;}
.soc-h .h2{margin:6px 0 0;font-size:clamp(28px,3.2vw,38px);max-width:none;}
.soc-g{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;max-width:900px;margin-inline:auto;}
.soc-c{display:grid;grid-template-columns:64px minmax(0,1fr);grid-template-rows:auto auto;gap:6px 18px;align-items:center;padding:22px 24px;border-radius:26px;background:#fff;border:2px solid var(--line);text-decoration:none;color:var(--ink);box-shadow:0 22px 40px -34px rgba(8,80,85,.6);transition:transform .2s,border-color .2s,box-shadow .2s;}
.soc-c:hover{transform:translateY(-4px);border-color:#CDE9EB;box-shadow:0 26px 44px -30px rgba(8,80,85,.6);}
.soc-c:focus-visible{outline:3px solid var(--ember);outline-offset:4px;}
.soc-l{grid-row:span 2;display:block;width:64px;height:64px;}
.soc-l svg{display:block;width:100%;height:100%;}
.soc-t{display:flex;flex-direction:column;gap:2px;min-width:0;}
.soc-t small{font-size:12.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);}
.soc-t b{font-family:var(--display);font-weight:400;font-size:21px;line-height:1.2;color:var(--pine);overflow-wrap:anywhere;}
.soc-t b.soc-hd{font-size:18px;overflow-wrap:normal;}
.soc-t > span{font-size:15px;line-height:1.45;color:var(--muted);}
.soc-a{font-weight:800;font-size:15px;color:var(--ember-ink);}
.soc-a span{display:inline-block;transition:translate .2s;} .soc-c:hover .soc-a span{translate:4px 0;}
@media (max-width:760px){.soc-g{grid-template-columns:1fr;max-width:520px;}}
@media (max-width:420px){.soc-c{grid-template-columns:52px minmax(0,1fr);padding:18px;gap:6px 14px;} .soc-l{width:52px;height:52px;} .soc-t b{font-size:18px;} .soc-t b.soc-hd{font-size:16px;}}
@media (prefers-reduced-motion:reduce){.soc-c,.soc-a span{transition:none;}}


.eq-more{margin-top:26px;text-align:center;color:var(--muted);font-size:15px;}
.eq-more a{font-weight:800;color:var(--pine);}
/* programme: numbered tiles + kit */
.mods{list-style:none;margin:36px 0 0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;}
.mods li{display:flex;flex-direction:column;gap:4px;padding:22px 22px 20px;border-radius:22px;background:#fff;}
.mods .mn{font-family:var(--display);font-size:38px;line-height:1;color:var(--ember);}
.mods b{font-family:var(--display);font-weight:400;font-size:21px;margin-top:8px;}
.mods li > span:last-child{font-family:var(--hand);font-size:23px;line-height:1.15;color:var(--teal);margin-top:4px;}
.kit{margin-top:30px;display:flex;flex-wrap:wrap;align-items:center;gap:12px 18px;}
.kit p{margin:0;color:var(--ink);}
.kit ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:8px;}
.kit li{background:var(--pine);color:#fff;border-radius:999px;padding:7px 14px;font-size:14px;font-weight:700;}
/* about */
.ab{display:grid;grid-template-columns:minmax(0,.7fr) minmax(0,1.3fr);gap:60px;align-items:start;}
.ab-v img{display:block;width:100%;max-width:320px;aspect-ratio:420/540;border-radius:32px;object-fit:cover;transform:rotate(-3deg);box-shadow:0 30px 50px -30px rgba(8,80,85,.7);}
.ab-n{margin:22px 0 0;display:flex;flex-direction:column;font-size:14.5px;color:var(--muted);max-width:300px;}
.ab-n b{font-family:var(--display);font-weight:400;font-size:24px;color:var(--ink);}
.ab-big{font-family:var(--display);font-size:clamp(28px,3.4vw,40px);line-height:1.15;color:var(--pine);margin:8px 0 20px;}
.ab-t > p{color:var(--ink);max-width:62ch;margin:0 0 14px;}
.ab-c{list-style:none;margin:22px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:10px;}
.ab-c li{background:var(--mint);border-radius:999px;padding:9px 16px;font-size:14px;font-weight:700;}
.ab-c b{font-family:var(--display);font-weight:400;font-size:19px;color:var(--pine);margin-right:6px;}
/* testimonials: scroll row */
 .tm-h{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:16px;}
 .tm-h .sp-google.big{margin:0;}
 .tms{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(290px,1fr);gap:18px;margin-top:34px;overflow-x:auto;scroll-snap-type:x mandatory;padding:6px 4px 22px;}
.tm{scroll-snap-align:start;margin:0;display:flex;flex-direction:column;gap:14px;padding:26px 24px 22px;border-radius:26px;background:#fff;box-shadow:0 18px 36px -28px rgba(8,80,85,.7);}
.tm-q{font-family:var(--display);font-size:70px;line-height:.6;color:var(--ember);height:30px;}
.tm blockquote{margin:0;font-size:15.5px;line-height:1.55;color:var(--ink);}
.tm figcaption{margin-top:auto;display:flex;align-items:center;gap:12px;font-size:13.5px;color:var(--muted);}
.tm figcaption b{display:block;color:var(--ink);font-size:15px;}
.tm-i{flex:none;display:grid;place-items:center;width:42px;height:42px;border-radius:50%;background:var(--peach2);color:var(--ember-ink);font-family:var(--display);font-size:16px;}
.tm-g{display:flex;align-items:center;gap:7px;font-size:12.5px;font-weight:800;color:#3c4043;}
.tm-g .sp-g{width:16px;height:16px;}
.tm-hint{margin:4px 0 0;font-family:var(--hand);font-size:22px;color:var(--pine);text-align:right;}
/* newsletter: peach card */
.nl{display:grid;grid-template-columns:auto minmax(0,1fr);gap:clamp(24px,5vw,60px);align-items:center;background:var(--peach2);border-radius:34px;padding:clamp(26px,4vw,50px);}
.nl img{width:clamp(140px,18vw,210px);height:auto;transform:rotate(-6deg);}
.nl h2{font-family:var(--display);font-weight:400;font-size:clamp(30px,4vw,46px);line-height:1.08;margin:6px 0 12px;}
.nl p{margin:0 0 12px;color:var(--ink);max-width:56ch;}
.nl-s b{font-family:var(--display);font-weight:400;font-size:30px;color:var(--ember-ink);margin-right:4px;}
.nl .btn{margin-top:8px;}
/* blog: editorial list */
.bl{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:56px;align-items:start;}
.bl .btn{margin-top:20px;}
.bl-l{list-style:none;margin:0;padding:0;border-top:2px solid var(--ink);}
.bl-l a{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:18px;align-items:center;padding:20px 4px;border-bottom:1.5px solid var(--line);text-decoration:none;color:var(--ink);}
.bl-l a:hover .bt{color:var(--teal);} .bl-l a:hover .ba{transform:translateX(4px);}
.bn{font-family:var(--hand);font-weight:700;font-size:26px;color:var(--ember-ink);}
.bt{font-family:var(--display);font-size:clamp(19px,2vw,23px);line-height:1.2;transition:color .2s;}
.ba{font-size:20px;color:var(--pine);transition:transform .2s;}
/* blog: picture cards */
.bg-h{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:20px 40px;}
.bg-h .sub{margin-bottom:0;}
.posts2{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;margin-top:52px;}
.pc2{display:flex;flex-direction:column;text-decoration:none;color:var(--ink);background:#fff;border-radius:24px;overflow:hidden;box-shadow:0 22px 40px -30px rgba(8,80,85,.7);transition:transform .25s,box-shadow .25s;}
.pc2:hover{transform:translateY(-6px);box-shadow:0 30px 50px -30px rgba(8,80,85,.8);}
.pc2-i{display:block;aspect-ratio:4/3;overflow:hidden;background:var(--mint);}
.pc2-i img{display:block;width:100%;height:100%;object-fit:cover;transition:transform .4s;}
.pc2:hover .pc2-i img{transform:scale(1.05);}
.pc2-t{display:flex;flex-direction:column;gap:10px;padding:22px 22px 24px;flex:1;}
.pc2-k{font-family:var(--hand);font-weight:700;font-size:21px;line-height:1;color:var(--ember-ink);}
.pc2-h{font-family:var(--display);font-size:20px;line-height:1.25;}
.pc2-m{margin-top:auto;padding-top:6px;font-weight:800;font-size:14px;color:var(--pine);}
.pc2:focus-visible{outline:3px solid var(--ember);outline-offset:4px;}
@media (max-width:1020px){.posts2{grid-template-columns:repeat(2,minmax(0,1fr));}}
@media (max-width:560px){.posts2{grid-template-columns:1fr;gap:20px;}}
@media (prefers-reduced-motion:reduce){.pc2,.pc2-i img{transition:none;}}
/* audit card: title on top, steps in a row, text + button below */
.aud{display:block!important;}
.aud .aud-h{max-width:24ch;margin-bottom:34px;}
.aud-s{grid-template-columns:repeat(3,minmax(0,1fr));align-items:stretch;}
.aud-s li{flex-direction:column;gap:14px;}
.aud-f{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:20px 40px;margin-top:34px;padding-top:30px;border-top:1.5px dashed rgba(8,80,85,.18);}
.aud-f .sub{margin:0!important;max-width:58ch;}
.aud-f .btn{margin:0!important;}
.aud-dark .aud-f{border-top-color:rgba(255,255,255,.22);}
/* audit: the two real options */
.aud-o{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;}
.ao{display:flex;flex-direction:column;gap:8px;padding:26px 26px 24px;border-radius:24px;text-decoration:none;color:var(--ink);border-left:6px solid var(--ember);background:var(--peach);transition:transform .2s,box-shadow .2s;}
.ao.co{border-left-color:var(--teal);background:var(--mint);}
.ao:hover{transform:translateY(-4px);box-shadow:0 22px 36px -28px rgba(8,80,85,.7);}
.ao:focus-visible{outline:3px solid var(--ember);outline-offset:4px;}
.ao-i{font-size:24px;line-height:1;color:var(--ember);} .ao.co .ao-i{color:var(--teal);}
.ao-k{font-size:12.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--ember-ink);} .ao.co .ao-k{color:var(--teal);}
.ao b{font-family:var(--display);font-weight:400;font-size:26px;line-height:1.15;color:var(--ink);}
.ao-t{font-size:15.5px;line-height:1.55;color:var(--muted);} .ao-t strong{color:var(--ink);}
.ao-c{margin-top:auto;padding-top:8px;font-weight:800;color:var(--ember-ink);} .ao.co .ao-c{color:var(--pine);}
.aud-n{margin:28px 0 0;padding-top:24px;border-top:1.5px dashed rgba(8,80,85,.18);font-size:17px;line-height:1.6;color:var(--muted);} .aud-n b{color:var(--pine);}
.aud-dark .aud-n{color:var(--on-pine-soft);border-top-color:rgba(255,255,255,.22);} .aud-dark .aud-n b{color:#fff;}
@media (max-width:760px){.aud-o{grid-template-columns:1fr;}}
@media (prefers-reduced-motion:reduce){.ao{transition:none;}}
/* formations equation: the two parcours side by side, "=" then the complete one across */
.eq{grid-template-columns:minmax(0,1fr) auto minmax(0,1fr)!important;align-items:stretch!important;}
.eq-eq{grid-column:1/-1;justify-self:center;}
.trk.big{grid-column:1/-1;display:grid!important;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:20px 56px;padding:44px 48px!important;}
.bg-a,.bg-b{display:flex;flex-direction:column;gap:14px;}
.bg-b ul{margin-top:0!important;}
.trk.big .bg-b .btn{align-self:flex-start;}
.trk.big h3{font-size:clamp(32px,3.4vw,42px)!important;}
/* kit du manager */
.kit2{margin-top:56px;display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:40px 56px;align-items:center;padding:clamp(32px,5vw,60px);border-radius:34px;background:var(--pine);color:#fff;box-shadow:0 34px 60px -40px rgba(8,80,85,.9);position:relative;overflow:hidden;}
.kit2::after{content:"";position:absolute;right:-90px;bottom:-110px;width:280px;height:280px;border-radius:50%;background:rgba(255,255,255,.05);pointer-events:none;}
.kit2 .hand{color:var(--ember);font-size:30px;}
.kit2 h3{font-family:var(--display);font-weight:400;font-size:clamp(28px,3.2vw,40px);line-height:1.12;margin:8px 0 16px;color:#fff;}
.kit2 h3 em{font-style:normal;color:#FFCFA3;}
.kit2-h p{margin:0;color:var(--on-pine-soft);font-size:17px;line-height:1.6;max-width:44ch;}
.kit2-l{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;position:relative;z-index:1;}
.kit2-l li{display:flex;align-items:center;gap:14px;padding:16px 18px;border-radius:20px;background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.12);}
.kit2-l .ki{flex:none;display:grid;place-items:center;width:46px;height:46px;border-radius:14px;background:var(--ember);color:#2B1304;}
.kit2-l .ki svg{width:24px;height:24px;}
.kit2-l b{display:block;font-size:16px;font-weight:800;color:#fff;line-height:1.3;}
.kit2-l small{display:block;font-size:13px;color:var(--on-pine-soft);margin-top:2px;line-height:1.35;}
@media (max-width:1020px){.kit2{grid-template-columns:1fr;}}
@media (max-width:520px){.kit2-l{grid-template-columns:1fr;}}
/* about: intro row + full-width "why" band */
#elodie .ab{align-items:center!important;}
#elodie .ab-v{position:static!important;align-self:center!important;}
#elodie .ab-v img{max-width:340px;}
#elodie .ab-sign{line-height:1.25!important;margin-top:22px!important;}
#elodie .ab-c{flex-direction:row!important;flex-wrap:wrap;margin:0 0 26px!important;}
.why2{margin-top:clamp(56px,7vw,90px);display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:28px 64px;align-items:center;padding:clamp(32px,5vw,60px);border-radius:34px;background:var(--peach);border-left:8px solid var(--ember);}
.why2-q{position:relative;margin:10px 0 0;padding-left:44px;font-family:var(--display);font-size:clamp(28px,3.2vw,40px);line-height:1.15;color:var(--pine);}
.why2-q span{position:absolute;left:0;top:-8px;font-size:76px;line-height:1;color:var(--ember);}
.why2-b p{margin:0 0 16px;color:var(--ink);line-height:1.7;}
.why2-b p:last-child{margin-bottom:0;}
@media (max-width:1020px){.why2{grid-template-columns:1fr;} #elodie .ab-v{justify-self:center;text-align:center;} #elodie .ab-v img{margin-inline:auto;} #elodie .ab-n{margin-inline:auto;}}
/* titles: fewer lines */
main .room .h2{max-width:28ch;}
.pg-h{text-align:center;display:flex;flex-direction:column;align-items:center;}
.pg-h .h2{max-width:none;font-size:clamp(30px,3.6vw,46px);}
.pg-h .sub{max-width:62ch;margin-inline:auto;}
@media (max-width:560px){main .room .h2{font-size:30px;line-height:1.12;} .aud .aud-h{font-size:25px;} .pg-h .h2{font-size:25px;}}
/* pourquoi je peux te former */
.ab-why{border-left:6px solid var(--ember);}
.ab-why .ab-big{position:relative;line-height:1.2!important;margin:10px 0 18px!important;padding-left:38px;font-size:clamp(24px,2.6vw,30px);}
.ab-why .ab-big span{position:absolute;left:0;top:-6px;font-size:64px;line-height:1;color:var(--ember);}
/* final: orange */
.fin2{background:var(--ember);color:#2B1304;text-align:center;}
.fin2 .wrap{padding-block:clamp(56px,7vw,90px);max-width:860px;}
.fin2 .hand{color:#fff;font-size:30px;}
.fin2 h2{font-family:var(--display);font-weight:400;font-size:clamp(34px,4.6vw,56px);line-height:1.06;margin:8px 0 16px;}
.fin2 p{margin:0 auto 8px;max-width:60ch;font-size:18px;}
.fin2-k{font-family:var(--hand);font-size:26px;font-weight:700;}
.fin2 .btn.rdvbtn{margin-top:22px;background:var(--pine);color:#fff;border-color:var(--pine);box-shadow:0 18px 30px -16px rgba(8,40,43,.8);}
.fin2 .btn.rdvbtn:hover{background:#0a6166;color:#fff;}
/* more air between and inside sections */
main > .room{padding-block:clamp(96px,11vw,150px);}
main .room .h2{margin:10px 0 24px;}
main .room .sub{margin:0 0 14px;line-height:1.65;}
main .room .hand{margin-bottom:18px;}
.h2o > .wrap:first-child{padding-block:96px 56px;gap:72px;}
.h2o .lede{margin-bottom:6px;} .h2o .ctas{margin-top:38px;}
.h2o-s{padding:40px 0 52px;gap:24px;}
.sp-band{padding:28px 0;}
.mo{gap:80px;} .chatlist{gap:20px;} .bub{padding:20px 24px;}
.aud{gap:64px;padding:clamp(36px,5vw,68px);} .aud-s{gap:18px;} .aud-s li{padding:22px 24px;} .aud-t .btn{margin-top:30px;}
.eq{margin-top:64px;gap:20px;} .trk{padding:32px 26px;gap:14px;} .trk.big{padding:38px 32px;} .trk ul{gap:10px;margin-top:10px;}
.eq-more{margin-top:40px;} .fm-quote{margin-top:56px;}
.mods{margin-top:56px;gap:22px;} .mods li{padding:28px 26px 26px;} .kit{margin-top:44px;gap:16px 22px;}
.ab{gap:88px;} .ab-t > p{margin:0 0 20px;line-height:1.7;} .ab-role{margin:-4px 0 26px;} .ab-sign{margin-top:14px!important;}
.ab-why{margin-top:48px;padding:34px 36px;} .ab-why p{margin:0 0 16px;line-height:1.7;}
.ab-v .ab-c{margin-top:26px;gap:12px;}
.tm-h{gap:24px;} .tms{margin-top:48px;gap:24px;} .tm{padding:32px 28px 26px;gap:18px;} .tm-hint{margin-top:14px;}
.nl{padding:clamp(36px,5vw,72px);gap:clamp(32px,6vw,80px);} .nl p{margin:0 0 16px;line-height:1.65;} .nl h2{margin:8px 0 18px;} .nl .btn{margin-top:14px;}
.bl{gap:80px;} .bl .btn{margin-top:30px;} .bl-l a{padding:26px 6px;}
.fin2 .wrap{padding-block:clamp(80px,10vw,130px);} .fin2 h2{margin:12px 0 22px;} .fin2 p{margin-bottom:12px;} .fin2 .btn.rdvbtn{margin-top:32px;}
#blog{background:var(--peach);}
footer .wrap{padding-block:40px;}
@media (max-width:1020px){
  main > .room{padding-block:clamp(72px,14vw,100px);}
  .h2o > .wrap:first-child{padding-block:64px 40px;gap:48px;}
  .mo,.ab,.bl{gap:48px;} .aud{gap:40px;} .eq{gap:16px;}
}
@media (max-width:1020px){
  .h2o > .wrap:first-child,.mo,.aud,.ab,.bl{grid-template-columns:1fr;} .ab-v{position:static;}
  .h2o-v{width:min(100%,320px);} .tag{left:-20px;}
  .eq{grid-template-columns:1fr!important;max-width:560px;margin-inline:auto;} .eq-op{justify-self:center;}
  .trk.big{grid-template-columns:1fr;padding:32px 26px!important;} .aud-s{grid-template-columns:1fr;}
  .mods{grid-template-columns:repeat(2,minmax(0,1fr));}
  .h2o-s{grid-template-columns:repeat(2,minmax(0,1fr));}
}
@media (max-width:560px){
  .mods{grid-template-columns:1fr;} .nl{grid-template-columns:1fr;} .bub{max-width:96%;}
  .hx .nav .rdvbtn{padding:9px 16px;font-size:14px;}
}
</style>
'''
