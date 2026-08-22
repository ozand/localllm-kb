
return (() => {
  const posts = [];
  const seen = new Set();
  for (const a of Array.from(document.querySelectorAll('a[href*="/comments/"]'))) {
    const raw = a.href.split('#')[0].split('?')[0].replace(/\/$/, '') + '/';
    if (seen.has(raw) || !raw.includes('/comments/')) continue;
    const title = (a.innerText || a.textContent || '').trim();
    if (title.length < 8) continue;
    seen.add(raw);
    posts.push({title, url: raw});
  }
  return JSON.stringify(posts);
})();
