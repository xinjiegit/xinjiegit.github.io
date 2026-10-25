// Preserve links to sections of the previous single-page website.
if (location.pathname.endsWith('/') || location.pathname.endsWith('/index.html')) {
  const destinations = {
    '#publications': 'publications.html',
    '#projects': 'projects.html',
    '#mentoring': 'teaching.html',
    '#research': 'index.html#research'
  };
  const target = destinations[location.hash];
  if (target && location.hash !== '#research') location.replace(target);
}
