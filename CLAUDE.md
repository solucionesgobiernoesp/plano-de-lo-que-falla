# Plano de lo que falla: web pública

Este repositorio publica en GitHub Pages el artefacto de Claude «Plano de lo que falla».

- Artefacto (donde se edita): https://claude.ai/artifact/TNiJkoXCzkp6zNRZns5UnV
- Web: https://solucionesgobiernoesp.github.io/plano-de-lo-que-falla/ (GitHub Pages, rama `main`, carpeta raíz)

## Regla: cada cambio va a los dos sitios en el mismo paso

1. Publica el cambio en el artefacto (Artifact, con su `url`).
2. Lee el artefacto (Artifact `read`) y pasa el archivo que guarda a `python3 scripts/build.py <archivo>`. Actualiza `fuente/plano.html` (copia exacta del artefacto) e `index.html` (la web completa).
3. Haz commit y push a `main`. GitHub Pages vuelve a desplegar la web solo, en uno o dos minutos.

No edites `index.html` a mano: se genera desde `fuente/plano.html`.
