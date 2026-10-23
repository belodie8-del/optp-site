"""Turns the generated pages into Systeme.io 'Code HTML' blocks:
- every big embedded image is written to IMG_DIR and referenced by URL (hosted with the Winter Pack site, folder /ose/);
- the CSS is pruned to what the page uses and scoped under .ose so it cannot clash with Systeme.io;
- output: sio/<page>.html (one block per page; the contact page is split around the native contact form)."""
import re, os, hashlib, base64, sys
OUT = 'sio/'; IMG_DIR = '/home/user/optp-site/site-ose/images-sio/'
BASE = 'https://winterpack.oseprendretaplace.fr/ose/'
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Young+Serif&family=Nunito+Sans:opsz,wght@6..12,400..800&family=Caveat:wght@600;700&display=swap">\n')
os.makedirs(OUT, exist_ok=True); os.makedirs(IMG_DIR, exist_ok=True)

def host(m):
    uri = m.group(0)
    if len(uri) < 2500: return uri
    head, data = uri.split(',', 1)
    ext = {'image/jpeg': 'jpg', 'image/png': 'png', 'image/svg+xml': 'svg', 'image/webp': 'webp'}[head[5:].split(';')[0]]
    raw = base64.b64decode(data) if ';base64' in head else data.encode()
    name = hashlib.sha1(raw).hexdigest()[:12] + '.' + ext
    open(IMG_DIR + name, 'wb').write(raw)
    return BASE + name

def split_rules(css):
    """yield (prelude, body) top-level statements; body None for ;-terminated at-rules"""
    i, n = 0, len(css)
    while i < n:
        while i < n and css[i] in ' \n\t\r': i += 1
        if i >= n: break
        if css.startswith('/*', i):
            i = css.index('*/', i) + 2; continue
        j = i
        while j < n and css[j] not in '{;': j += 1
        if j >= n: break
        pre = css[i:j].strip()
        if css[j] == ';': yield pre, None; i = j + 1; continue
        depth, k = 1, j + 1
        while k < n and depth:
            if css[k] == '{': depth += 1
            elif css[k] == '}': depth -= 1
            k += 1
        yield pre, css[j + 1:k - 1]; i = k

def scope_sel(s):
    s = s.strip()
    if s.startswith(':root'): return '.ose' + s[5:]
    if re.match(r'^html\b', s):
        m = re.match(r'^(html[^\s>+~]*)(.*)$', s)
        return m.group(1) + (' .ose' + m.group(2) if m.group(2).strip() else '')
    if re.match(r'^body\b', s): return '.ose' + s[4:]
    return '.ose ' + s

def used(sel, tokens):
    for part in sel.split(','):
        names = re.findall(r'[.#]([A-Za-z_][\w-]*)', re.sub(r':not\([^)]*\)', '', part))
        if all(nm in tokens for nm in names): return True
    return False

def transform(css, tokens):
    out = []
    for pre, body in split_rules(css):
        if body is None:
            if not pre.startswith('@import'): out.append(pre + ';')
            continue
        if pre.startswith('@media') or pre.startswith('@supports'):
            inner = transform(body, tokens)
            if inner.strip(): out.append(pre + '{' + inner + '}')
        elif pre.startswith('@'):
            out.append(pre + '{' + body + '}')
        else:
            if not used(pre, tokens): continue
            out.append(','.join(scope_sel(x) for x in pre.split(',')) + '{' + body.strip() + '}')
    return '\n'.join(out)

def export(src, name, parts=None):
    s = open(src, encoding='utf-8').read()
    s = re.sub(r'data:[^"\')\s]+', host, s)
    css = '\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', s, re.S))
    body = s[s.index('<header'):]
    body = re.sub(r'<style[^>]*>.*?</style>\s*', '', body, flags=re.S)
    tokens = set(re.findall(r'[A-Za-z_][\w-]*', body)) | {'oa', 'oa-r', 'oa-in', 'oa-m', 'oa-on', 'on', 'wpop-open', 'bonus-open', 'in', 'picked'}
    scoped = transform(css, tokens)
    reset = ('.ose,.ose *,.ose *::before,.ose *::after{box-sizing:border-box;}'
             '.ose h1,.ose h2,.ose h3,.ose h4,.ose h5,.ose p,.ose ul,.ose ol,.ose li,.ose figure,.ose blockquote,.ose figcaption,.ose small,.ose b,.ose strong,.ose em,.ose span,.ose a,.ose label{color:inherit;}'
             '.ose h1,.ose h2,.ose h3,.ose h4,.ose h5,.ose p,.ose ul,.ose ol,.ose figure,.ose blockquote{margin:0;}'
             '.ose ul,.ose ol{padding-left:0;}.ose img,.ose svg{border:0;max-width:100%;}.ose button,.ose input,.ose textarea{font:inherit;}\n')
    style = FONTS + '<style>\n' + reset + scoped + '\n.ose{display:block;width:100%;}\n</style>\n'
    if not parts:
        open(OUT + name + '.html', 'w', encoding='utf-8').write('<!-- ' + name + ' · bloc Code HTML Systeme.io -->\n' + style + '<div class="ose">' + body + '</div>\n')
        return
    # split the body at the given markers: block 1 gets the CSS, the others only markup (+ scripts at the end)
    cuts = [0] + [body.index(m) for m in parts] + [len(body)]
    for k in range(len(cuts) - 1):
        chunk = body[cuts[k]:cuts[k + 1]]
        if k > 0: chunk = '<main>' + chunk   # keeps the `main > …` rules working in the following blocks
        out = ('<!-- ' + name + ' · bloc %d/%d -->\n' % (k + 1, len(cuts) - 1)) + (style if k == 0 else '') + '<div class="ose">' + chunk + '</div>\n'
        open(OUT + '%s-%d.html' % (name, k + 1), 'w', encoding='utf-8').write(out)

if __name__ == '__main__':
    export('accueil-A.html', 'accueil')
    export('formations-test.html', 'formations')
    export('contact-sio.html', 'contact', parts=['<!--FORM-->'])
    export('blog-sio.html', 'blog', parts=['<!--LIST-->'])
    for f in sorted(os.listdir(OUT)): print(f, os.path.getsize(OUT + f))
    print('images', sorted(os.listdir(IMG_DIR)))
