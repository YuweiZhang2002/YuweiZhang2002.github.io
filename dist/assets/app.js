'use strict';
const zh = document.body.dataset.language === 'zh';
const papers = window.PAPERS;
let active = 'selected';
const escapeHTML = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function render(){
 const query = document.querySelector('#search').value.trim().toLowerCase();
 const shown = papers.filter(p => (active === 'all' || (active === 'selected' ? p.selected : p.topic === active)) && `${p.title} ${p.authors} ${p.venue} ${p.year}`.toLowerCase().includes(query));
 document.querySelector('#result-count').textContent = zh ? `${shown.length} 条成果记录` : `${shown.length} publication records`;
 document.querySelector('#papers').innerHTML = shown.length ? shown.map(p => {
 const href = `https://scholar.google.com/citations?view_op=view_citation&user=renmzGoAAAAJ&citation_for_view=renmzGoAAAAJ:${p.id}`;
 const authors = escapeHTML(p.authors).replace(/\b(E Zhang|Y Zhang)\b/g,'<strong>$1</strong>');
 return `<article class="paper"><div class="year">${p.year}</div><div><h3><a href="${href}" target="_blank" rel="noopener">${escapeHTML(p.title)}</a></h3><p class="authors">${authors}</p><div class="paper-meta"><span class="venue">${escapeHTML(p.venue)} ${p.venue.includes(String(p.year)) ? '' : '· '+p.year}</span><a href="${href}" target="_blank" rel="noopener">${zh?'论文':'Paper'} ↗</a>${p.code ? `<a href="https://github.com/YuweiZhang2002/${p.code}" target="_blank" rel="noopener">${zh?'代码':'Code'} ↗</a>` : ''}</div></div></article>`;
 }).join('') : `<p class="muted">${zh?'没有找到匹配的论文。':'No publications match this search.'}</p>`;
}
document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click',()=>{
 active = button.dataset.filter;
 document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
 render();
}));
document.querySelector('#search').addEventListener('input',render);
render();
