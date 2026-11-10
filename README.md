# Plano de lo que falla

Los 49 problemas estructurales de España contados como un plano de metro: el dato, por qué pasa, por qué no se arregla y qué país lo hace mejor.

Proyecto SOLUCIONESGOBIERNO. Apolítico: cada dato lleva su fuente y cada solución se mide con los mismos criterios.

## Cómo se actualiza

La página se edita con Claude. Cada cambio se publica a la vez en el artefacto de Claude y en este repositorio, y GitHub Pages vuelve a desplegar la web en un minuto o dos.

- `index.html`: la web completa, en un solo archivo.
- `fuente/plano.html`: el mismo contenido tal como lo guarda Claude, sin la cabecera HTML.
- `scripts/build.py`: convierte la fuente en `index.html` (`python3 scripts/build.py`).
