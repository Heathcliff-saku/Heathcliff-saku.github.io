---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
I am a Ph.D. candidate in the [Institute of Artificial Intelligence](https://iai.buaa.edu.cn/), [Beihang(BUAA) University](https://www.buaa.edu.cn/) <img src='./images/buaa.png' style='width: 2em;'>, advised by Prof. [**Xingxing Wei(韦星星)**](https://sites.google.com/site/xingxingwei1988/) and co-mentored by Prof. [Hang Su(苏航)](https://www.suhangss.me/) and Dr. [Yinpeng Dong(董胤蓬)](https://ml.cs.tsinghua.edu.cn/~yinpeng/). Before that, I received my B.E. degree in Intelligent Science & Technology from [School of Artificial Intelligence](https://sai.xidian.edu.cn/), [Xidian(XDU) University](https://www.xidian.edu.cn/) <img src='./images/xdu.png' style='width: 2em;'>.

I received the national scholarship in 2021 at Xidian University. I was a research summer intern in 2021 at Digital Team, [Dell Technologies(China) Co](https://www.dell.com/zh-cn) <img src='./images/dell.png' style='width: 6em;'>, mentored by SSE. Xuejin Liang. I was a research intern in 2022 at [RealAI](https://www.realai.eu/) <img src='./images/realai.png' style='width: 2em;'>, mentored by Dr. Yinpeng Dong.

I'm a AI beginner with interest includes adversarial robustness and natural robustness for deep learning. If you have any suggestions or questions about our works, please feel free to email me: [shouweiruan@buaa.edu.cn](shouweiruan@buaa.edu.cn).

# 🔥 News
- *2022.02*: &nbsp;✨ there is no news

# 📝 Publications 

**🛩️ Chapter-1: Viewpoint Robustness and Invariance of Visual Systems**\\
In the field of computer vision, viewpoint robustness and invariance present a longstanding challenge. This requires visual models to have the same response or representation to inputs from different viewpoints. To achieve this, we have made a series of efforts, including constructing the first adversarial viewpoint benchmark (ImageNet-V/ImageNet-V+), adversarial viewpoint optimization methods (ViewFool), and adversarial training framework that enhances viewpoint invariance (VIAT). The related work is showcased as follows:

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Journal Version, Under Review</div><img src='images/viat_2.png' alt="sym" width="90%"></div></div>
<div class='paper-box-text' markdown="1">
**Improving Viewpoint Robustness for Visual Recognition via Adversarial Training**\\
**Shouwei Ruan**, Yinpeng Dong, Hang Su, Jianteng Peng, Ning Chen, Xingxing Wei\\
💾[**Project**](https://arxiv.org/pdf/2307.10235.pdf) 📃[**Paper**](https://arxiv.org/pdf/2307.11528.pdf)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV2023, Accepted</div><img src='images/viat.png' alt="sym" width="90%"></div></div>
<div class='paper-box-text' markdown="1">
**Towards Viewpoint-Invariant Visual Recognition via Adversarial Training**\\
**Shouwei Ruan**, Yinpeng Dong, Hang Su, Jianteng Peng, Ning Chen, Xingxing Wei\\
💾[**Project**](https://arxiv.org/pdf/2307.10235.pdf) 📃[**Paper**](https://arxiv.org/pdf/2307.10235.pdf)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS2022, Accepted</div><img src='images/viewfool.png' alt="sym" width="90%"></div></div>
<div class='paper-box-text' markdown="1">
**ViewFool: Evaluating the Robustness of Visual Recognition to Adversarial Viewpoints**\\
Yinpeng Dong, **Shouwei Ruan**, Hang Su, Caixin Kang, Xingxing Wei, Jun Zhu\\
💾[**Project**](https://github.com/Heathcliff-saku/ViewFool_) 📃[**Paper**](https://arxiv.org/pdf/2210.03895.pdf)
</div>
</div>

**🛩️ Chapter-2: Adversarial Robustness: Attack and Defense**\\
We primarily focuses on attack and defense methods against adversarial patches, as well as on the generation of 3D adversarial textures.

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR2024, Accepted</div><img src='images/tt3d.png' alt="sym" width="90%"></div></div>
<div class='paper-box-text' markdown="1">
**Towards Transferable Targeted 3D Adversarial Attack in the Physical World**\\
Yao Huang, Yinpeng Dong, **Shouwei Ruan**, Xiao Yang, Hang Su, Xingxing Wei\\
📃[**Paper**](https://arxiv.org/pdf/2312.09558.pdf)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Journal Version, Under Review</div><img src='images/dopatch.png' alt="sym" width="90%"></div></div>
<div class='paper-box-text' markdown="1">
**Distributional Modeling for Location-Aware Adversarial Patches**\\
Xingxing Wei, **Shouwei Ruan**, Yinpeng Dong, and Hang Su\\
💾[**Project**](https://github.com/heathcliff-saku/dopatch) 📃[**Paper**](https://arxiv.org/pdf/2306.16131.pdf)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV2024, Under Review</div><img src='images/diffender.png' alt="sym" width="90%"></div></div>
<div class='paper-box-text' markdown="1">
**DIFFender: Diffusion-Based Adversarial Defense against Patch Attacks in the Physical World**\\
Caixin Kang, Yinpeng Dong, Zhengyi Wang, **Shouwei Ruan**, Hang Su, Xingxing Wei\\
📃[**Paper**](https://arxiv.org/html/2306.09124v3)
</div>
</div>

# 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 

# 📖 Educations
- *2019.06 - 2022.04 (now)*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2015.09 - 2019.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 

# 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)

# 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China.
