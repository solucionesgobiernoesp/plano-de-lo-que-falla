#!/usr/bin/env python3
"""Convierte la fuente del artefacto de Claude en una web completa (index.html).

Uso: python3 scripts/build.py [fuente/plano.html] [index.html]

Acepta la fuente tal como la guarda Claude (empieza por <title>) o la versión
servida por el visor (con <!doctype html>…<body> delante): en ese caso quita
esa envoltura antes de construir.
"""
import sys, re, pathlib

src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'fuente/plano.html')
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else 'index.html')
html = src.read_text(encoding='utf-8')

# Quitar la envoltura del visor si viene incluida
if html.lstrip().lower().startswith('<!doctype'):
    html = html[html.index('<body>') + len('<body>'):]
    html = re.sub(r'</body>\s*</html>\s*$', '', html.rstrip()) + '\n'
html = html.lstrip()

split = html.index('<div id="app">')
head, body = html[:split], html[split:]
head = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\s*', '', head)

DESC = ('Los 49 problemas estructurales de España contados como un plano de metro: '
        'el dato, por qué pasa, por qué no se arregla y qué país lo hace mejor.')
ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 28 28'%3E"
        "%3Ccircle cx='14' cy='14' r='10.5' fill='none' stroke='%23121418' stroke-width='7'/%3E%3C/svg%3E")
RESET = (':root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);'
         'padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}'
         'body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}'
         'img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}')

page = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="{DESC}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="Plano de lo que falla">
<meta property="og:description" content="{DESC}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{ICON}">
<style>{RESET}</style>
{head.rstrip()}
</head>
<body>
{body.rstrip()}
</body>
</html>
'''
out.write_text(page, encoding='utf-8')
print(f'{out}: {len(page.encode("utf-8")):,} bytes')
