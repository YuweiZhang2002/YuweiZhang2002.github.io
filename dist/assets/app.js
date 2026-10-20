'use strict';
const zh = document.body.dataset.language === 'zh';
const assetBase = zh ? '../' : './';
const papers = window.PAPERS;
let active = 'selected';
const escapeHTML = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function render(){
 const query = document.querySelector('#search').value.trim().toLowerCase();
 const shown = papers.filter(p => (active === 'all' || (active === 'selected' ? p.selected : p.topic === active)) && `${p.title} ${p.authors} ${p.venue} ${p.year}`.toLowerCase().includes(query));
 document.querySelector('#result-count').textContent = zh ? `${shown.length} 条成果记录` : `${shown.length} publication records`;
 document.querySelector('#papers').innerHTML = shown.length ? shown.map(p => {
 const href = p.paperUrl || `https://scholar.google.com/citations?view_op=view_citation&user=renmzGoAAAAJ&citation_for_view=renmzGoAAAAJ:${p.id}`;
 const authors = escapeHTML(p.authors).replace(/\b(Evelyn Zhang|E Zhang|Y Zhang)\b/g,'<strong>$1</strong>');
 const overview = p.image ? `<button class="paper-overview" type="button" data-figure="${escapeHTML(p.id)}" aria-label="${zh?'放大论文概览图：':'Enlarge overview: '}${escapeHTML(p.title)}"><span class="overview-image"><img src="${assetBase}${escapeHTML(p.thumbnail || p.image)}" alt="${zh?'论文概览图：':'Overview of '}${escapeHTML(p.title)}" width="520" height="320" loading="lazy" decoding="async"></span><span class="overview-label">Overview <span aria-hidden="true">⤢</span></span></button>` : `<div class="overview-unavailable"><span>${zh?'原论文图片待补充':'Paper figure pending'}</span><a href="${href}" target="_blank" rel="noopener">${zh?'查看论文':'View paper'} ↗</a></div>`;
 return `<article class="paper">${overview}<div class="paper-content"><p class="paper-year">${p.year}</p><h3><a href="${escapeHTML(href)}" target="_blank" rel="noopener">${escapeHTML(p.title)}</a></h3><p class="authors">${authors}</p><div class="paper-meta"><span class="venue">${escapeHTML(p.venue)} ${p.venue.includes(String(p.year)) ? '' : '· '+p.year}</span><a href="${escapeHTML(href)}" target="_blank" rel="noopener">${zh?'论文':'Paper'} ↗</a>${p.code ? `<a href="https://github.com/YuweiZhang2002/${escapeHTML(p.code)}" target="_blank" rel="noopener">${zh?'代码':'Code'} ↗</a>` : ''}${p.projectUrl ? `<a href="${escapeHTML(p.projectUrl)}" target="_blank" rel="noopener">${zh?'项目主页':'Project'} ↗</a>` : ''}</div></div></article>`;
 }).join('') : `<p class="muted">${zh?'没有找到匹配的论文。':'No publications match this search.'}</p>`;
}
document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click',()=>{
 active = button.dataset.filter;
 document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
 render();
}));
document.querySelector('#search').addEventListener('input',render);
const dialog = document.querySelector('#figure-dialog');
document.querySelector('#papers').addEventListener('click', event => {
 const button = event.target.closest('[data-figure]');
 if (!button) return;
 const paper = papers.find(p => p.id === button.dataset.figure);
 if (!paper?.image) return;
 document.querySelector('#figure-title').textContent = paper.title;
 const img = document.querySelector('#figure-image');
 img.src = assetBase + paper.image;
 img.alt = `${zh?'论文概览图：':'Overview of '}${paper.title}`;
 document.querySelector('#figure-caption').textContent = paper.caption || '';
 document.querySelector('#figure-source').href = paper.sourceUrl || paper.paperUrl;
 dialog.showModal();
 document.body.classList.add('figure-open');
});
document.querySelector('#close-figure').addEventListener('click', () => dialog.close());
dialog.addEventListener('close', () => document.body.classList.remove('figure-open'));
dialog.addEventListener('click', event => {
 if (event.target !== dialog) return;
 const r = dialog.getBoundingClientRect();
 if(event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) dialog.close();
});
render();
