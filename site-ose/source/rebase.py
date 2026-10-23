"""Replaces the @@SITE@@ placeholder of the generated pages with the public address of the new site (site_base.txt, no trailing slash).
Today: https://oseprendretaplace-formation.netlify.app. If the site later moves to its own domain, change that one line and rebuild."""
import glob
BASE = open('site_base.txt', encoding='utf-8').read().strip().rstrip('/')
n = 0
for f in sorted(glob.glob('*.html')):
    s = open(f, encoding='utf-8').read()
    if '@@SITE@@' in s:
        open(f, 'w', encoding='utf-8').write(s.replace('@@SITE@@', BASE)); n += 1
print('rebase ->', BASE, '(%d files)' % n)
