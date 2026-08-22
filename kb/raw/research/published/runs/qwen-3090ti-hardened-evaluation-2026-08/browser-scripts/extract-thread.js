
return (() => {
  const post = document.querySelector('shreddit-post');
  const title = document.querySelector('h1')?.innerText || document.title || '';
  const body = post?.getAttribute('post-text') || post?.innerText ||
    document.querySelector('div[data-click-id="text"]')?.innerText || '';
  const comments = Array.from(document.querySelectorAll('shreddit-comment')).slice(0, 15).map(c => ({
    author: c.getAttribute('author') || 'anonymous',
    score: c.getAttribute('score') || '0',
    text: (c.innerText || '').trim().slice(0, 4000)
  })).filter(c => c.text.length > 20);
  const externalLinks = Array.from(document.querySelectorAll('a[href^="http"]'))
    .map(a => a.href.split('#')[0])
    .filter(h => !/reddit\.com|redd\.it|google\.com/.test(h));
  return JSON.stringify({
    canonical_url: window.location.href.split('#')[0].split('?')[0],
    title,
    author: post?.getAttribute('author') || null,
    post_body: body.slice(0, 12000),
    comments,
    external_links: Array.from(new Set(externalLinks)).slice(0, 50)
  });
})();
