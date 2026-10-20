from pathlib import Path
import json, html
root=Path(__file__).parent
D=root/'dist'
# Bibliographic records transcribed from the supplied public Google Scholar profile on 2026-10-20.
rows=[
('HiLoc: A Hierarchical Representation Method for Spatial Localization in Multimodal Large Language Models','Evelyn Zhang, Fufu Yu, Hanjun Li, Aoqi Wu, Ke Yan, Shouhong Ding, Tianhe Ren, Xinting Hu, Xiaojuan Qi, Li Jiang, Jiaya Jia','NeurIPS',2026,'hiloc','Vision',True,''),
('Focused Forcing: Content-Aware Per-Frame KV Selection for Efficient Autoregressive Video Diffusion','P Cai, E Zhang, J Liu, H Lin, R Zhang, W Mo, Y Ma, S Zheng, J Huang, et al.','NeurIPS',2026,'UebtZRa9Y70C','Generation',True,''),
('WorldCast: Distributed Multiplayer World Models','Z Ye, J Huang, E Zhang, Z Xie, R Zhang, B Han, L Ban, Z Wang, X Hu, et al.','arXiv:2610.12412',2026,'3fE2CSJIrl8C','Generation',False,''),
('D²Pruner: Debiased Importance and Structural Diversity for MLLM Token Pruning','E Zhang, F Yu, A Wu, Z Wen, K Yan, S Ding, B Qi, L Zhang','AAAI',2026,'LkGwnXOMwfcC','Efficiency',True,'D2Pruner'),
('Rethinking Token-wise Feature Caching: Accelerating Diffusion Transformers with Dual Feature Caching','C Zou, S Zheng, E Zhang, R Guo, H Xu, Z Shi, C He, X Hu, L Zhang','IEEE Transactions on Image Processing',2026,'hqOjcs7Dif8C','Efficiency',True,''),
('A Survey of Linear Attention: Algorithm, Theory, Application, and Infrastructure','Y Zhang, W Sun, W Ding, S Sun, R Xie, H Wang, J Chen, J Liu, S Wang, et al.','Transactions on Machine Learning Research',2026,'5nxA0vEk-isC','Efficiency',False,''),
('Reinforcement Learning-driven Diffusion Models: Language, Vision, and Beyond','Z Ma, J Wei, T Wang, H Wang, J Pan, H Xu, L Zhao, R Liu, Y Wang, et al.','IEEE Transactions on Pattern Analysis and Machine Intelligence',2026,'kNdYIx-mwKoC','Generation',False,''),
('NC2C: Automated Convexification of Generic Non-Convex Optimization Problems','X Peng, Y Liu, Y Cang, Y Zhang, X Wang, S Deng, J Cao','arXiv:2601.04789',2026,'8k81kl-MbHgC','Reasoning',False,''),
('AMID: Model-Agnostic Dataset Distillation by Adversarial Mutual Information Minimization','A Wu, J Liu, Y Zhang, W Huang, L Hu, Y Yang, Q Zhang, J Miao, Y Tang, et al.','The ACM Web Conference',2026,'0EnyYjriUFMC','Vision',False,''),
('Training-free and Hardware-friendly Acceleration for Diffusion Models via Similarity-based Token Pruning','E Zhang, J Tang, X Ning, L Zhang','AAAI',2025,'roLk4NBRz8UC','Efficiency',True,'SiTo'),
('CPA-enhancer: Chain-of-thought Prompted Adaptive Enhancer for Downstream Vision Tasks under Unknown Degradations','Y Zhang, Y Wu, Y Liu, X Peng','ICASSP',2025,'Y0pCki6q_DkC','Vision',True,''),
('RamIR: Reasoning and Action Prompting with Mamba for All-in-one Image Restoration','A Tang, Y Wu, Y Zhang','Applied Intelligence',2025,'IjCSPb-OGe4C','Vision',False,''),
('DP-MemArc: Differential Privacy Transfer Learning for Memory Efficient Language Models','Y Liu, X Peng, Y Zhang, X Ke, S Deng, J Cao, C Ma, M Fu, X Zhang, et al.','AAAI',2025,'zYLM7Y9cAGgC','Efficiency',False,''),
('Token Pruning for Caching Better: 9 Times Acceleration on Stable Diffusion for Free','E Zhang, B Xiao, J Tang, Q Ma, C Zou, X Ning, X Hu, L Zhang','arXiv:2501.00375',2024,'Se3iqnhoufwC','Efficiency',True,'DaTo'),
('Tool-Planner: Dynamic Solution Tree Planning for Large Language Model with Tool Clustering','Y Liu, X Peng, Y Zhang, J Cao, X Zhang, S Cheng, X Wang, J Yin, T Du','arXiv:2406.03807',2024,'2osOgNQ5qMEC','Reasoning',False,''),
('MemDPT: Differential Privacy for Memory Efficient Language Models','Y Liu, X Peng, J Cao, Y Zhang, C Ma, S Deng, M Fu, X Zhang, S Cheng, et al.','CoRR',2024,'qjMakFHDy7sC','Efficiency',False,''),
]
papers=[dict(zip(['title','authors','venue','year','id','topic','selected','code'],r)) for r in rows]
media_path = root/'paper-media.json'
paper_media = json.loads(media_path.read_text()) if media_path.exists() else {}
for paper in papers:
 paper.update(paper_media.get(paper['id'], {}))
 if paper['id'] == 'hiloc':
  paper.update(paperUrl='https://github.com/YuweiZhang2002/HiLoc/blob/main/paper/HiLoc.pdf', projectUrl='https://yuweizhang2002.github.io/HiLoc/')
(D/'assets/papers.js').write_text('window.PAPERS = '+json.dumps(papers,ensure_ascii=False)+';\n')
text={
'en':dict(lang='en',nav=['About','Research','Publications','Code','Contact'],over='COMPUTER VISION · MULTIMODAL LEARNING',sub='Evelyn Zhang',alias='Publications also appear under Yuwei Zhang',intro='Exploring efficient visual intelligence.',bio='My research focuses on computer vision, multimodal learning, and diffusion models. I am interested in making generative and multimodal systems more efficient through token pruning, feature caching, and better use of visual information.',aff='Tongji University · Shanghai, China',scholar='Google Scholar',contact='Get in touch',about='A little about me',aboutbody='My work spans efficient diffusion inference, multimodal token selection, and robust visual understanding. Across these topics, I explore how models can retain useful information while reducing redundant computation.',affnote='Affiliation listed on Google Scholar: Tongji University.',research='Research interests',researchsub='Three connected directions.',rnames=['Efficient generation','Multimodal intelligence','Robust visual understanding'],rdesc=['Token pruning and feature caching for diffusion models and transformers.','Visual token selection, multimodal reasoning, and efficient attention.','Image enhancement, restoration, and visual perception under degradations.'],pubs='Publications',pubsub='Selected work and publications.',filters=['Selected','All publications','Efficiency','Generation','Vision','Reasoning'],search='Search titles, authors, or venues',paper='Paper',code='Code',empty='No publications match this search.',projects='Open-source projects',projectsub='From research ideas to reproducible code.',pdesc=['Similarity-based token pruning for training-free diffusion acceleration.','Dynamic token pruning combined with caching for Stable Diffusion.','Debiased importance and structural diversity for multimodal token pruning.'],repo='View repository',ctitle='Let’s exchange ideas.',cbody='For research discussions and collaboration, feel free to reach out.',footer='Academic homepage',updated='Publication records checked against Google Scholar · 20 October 2026',note='Years follow the Scholar profile; preprints may have a later publication date.',switch='中文',switchurl='zh/'),
'zh':dict(lang='zh-CN',nav=['关于我','研究方向','论文成果','开源代码','联系'],over='计算机视觉 · 多模态学习',sub='张煜玮',alias='论文署名：Evelyn Zhang / Yuwei Zhang',intro='探索更高效的视觉智能。',bio='我的研究聚焦计算机视觉、多模态学习与扩散模型，关注如何通过 Token 剪枝、特征缓存以及更有效的视觉信息利用，提升生成模型与多模态系统的效率。',aff='同济大学 · 中国上海',scholar='谷歌学术',contact='联系我',about='关于我',aboutbody='我的工作涵盖高效扩散推理、多模态 Token 选择和鲁棒视觉理解。我关注这些方向中的共同问题：如何在减少冗余计算的同时，保留对模型真正有用的信息。',affnote='Google Scholar 所列单位：同济大学。',research='研究方向',researchsub='三个相互关联的研究方向。',rnames=['高效生成模型','多模态智能','鲁棒视觉理解'],rdesc=['面向扩散模型与 Transformer 的 Token 剪枝及特征缓存。','视觉 Token 选择、多模态推理与高效注意力。','退化条件下的图像增强、图像恢复与视觉感知。'],pubs='论文成果',pubsub='代表性工作与论文列表。',filters=['代表作','全部论文','模型效率','生成模型','视觉理解','推理规划'],search='搜索论文标题、作者或发表刊会',paper='论文',code='代码',empty='没有找到匹配的论文。',projects='开源项目',projectsub='从研究想法到可复现的代码。',pdesc=['基于相似度的 Token 剪枝，实现无需训练的扩散模型加速。','结合动态 Token 剪枝与缓存，加速 Stable Diffusion 推理。','利用去偏重要性和结构多样性进行多模态 Token 剪枝。'],repo='查看代码仓库',ctitle='期待与你交流。',cbody='欢迎就研究问题与合作机会联系我。',footer='个人学术主页',updated='论文资料核对自 Google Scholar · 2026 年 10 月 20 日',note='年份沿用 Scholar 记录；预印本与正式发表年份可能不同。',switch='English',switchurl='../')}
education = {
 'en': [
  ('The Hong Kong University of Science and Technology', 'Hong Kong', 'Ph.D. in Computer Science', 'Sep 2026 – Jun 2030', 'Research: Embodied intelligence, world models', ''),
  ('Tongji University', 'Shanghai', 'Master’s in Computer Science', 'Sep 2023 – Mar 2026', 'Research: Computer vision, multimodal large language models', ''),
  ('Beijing Jiaotong University', 'Beijing', 'Bachelor’s in Computer Science', 'Sep 2019 – Jun 2023', '', ''),
 ],
 'zh': [
  ('香港科技大学', '香港', '计算机科学博士', '2026 年 9 月 — 2030 年 6 月', '研究方向：具身智能、世界模型', ''),
  ('同济大学', '上海', '计算机科学硕士', '2023 年 9 月 — 2026 年 3 月', '研究方向：计算机视觉、多模态大模型', ''),
  ('北京交通大学', '北京', '计算机科学学士', '2019 年 9 月 — 2023 年 6 月', '', ''),
 ],
}
experience = {
 'en': [
  ('Jun 2026 – Sep 2026', 'Tencent IEG', 'Intern', 'Game world models', ''),
  ('Jan 2026 – May 2026', 'The University of Hong Kong', 'Research Assistant', '', 'Advisor: Prof. Xiaojuan Qi'),
  ('Feb 2025 – May 2026', 'Tencent Youtu Lab', 'Intern', 'Multimodal large language models', ''),
  ('Jun 2024 – Sep 2025', 'Shanghai Jiao Tong University', 'Research Assistant', 'Efficient AI', 'Advisor: Prof. Linfeng Zhang'),
  ('Mar 2024 – Jun 2024', 'Intel', 'Intern', 'Fine-tuning multimodal large language models', ''),
 ],
 'zh': [
  ('2026.06 — 2026.09', '腾讯 IEG', '实习生', '游戏世界模型', ''),
  ('2026.01 — 2026.05', '香港大学', '研究助理', '', '导师：齐晓娟老师'),
  ('2025.02 — 2026.05', '腾讯优图实验室', '实习生', '多模态大模型', ''),
  ('2024.06 — 2025.09', '上海交通大学', '研究助理', 'Efficient AI', '导师：张林峰老师'),
  ('2024.03 — 2024.06', '英特尔', '实习生', '多模态大模型微调', ''),
 ],
}
# Background and experience supplied by the owner.
text['en']['aff'] = 'Ph.D. student · HKUST CSE'
text['zh']['aff'] = '博士研究生 · 香港科技大学 CSE'
text['en']['aboutbody'] = 'I am a first-year Ph.D. student in the Department of Computer Science and Engineering (CSE) at the Hong Kong University of Science and Technology (HKUST), advised by <a href="https://jiaya.me/home" target="_blank" rel="noopener">Prof. Jiaya Jia</a>. I am also fortunate to be co-supervised by <a href="https://llijiang.github.io/" target="_blank" rel="noopener">Prof. Li Jiang</a>.'
text['zh']['aboutbody'] = '我是香港科技大学计算机科学与工程系（CSE）的博士一年级学生，导师是<a href="https://jiaya.me/home" target="_blank" rel="noopener">贾佳亚教授</a>。幸运的是，我同时还得到联合导师<a href="https://llijiang.github.io/" target="_blank" rel="noopener">蒋理教授</a>的指导。'
text['en']['affnote'] = 'Previously, I received my master’s degree from Tongji University and my bachelor’s degree from Beijing Jiaotong University.'
text['zh']['affnote'] = '在此之前，我在同济大学获得硕士学位，在北京交通大学获得本科学位。'
text['en']['over'] = 'WORLD MODELS · MULTIMODAL LLMS · EFFICIENT AI'
text['zh']['over'] = '世界模型 · 多模态大模型 · EFFICIENT AI'
text['en']['bio'] = 'My research interests are world models for games and embodied intelligence, multimodal large language models, and efficient AI.'
text['zh']['bio'] = '我的研究兴趣包括世界模型（游戏世界模型与具身世界模型）、多模态大模型，以及 Efficient AI。'
text['en']['rnames'] = ['World models', 'Multimodal LLMs', 'Efficient AI']
text['zh']['rnames'] = ['世界模型', '多模态大模型', 'Efficient AI']
text['en']['rdesc'] = ['World models for games and embodied intelligence.', 'Multimodal understanding and reasoning with large language models.', 'Efficient model inference through token pruning and feature caching.']
text['zh']['rdesc'] = ['游戏世界模型与具身世界模型。', '多模态大模型的理解与推理。', '通过 Token 剪枝与特征缓存提升模型推理效率。']
text['en']['nav'].insert(1, 'Education')
text['zh']['nav'].insert(1, '教育背景')
text['en']['nav'][4] = 'Experience'
text['zh']['nav'][4] = '实习经历'
text['en']['experience'] = 'Internships & Research Experience'
text['zh']['experience'] = '实习经历'
text['en']['updated'] = 'Last updated · 20 October 2026'
text['zh']['updated'] = '最近更新 · 2026 年 10 月 20 日'
text['en']['note'] = 'Figures are reproduced from the papers or authors’ project pages. Click an overview to enlarge it and view its source.'
text['zh']['note'] = '配图摘自论文或作者项目主页。点击 Overview 可放大查看，并访问原始来源。'
school_logos = ['hkust.svg', 'tongji.png', 'bjtu.png']
scholar='https://scholar.google.com/citations?user=renmzGoAAAAJ&hl=en'
for lang,t in text.items():
 prefix='../' if lang=='zh' else ''
 nav=''.join(f'<a href="#{s}">{n}</a>' for s,n in zip(['about','education','research','publications','experience','contact'],t['nav']))
 education_html = ''.join(
  f'<article class="education-entry"><div class="education-date">{dates}</div><div class="education-detail"><div class="school-logo-wrap"><img class="school-logo school-logo-{i}" src="{prefix}assets/schools/{school_logos[i]}" alt="{school} Logo" width="112" height="64" loading="lazy"></div><div class="school-copy"><div class="school-line"><h3>{school}</h3><span>{city}</span></div><p class="degree">{degree}</p>'
  + (f'<p class="education-focus">{focus}</p>' if focus else '')
  + (f'<p class="education-advisor">{advisor}</p>' if advisor else '')
  + '</div></div></article>' for i,(school,city,degree,dates,focus,advisor) in enumerate(education[lang])
 )
 research=''.join(f'<article><span class="number">0{i+1}</span><h3>{n}</h3><p>{t["rdesc"][i]}</p></article>' for i,n in enumerate(t['rnames']))
 experience_html = ''.join(
  f'<article class="experience-entry"><div class="experience-date">{dates}</div><div class="experience-detail"><h3>{organization}</h3><p class="experience-role">{role}</p>'
  + (f'<p class="experience-mentor">{mentor}</p>' if mentor else '')
  + (f'<p class="experience-focus">{focus}</p>' if focus else '')
  + '</div></article>' for dates,organization,role,focus,mentor in experience[lang]
 )
 filters=''.join(f'<button type="button" data-filter="{v}" aria-pressed="{str(i==0).lower()}">{n}</button>' for i,(v,n) in enumerate(zip(['selected','all','Efficiency','Generation','Vision','Reasoning'],t['filters'])))
 noscript=''.join(f'<p><a href="{html.escape(p.get("paperUrl") or scholar+"&view_op=view_citation&citation_for_view=renmzGoAAAAJ:"+p["id"])}">{html.escape(p["title"])}</a> — {p["venue"]}, {p["year"]}</p>' for p in papers)
 page=f'''<!doctype html>
<html lang="{t['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{t['bio']}"><meta name="theme-color" content="#f8f7f4"><title>{t['sub']} — {t['footer']}</title><link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/style.css"><script defer src="{prefix}assets/papers.js"></script><script defer src="{prefix}assets/app.js"></script></head>
<body data-language="{lang}"><a class="skip" href="#main">{'跳至正文' if lang=='zh' else 'Skip to content'}</a><header><a class="wordmark" href="{prefix or './'}">EZ<span>.</span></a><nav aria-label="{'主导航' if lang=='zh' else 'Main navigation'}">{nav}</nav><a class="language" href="{t['switchurl']}" lang="{'en' if lang=='zh' else 'zh-CN'}">{t['switch']} <span aria-hidden="true">↗</span></a></header>
<main id="main"><section class="hero" aria-labelledby="name"><div class="hero-copy"><p class="eyebrow">{t['over']}</p><h1 id="name">{t['sub']}<span>{"Evelyn Zhang" if lang=="zh" else "张煜玮"}</span></h1><p class="alias">{t['alias']}</p><h2>{t['intro']}</h2><p class="intro">{t['bio']}</p><div class="hero-links"><a class="primary" href="{scholar}" target="_blank" rel="noopener">{t['scholar']} ↗</a><a href="https://github.com/YuweiZhang2002" target="_blank" rel="noopener">GitHub ↗</a><a href="#contact">{t['contact']} →</a></div></div><aside class="portrait-wrap"><div class="portrait-frame"><img src="{prefix}assets/portrait.jpg" alt="Evelyn Zhang / 张煜玮" width="240" height="300"></div><div class="portrait-caption"><span class="dot"></span>{t['aff']}</div><span class="portrait-note">VISION / GENERATION / EFFICIENCY</span></aside></section>
<section id="about" class="about section"><div class="section-label">01 / {t['about']}</div><div><p class="about-text">{t['aboutbody']}</p><p class="muted">{t['affnote']}</p></div></section>
<section id="education" class="section"><div class="section-heading"><div><p class="section-label">02 / EDUCATION</p><h2>{"教育背景" if lang=="zh" else "Education"}</h2></div></div><div class="education-list">{education_html}</div></section>
<section id="research" class="section"><div class="section-heading"><div><p class="section-label">03 / RESEARCH</p><h2>{t['research']}</h2></div><p>{t['researchsub']}</p></div><div class="research-grid">{research}</div></section>
<section id="publications" class="section"><div class="section-heading"><div><p class="section-label">04 / PUBLICATIONS</p><h2>{t['pubs']}</h2></div><a href="{scholar}" target="_blank" rel="noopener">{t['scholar']} ↗</a></div><p class="muted">{t['pubsub']}</p><div class="publication-tools"><div class="filters" role="group" aria-label="{'论文分类' if lang=='zh' else 'Publication filters'}">{filters}</div><label class="search"><span aria-hidden="true">⌕</span><input id="search" type="search" placeholder="{t['search']}" aria-label="{t['search']}"></label></div><p id="result-count" role="status" aria-live="polite"></p><div id="papers"></div><noscript>{noscript}</noscript><p class="data-note">{t['note']}</p></section>
<section id="experience" class="section"><div class="section-heading"><div><p class="section-label">05 / EXPERIENCE</p><h2>{t['experience']}</h2></div></div><div class="experience-list">{experience_html}</div></section>
<section id="contact" class="contact section"><div><p class="section-label">06 / CONTACT</p><h2>{t['ctitle']}</h2><p>{t['cbody']}</p></div><a class="email" href="mailto:evelynzhang2002@163.com">evelynzhang2002@163.com <span>↗</span></a></section></main><footer><span>© 2026 {t['sub']}</span><span>{t['updated']}</span><a href="#">↑ {'回到顶部' if lang=='zh' else 'Back to top'}</a></footer>
<dialog id="figure-dialog" aria-labelledby="figure-title"><div class="figure-toolbar"><p id="figure-title"></p><button type="button" id="close-figure" aria-label="{'关闭图片' if lang=='zh' else 'Close figure'}">×</button></div><div class="figure-stage"><img id="figure-image" alt=""></div><div class="figure-footer"><p id="figure-caption"></p><a id="figure-source" target="_blank" rel="noopener">{'查看图片来源' if lang=='zh' else 'View figure source'} ↗</a></div></dialog></body></html>'''
 out=D/('zh/index.html' if lang=='zh' else 'index.html');out.parent.mkdir(exist_ok=True);out.write_text(page)
(D/'.nojekyll').touch()
