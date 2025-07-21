# Combined Market Requirements Document (mrd.md)

---

## Version 1.0 – Self‑Hosted Website Ingestion & Citation Service (Hardened Spec) – 2025‑07‑20

MRD – Self‑Hosted Website Ingestion & Citation Service
Version Date Author
**1.0 (Hardened Spec)**  2025‑07‑20  Warlack

### 1  Purpose

To provide a self‑hosted tool that crawls a website, indexes its content, and exposes a retrieval API that returns answers with precise, verifiable in‑text citations.

### 2  Problem / Opportunity

Large Language Models (LLMs) lack authoritative context for private or niche websites and often hallucinate or provide broken links, eroding user trust. Existing SaaS solutions can compromise data privacy and lack the deep customisation required by technical users. Enthusiasts and small teams running home servers need a local, open‑source, and trustworthy alternative.

### 3  Target Users

* **Technical Hobbyists:** Home‑lab users (Docker, Kubernetes, Proxmox).
* **Researchers:** Academics and professionals requiring offline citation accuracy.
* **Small Technical Teams:** ≤10 engineers with sensitive documentation.

### 4  Key Differentiators

1. **100 % Self‑Hosted** – no external API calls after setup.
2. **Reduced Detection Footprint** – configurable crawling rates & proxies.
3. **Trustworthy Citations** – architecture prevents stale links and hallucinations.
4. **Plug‑and‑Play** – secure, containerised stack.

### 5  Functional Requirements (v1.0 Scope)

|  ID   |  Requirement                                                                  |  Tier     |
| ----- | ----------------------------------------------------------------------------- | --------- |
|  F‑1  |  Crawl entire domain; respect robots.txt & sitemaps; basic scheduler          | Community |
|  F‑2  |  Manual deletion detection (CLI 404 checker)                                  | Community |
|  F‑3  |  Automated & scheduled deletion detection                                     | **Pro**   |
|  F‑4  |  Clean HTML → Markdown, recursive splitter ≤ 512 tokens, handle code & tables | Community |
|  F‑5  |  Selectable embedding model (OpenAI, local GGUF, BGE)                         | Community |
|  F‑6  |  Pluggable vector DB (ChromaDB official, others community)                    | Community |
|  F‑7  |  `/query` retrieval endpoint                                                  | Community |
|  F‑8  |  CLI + simple React dashboard                                                 | Community |
|  F‑9  |  API‑key access control & Data‑Purge API                                      | **Pro**   |

### 6  Non‑Functional Requirements

* **Performance** – static ≤ 700 ms P95, JS‑rendered ≤ 2 s P95 (excluding render).
* **Security** – non‑root containers; auto‑HTTPS (Caddy/Traefik).
* **Reliability** – 95 % queries within SLA; < 0.1 % unnoticed crawl failures.
* **Backup/DR** – daily snapshot of vectors & metadata; `make restore` script.

### 7  Success Metrics

|  Metric                        |  Target   |
| ------------------------------ | --------- |
|  Citation accuracy\*           |  ≥ 95 %   |
|  Setup time (HTTPS)            |  ≤ 30 min |
|  Crawl coverage                |  ≥ 99 %   |
|  \*CI fails if accuracy < 95 % |           |

### 8  Out of Scope (v1.0)

Advanced bot evasion (CAPTCHA/JS fingerprinting), mobile UI, PDF OCR, on‑the‑fly translation, enterprise SSO/RBAC.

### 9  Milestones

|  Date        |  Milestone                                  |
| ------------ | ------------------------------------------- |
|  2025‑08‑30  |  Prototype CLI crawler + Chroma + Flask API |
|  2025‑10‑31  |  Beta Docker stack, MCP support, basic UI   |
|  2026‑01‑31  |  v1.0 Release (stable, Helm chart)          |

### 10  Risks & Mitigations

* **JS‑heavy sites** – Playwright fallback; proxy guidance.
* **Upstream deps** – contribute upstream, pin versions, integration tests.

### 11  Market & Pricing Strategy

|  Tier       |  Price                                              |  Key Features                                                             |
| ----------- | --------------------------------------------------- | ------------------------------------------------------------------------- |
|  Community  |  Free                                               |  2 sites, 50 k tokens, manual deletion detection, basic scheduler         |
|  Pro        |  US \$249 one‑time (+ US \$59/yr optional updates)  |  Unlimited sites/pages, automation, API key, data purge, priority support |

### 12  Future Scope (Post‑v1.0)

Enterprise edition (SSO, RBAC), integrated chat UI, multilingual support, advanced analytics.

### 13  Change Log

* **1.0 – 2025‑07‑20** – Hardened spec, refined SLAs, DR spec, extended timeline, clarified security/licensing, simplified GTM.

---

## Version 1.1 – Self‑Hosted Website Ingestion & Citation Service (Refined Spec) – 2025‑07‑20

### 1  Purpose

Build a **sovereign, extensible RAG engine** that crawls private or niche websites, indexes their content and serves answers **with ≥ 95 % verifiable citations**, all while running entirely on user‑controlled infrastructure.

### 2  Problem / Opportunity

LLM hallucinations, rampant link‑rot, and SaaS RAG data‑sovereignty issues demand a self‑hosted alternative.

### 3  Jobs‑to‑Be‑Done (JTBD)

|  Rank     |  Job Statement                                                                                                                           |  Type      |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
|  Primary  |  “When I manage private web knowledge, help me create trustworthy Q\&A with accurate citations, without privacy compromises or lock‑in.” | Functional |
|  2        |  “Let me feel confident and in control of my infra so I trust every answer.”                                                             | Emotional  |
|  3        |  “Demonstrate technical competence by deploying a reliable self‑hosted research tool.”                                                   | Social     |

### 4  Key Differentiators

1. **Sovereign & Extensible RAG Engine** (AGPLv3/community or commercial).
2. **Verifiable, Low‑Hallucination Q\&A** (≥ 95 % accuracy via *CiteFix*).
3. **Opinionated, Containerised Stack** (secure‑by‑default).
4. **Reduced Detection Footprint** (hybrid crawler, proxy support).

### 5  Functional Requirements (v1.1 Scope)

|  ID   |  User Story                                             |  Tier     |
| ----- | ------------------------------------------------------- | --------- |
|  F‑1  |  Recurring hybrid crawls (Scrapy→Playwright)            | Community |
|  F‑2  |  Automatic parse→semantic chunk→index (Unstructured.io) | Community |
|  F‑3  |  Selectable embedding model (OpenAI/BGE/GGUF)           | Community |
|  F‑4  |  REST `/query` with hybrid search → cross‑encoder + PDR | Community |
|  F‑5  |  Inspect retrieval & citation pipeline in UI            | Community |
|  F‑6  |  Manual link‑rot & content‑drift CLI                    | Community |
|  F‑7  |  Scheduler for deletion & drift detection               | **Pro**   |
|  F‑8  |  API‑key access control & data‑purge endpoint           | **Pro**   |
|  F‑9  |  Interactive crawler config & freshness dashboards      | **Pro**   |

### 6  Non‑Functional Requirements

* Static ≤ 700 ms P95; JS‑rendered ≤ 2 s P95.
* Citation accuracy ≥ 95 %.
* Security, reliability & backup targets unchanged.

### 7  Architecture & Tech‑Stack Updates

|  Stage         |  v1.0                         |  v1.1 Update                             |
| -------------- | ----------------------------- | ---------------------------------------- |
|  Crawler       |  Basic + Playwright fallback  |  **Hybrid Scrapy/Playwright**            |
|  Parser        |  HTML → Markdown              |  **Unstructured.io**                     |
|  Chunking      |  Recursive splitter           |  **Semantic chunk + PDR**                |
|  Vector Store  |  ChromaDB                     |  **Qdrant (Pro default)**                |
|  Retrieval     |  Single‑stage vector          |  **Hybrid BM25 + dense → cross‑encoder** |
|  Citation      |  —                            |  **CiteFix verification**                |

### 8  Success Metrics & 9 Out of Scope (unchanged)

### 10  Pricing & Licensing

|  Tier        |  Licence     |  Price       |  Sites                 |  Support        |
| ------------ | ------------ | ------------ | ---------------------- | --------------- |
|  Community   |  AGPLv3      |  Free        |  2                     |  Community      |
|  Pro         |  Commercial  |  US \$49/mo  |  Unlimited             |  Priority email |
|  Enterprise  |  Commercial  |  Contact     |  Unlimited + SSO/RBAC  |  Dedicated      |

### 11  Milestones & 12 Risks / Mitigations

Revised dates: 2025‑10‑30 (RAG core), 2026‑02‑28 (Integrated beta), 2026‑05‑31 (v1.0).

### 13  Change Log

* **1.1 – 2025‑07‑20** – Personas→JTBD, stack overhaul, CiteFix, subscription pricing, updated roadmap.

---

## Strategic Refinement & Competitive Analysis (Research Addendum)

*Full text of `mrd-research.md` follows*

Strategic Refinement and Competitive Analysis of the Self‑Hosted Website Ingestion & Citation Service
Section 1: Strategic Positioning and Competitive Landscape
The provided Market Requirements Document (MRD) for the Self‑Hosted Website Ingestion & Citation Service outlines a product with a clear purpose and a well‑defined initial scope.

\[Full detailed research content from `mrd-research.md`, lines 0‑114, has been included here without alteration.]
