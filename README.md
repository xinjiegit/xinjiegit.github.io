# Xinjie He's academic website

Static adaptation of [Academic Pages](https://academicpages.github.io/), using the official theme's compiled styles and a shared profile/sidebar layout. This uses plain HTML rather than Jekyll, so the existing GitHub Pages branch deployment and `.nojekyll` continue to work.

## Edit and preview

Edit the page fragments in `content/` and the shared layout in `scripts/build.py`, then run:

```sh
python3 scripts/build.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Visit http://127.0.0.1:8000. Commit the generated root HTML files along with source changes. `style.css` contains local theme adjustments. The PDF CV remains at `cv.pdf` and its LaTeX source at `CV.tex`.

Pages: `index.html`, `publications.html`, `projects.html`, `teaching.html`, and `cv.html`. Legacy homepage section links redirect to their corresponding pages through `navigation.js`.

## Theme provenance

The upstream Sass and MIT license are retained in `assets/vendor/academicpages/`; `UPSTREAM.txt` records the source commit. A local copy of the compiled CSS is included, so page loads do not depend on external stylesheets or fonts.

To rebuild the upstream CSS after changing Sass sources:

```sh
npx --yes sass@1.77.8 --load-path=assets/vendor/academicpages/_sass assets/vendor/academicpages/main.scss assets/vendor/academicpages/main.css --style=compressed --no-source-map
```
