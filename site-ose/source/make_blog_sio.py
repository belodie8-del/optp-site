"""Blog variant for Systeme.io: our header+hero, then the native article list (<!--LIST-->), then audit strip + newsletter + footer."""
s = open('blog-test.html', encoding='utf-8').read()
a = s.index('<section class="room" id="articles">'); b = s.index('<div class="as">', a); c = s.index('</div></section>', b)
strip = s[b:c]
s = s[:a] + '<!--LIST-->\n<section class="room" id="articles"><div class="wrap">' + strip + '</div></section>' + s[c + len('</div></section>'):]
s = s.replace("main > #articles{padding-bottom:clamp(40px,5vw,64px);}", "main > #articles{padding-top:24px;padding-bottom:clamp(40px,5vw,64px);} #articles .as{margin-top:0;}")
i = s.index("<script>(function(){\n  var bs="); j = s.index('</script>', i) + len('</script>')
s = s[:i] + s[j:]
open('blog-sio.html', 'w', encoding='utf-8').write(s)
