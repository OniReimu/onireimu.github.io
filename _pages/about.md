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

I am a [Lecturer](https://www.wikiwand.com/en/articles/Academic_ranks_(Australia_and_New_Zealand)) at [University of Technology Sydney](https://www.uts.edu.au/about/faculty-engineering-and-information-technology) where I also obtained my PhD. Before that, I was a Postdoctoral Fellow at the [CSIRO Data61](https://www.csiro.au/en/research/technology-space?start=0&count=12) working with [Dr. Xiwei Xu](https://scholar.google.com/citations?user=x9IUq78AAAAJ), [Prof. Shiping Chen](https://scholar.google.com/citations?user=z4We1-UAAAAJ), and [Dr. Wei Ni](https://scholar.google.com/citations?user=GMS201gAAAAJ). I received my B.Eng. and M.Eng. degrees in Telecommunication Network Engineering from the [University of New South Wales](https://www.unsw.edu.au/engineering/our-schools/electrical-engineering-telecommunications).

I have expertise in the reliability, trust, and scalability of data management systems, with a focus on security and privacy analysis in ML, including attacks and defenses, machine unlearning, incentivized/decentralized ML, and privacy-preserving blockchains. I have published 50+ papers at the top international journals and conferences with total <a href='https://scholar.google.com/citations?user=oMUYCk0AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

If you are interested in my research and keen to collaborate or discuss potential PhD opportunities, please feel free to contact me via email. Much welcome!


# 🔥 News
- *15.10.2025*: &nbsp;🌟 We’re beyond excited! 🌟
Absolutely thrilled to share that our paper, [Split Unlearning](https://dl.acm.org/doi/10.1145/3719027.3744787), has been recongized with the 🏆 **Distinguished Paper Award** at **ACM CCS'25**!
- *24.06.2025*: &nbsp;🎉🎉 Thrilled to announce that our paper, [Is Your AI Truly Yours? Leveraging Blockchain for Copyrights, Provenance, and Lineage](https://ieeexplore.ieee.org/document/11071388), has been accepted by **IEEE Transactions on Service Computing (TSC)**!
- *16.06.2025*: &nbsp;🎉🎉 Thrilled to announce that our paper, [BlockFUL: Enabling Unlearning in Blockchained Federated Learning](https://ieeexplore.ieee.org/document/11050955), has been accepted by **IEEE Transactions on Information Forensics & Security (TIFS)**!
- *04.06.2025*: &nbsp;🎉🎉 Thrilled to announce that our paper, [Understanding BRC-20: Hope or Hype](https://ieeexplore.ieee.org/document/11077736), has been accepted by **IEEE Transactions on Computational Social Systems (TCSS)**!
- *25.05.2025*: &nbsp;🎉🎉 Thrilled to announce that our paper, [Maximizing NFT Incentives: References Make You Rich](https://ieeexplore.ieee.org/abstract/document/11031201), has been accepted by **IEEE Transactions on Service Computing (TSC)**!
- *01.05.2025*: &nbsp;🎉🎉 Thrilled to announce that our paper, [RobustLight:Improving Robustness via Diffusion Reinforcement Learning for Traffic Signal Control](https://openreview.net/forum?id=YGjd2xw98G), has been accepted by **ICML'25**!
- *17.02.2025*: &nbsp;🎉🎉 Thrilled to announce that our paper, [Understanding DAOs: An Empirical Study on Governance Dynamics](https://ieeexplore.ieee.org/document/10891558), has been published online in **IEEE Transactions on Computational Social Systems (TCSS)**!
- *04.01.2025*: &nbsp;🎉🎉 Thrilled to announce that our paper, [CAN-Trace Attack: Exploit CAN Messages to Uncover Driving Trajectories](https://ieeexplore.ieee.org/abstract/document/10858595), has been accepted by **IEEE Transactions on Intelligent Transportation Systems (TITS)**! Congrats to my PhD student, [Xiaojie Lin](https://scholar.google.com/citations?user=TH9WESkAAAAJ)!

# 📝 Publications

## 👾 AI, AI-Cybersecurity, AI4Blockchain, Blockchain4AI

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CCS'25</div><img src='images/paper_split.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Split Unlearning](https://dl.acm.org/doi/10.1145/3719027.3744787) 🏆 **(Distinguished Paper Award)**

**Guangsheng Yu**, Yanna Jiang, Qin Wang, Xu Wang, Baihe Ma, Caijun Sun, Wei Ni, Ren Ping Liu.

- This work is the first to propose, implement, and evaluate a practical unlearning framework for split learning.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TNNLS</div><img src='images/paper_ironforge.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[IronForge: An Open, Secure, Fair, Decentralized Federated Learning](https://ieeexplore.ieee.org/abstract/document/10323597)

**Guangsheng Yu**, Xu Wang, Caijun Sun, Qin Wang, Ping Yu, Wei Ni, Ren Ping Liu.

<!-- [**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong> -->
- This work is an implementation of [*ERC-5521*](https://eips.ethereum.org/EIPS/eip-5521) in an AI context.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML'25</div><img src='images/paper_robustlight.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[RobustLight: Improving Data Quality via Diffusion Reinforcement Learning for Traffic Signal Control](https://openreview.net/forum?id=YGjd2xw98G)

Mingyuan Li, Jiahao Wang, **Guangsheng Yu**, et al.

- This work makes novel use of diffusion models to address advesrail attack and missing data in real-world traffic signal control systems.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TIFS</div><img src='images/paper_fisher.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Parallel Unlearning in Inherited Model Networks](https://ieeexplore.ieee.org/document/11224866)

Xiao Liu, Mingyuan Li, **Guangsheng Yu**, et al.

- This work is the first-ever to achieve fully parallel unlearning across models that are interlinked.
</div>
</div>

- **[TIFS]** [BlockFUL: Enabling Unlearning in Blockchained Federated Learning](https://ieeexplore.ieee.org/document/11050955), Xiao Liu, Mingyuan Li, **Guangsheng Yu**, Xu Wang, et al. 2025.

- **[TSC]** [Is Your AI Truly Yours? Leveraging Blockchain for Copyrights, Provenance, and Lineage](https://ieeexplore.ieee.org/document/11071388), Qin Wang, **Guangsheng Yu**, et al. 2025.

- **[TOMM]** [NNFMAC: A Neural Network Fingerprinting-based Model Authentication Code Scheme](https://dl.acm.org/doi/10.1145/3778121), Haiyu Deng, Xu Wang, **Guangsheng Yu**, et al. 2025.

- **[FGCS]** [TDML - A Trustworthy Distributed Machine Learning Framework](https://www.sciencedirect.com/science/article/abs/pii/S0167739X25002468?via%3Dihub), Zhen Wang, Qin Wang, **Guangsheng Yu**, Shiping Chen. 2025.

- **[TSMC]** [Adaptive Resource Scheduling in Permissionless Sharded-Blockchains: A Decentralized Multiagent Reinforcement Learning Approach](https://ieeexplore.ieee.org/abstract/document/10201805), **Guangsheng Yu**, Xu Wang, et al. 2023.

- **[TIST]** [Obfuscating the Dataset: Impacts and Applications](https://dl.acm.org/doi/abs/10.1145/3597936), **Guangsheng Yu**, Xu Wang, et al. 2023.

- **[Neurocomputing]** [Preventing harm to the rare in combating the malicious: A filtering-and-voting framework with adaptive aggregation in federated learning](https://www.sciencedirect.com/science/article/pii/S0925231224010889), Yanna Jiang, Baihe Ma, Xu Wang, **Guangsheng Yu**, et al. 2024.

- **[CSUR]** [Blockchained Federated Learning for Internet of Things: A Comprehensive Survey](https://dl.acm.org/doi/full/10.1145/3659099), Yanna Jiang, Baihe Ma, Xu Wang, **Guangsheng Yu**, et al. 2024

- **[Computer Networks]** [TBDD: A New Trust-based, DRL-driven Framework for Blockchain Sharding in IoT](https://www.sciencedirect.com/science/article/pii/S1389128624001750), Zixu Zhang, **Guangsheng Yu**, et al. 2024.

## 💰 Blockchain and Web3

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TEM</div><img src='images/paper_abe.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Enabling Attribute Revocation for Fine-Grained Access Control in Blockchain-IoT Systems](https://ieeexplore.ieee.org/abstract/document/8989788)

**Guangsheng Yu**, Xuan Zha,Xu Wang, Wei Ni, Kan Yu, Ping Yu, J. Andrew Zhang, Ren Ping Liu, Y. Jay Guo.

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TCSS</div><img src='images/paper_servicenow.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Toward Web3 Applications: Easing the Access and Transition](https://ieeexplore.ieee.org/abstract/document/10505933)

**Guangsheng Yu**, Xu Wang, Qin Wang, Tingting Bi, Yifei Dong, Ren Ping Liu, Nektarios Georgalas, Andrew Reeves.

- This work is collaborated with [British Telecom](https://www.bt.com).
</div>
</div>

- **[TSC]** [Maximizing NFT Incentives: References Make You Rich](https://ieeexplore.ieee.org/abstract/document/11031201), **Guangsheng Yu**, Qin Wang, et al. 2025.

- **[TCSS]** [Understanding BRC-20: Hope or Hype](https://ieeexplore.ieee.org/document/11077736), **Guangsheng Yu**, Qin Wang, et al. 2025.

- **[TCSS]** [Understanding DAOs: An Empirical Study on Governance Dynamics](https://ieeexplore.ieee.org/document/10891558), Qin Wang, **Guangsheng Yu**, et al. 2025.

- **[TCSS]** [Cryptocurrency in the Aftermath: Unveiling the Impact of the SVB Collapse](https://ieeexplore.ieee.org/abstract/document/10522795), Qin Wang, **Guangsheng Yu**, Shiping Chen. 2024.

- **[IoTJ]** [Blockchain-Enabled Fish Provenance and Quality Tracking System](https://ieeexplore.ieee.org/abstract/document/9526860), Xu Wang, **Guangsheng Yu**, Ren Ping Liu, et al. 2021.

- **[Computer Communications]** [Capacity Analysis of Public Blockchain](https://www.sciencedirect.com/science/article/pii/S0140366421002437), Xu Wang, Wei Ni, Xuan Zha, **Guangsheng Yu**, Ren Ping Liu, et al. 2021.

- **[IPM]** [A Novel Dual-Blockchained Structure for Contract-theoretic LoRa-based Information Systems](https://www.sciencedirect.com/science/article/pii/S0140366421002437), **Guangsheng Yu**, Litianyi Zhang, Xu Wang, et al. 2021.

- **[Computer & Security]** [A Unified Analytical Model for Proof-of-X Schemes](https://www.sciencedirect.com/science/article/pii/S0167404820302108), **Guangsheng Yu**, Xuan Zha, Xu Wang, et al. 2020.

- **[Information Systems]** [Defining Blockchain Governance Principles: A Comprehensive Framework](https://www.sciencedirect.com/science/article/pii/S0306437922000758), Yue Liu, Qinghua, Lu, **Guangsheng Yu**, et al. 2022.

- **[IA]** [Survey: Sharding in Blockchains](https://ieeexplore.ieee.org/abstract/document/8954616), **Guangsheng Yu**, Xu Wang, et al. 2020.

- **[ICSA'23]** [A Pattern-oriented Reference Architecture for Governance-driven Blockchain Systems](https://ieeexplore.ieee.org/abstract/document/10092670), Yue Liu, Qinghua Lu, **Guangsheng Yu**, et al.

- **[EuroPLoP'22]** [A Pattern Language for Blockchain Governance](https://dl.acm.org/doi/abs/10.1145/3551902.3564802), Yue Liu, Qinghua Lu, **Guangsheng Yu**, et al.

- **[ICBC'23]** [Predicting NFT Classification with GNN: A Recommender System for Web3 Assets](https://ieeexplore.ieee.org/abstract/document/10174882), **Guangsheng Yu**, Qin Wang, et al.

- **[ICBC'23]** [A First Look into Blockchain DAOs](https://ieeexplore.ieee.org/abstract/document/10174961), Qin Wang, **Guangsheng Yu**, et al.

- **[ICBC'23]** [Leveraging Architectural Approaches in Web3 Applications - A DAO Perspective Focused](https://ieeexplore.ieee.org/abstract/document/10174988), **Guangsheng Yu**, Qin Wang, Tingting, Bi, et al.

- **[ICBC'23]** [A Referable NFT Scheme](https://ieeexplore.ieee.org/abstract/document/10174865), Qin Wang, **Guangsheng Yu**, et al.

- **[ICBC'22]** [Carboncoin: Blockchain Tokenization of Carbon Emissions with ESG-based Reputation](https://ieeexplore.ieee.org/abstract/document/9805516), Oscar Golding, **Guangsheng Yu**, et al.

- **[GLOBECOM'18]** [Attack and Defence of Ethereum Remote APIs](https://ieeexplore.ieee.org/abstract/document/8644498), Xu Wang, Xuan Zha, **Guangsheng Yu**, et al.

- **[GLOBECOM'18]** [An Optimized Round-Robin Scheduling of Speakers for Peers-to-Peers-Based Byzantine Faulty Tolerance](https://ieeexplore.ieee.org/abstract/document/8644251), **Guangsheng Yu**, Xu Wang, Xuan Zha, et al.

## 🚗 Applied Cybersecurity

- **[TITS]** [CAN-Trace Attack: Exploit CAN Messages to Uncover Driving Trajectories](https://ieeexplore.ieee.org/abstract/document/10858595), Xiaojie Lin, Baihe Ma, Xu Wang, **Guangsheng Yu**, et al. 2025.

- **[WCM]** [Accountability and Reliability in 6G O-RAN: Who is Responsible When it Fails?](https://ieeexplore.ieee.org/document/10944629?source=AUTHORALERT&dld=dXRzLmVkdS5hdQ%3D%3D), Ying He, **Guangsheng Yu**, Xu Wang, Qin Wang, et al. 2025.

- **[IoTJ]** [ByCAN: Reverse Engineering Controller Area Network (CAN) Messages From Bit to Byte Level](https://ieeexplore.ieee.org/abstract/document/10614332), Xiaojie Lin, Baihe Ma, Xu Wang, **Guangsheng Yu**, et al. 2024.



# 🎖 Honors and Awards
- *15.10.2025* [Split Unlearning](https://dl.acm.org/doi/10.1145/3719027.3744787) (ACM CCS'25, 🏆 Distinguished Paper Award)


# 📖 Standards

**We are deeply involved in the Ethereum community, contributing, collaborating, and growing together with this amazing ecosystem! 🚀✨💎🙌 #Ethereum**

- [[*ERC-5521*](https://eips.ethereum.org/EIPS/eip-5521)][[Webpage](https://www.r-nft.io)][[Doc](https://arxiv.org/pdf/2210.10910)], Referable NFT, Finalized!!!
- [[*ERC-7634*](https://eips.ethereum.org/EIPS/eip-7634)], Limited transfer count NFT, Draft.

# 💻 Teaching

- *Coord./Lect./Tut.*, 41900/42000 Cryptography, University of Technology Sydney. Large-scale course with over 450 students.
- *Coord./Lect./Tut.*, 48436/32309 Digital Forensics, University of Technology Sydney. Advanced course for Forensic students (Cybersecurity-oriented).
- *Coord./Lect./Tut.*, 41092 Network Fundamentals, University of Technology Sydney. Fundamentals course for all Cybersecurity students.
- *Coord./Lect.*, 65325 Digital Trace and Identity, University of Technology Sydney. Core course for Forensic students (Forensic-oriented).
- *Coord./Lect.*, 420108 Cybersecurity Management, University of Technology Sydney. OPM course for industry.
- *Tut.*, 43010 Cyber Threat Intelligence and Incident Response, University of Technology Sydney. SecOps course collaborated with [ThreatDefense](https://www.threatdefence.com).
- *Curric. Des.*, 43030 Professional Practice in Computing (Cybersecurity), University of Technology Sydney. Aimed for 500 students in two years.

# 💬 Invited Talks
- *2025.12*, Talk on “PoLO: Proof-of-Learning and Proof-of-Ownership at Once with Chained Watermark”, CRWA Meetup Melbourne.
- *2025.12*, Talk on “Split Unlearning”, CSIRO Data61.
- *2025.10*, Talk on “Split Unlearning”, ACM CCS Meetup Taipei.
- *2019*, Talk on “Attack and Defence of Ethereum Remote APIs”, Sydney Blockchain Centre.
- *2018.12*, Talk on “An Optimized Round-Robin Scheduling of Speakers for Peers-to-Peers-based Byzantine Faulty Tolerance”, IEEE GLOBECOM Meetup Abu Dhabi.

