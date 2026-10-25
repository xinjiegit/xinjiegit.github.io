#!/usr/bin/env python3
"""Render the static Academic Pages adaptation using only Python's standard library."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    ('index.html', 'about', 'About me', 'About'),
    ('publications.html', 'publications', 'Publications', 'Publications'),
    ('projects.html', 'projects', 'Research projects', 'Projects'),
    ('teaching.html', 'teaching', 'Mentoring and teaching', 'Teaching'),
    ('cv.html', 'cv', 'Curriculum vitae', 'CV'),
]
profile = (ROOT / 'content/profile.html').read_text()
for filename, slug, title, label in PAGES:
    navigation = ''.join(
        f'<li class="masthead__menu-item"><a href="{url}"'
        + (' aria-current="page"' if url == filename else '')
        + f'>{name}</a></li>'
        for url, _, _, name in PAGES
    )
    body = (ROOT / f'content/{slug}.html').read_text()
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} - Xinjie He</title>
<meta name="description" content="Xinjie He, Ph.D. candidate in Mathematics at UCLA. Research in AI for mathematics, automated theorem proving, and formal verification.">
<meta property="og:title" content="{escape(title)} - Xinjie He">
<meta property="og:type" content="website">
<meta property="og:url" content="https://xinjiegit.github.io/{'' if filename == 'index.html' else filename}">
<meta name="color-scheme" content="light">
<link rel="canonical" href="https://xinjiegit.github.io/{'' if filename == 'index.html' else filename}">
<link rel="stylesheet" href="assets/vendor/academicpages/main.css">
<link rel="stylesheet" href="style.css">
<script src="navigation.js" defer></script>
</head>
<body id="top">
<a class="skip-link" href="#content">Skip to content</a>
<header class="masthead">
  <div class="masthead__inner-wrap">
    <nav class="site-navigation" aria-label="Main navigation">
      <a class="site-title" href="index.html">Xinjie He</a>
      <ul>{navigation}</ul>
    </nav>
  </div>
</header>
<div id="main">
  <aside class="sidebar" aria-label="About Xinjie He">{profile}</aside>
  <main class="page" id="content" tabindex="-1">
    <div class="page__inner-wrap">
      <h1 class="page__title">{title}</h1>
      <div class="page__content">{body}</div>
    </div>
  </main>
</div>
<footer class="page__footer">
  <div class="footer-inner">
    <p><a href="https://github.com/xinjiegit">GitHub</a> · <a href="mailto:xinjieh@math.ucla.edu">Email</a> · <a href="cv.pdf">CV (PDF)</a></p>
    <p>© 2026 Xinjie He. Adapted from <a href="https://academicpages.github.io/">Academic Pages</a>, based on <a href="https://mmistakes.github.io/minimal-mistakes/">Minimal Mistakes</a>.</p>
    <p>Last updated October 2026</p>
  </div>
</footer>
</body>
</html>
'''
    (ROOT / filename).write_text(html)
    print(f'Built {filename}')
