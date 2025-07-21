# AGENTS.md – Agent Operating Manual

> **Repository:** `crm/`
> **Maintainer:** Warlack (@msawczyn)
> **Last updated:** 2025‑07‑21

This file instructs autonomous coding agents (e.g. OpenAI Codex) how to extend and maintain the project. **Follow every rule exactly.**

---

## 1 Mission

Build and evolve a sovereign, extensible Retrieval‑Augmented‑Generation (RAG) stack that crawls private or niche websites, indexes their content, and serves answers with ≥ 95 % verifiable citations while running entirely on user‑controlled infrastructure.

## 2 Core Scope (Community Tier v1.1)

Deliver MRD features **F‑1 → F‑7** as described in `mrd.md`. Pro‑tier features **F‑8 → F‑9** are stubbed with TODOs and marked `pytest.mark.xfail`.

## 3 Repository Layout (authoritative)

```
crm/
├── AGENTS.md            # ← you are here
├── mrd.md               # Combined Market Requirements Document
├── docs/                # ← NEW: human‑readable documentation (design notes, ADRs, run‑books)
│   └── README.md        # index for all docs (auto‑generated if missing)
├── codex/               # ← NEW: persistent agent memory & progress logs
│   ├── logs/            # chronological execution transcripts (YYYY‑MM‑DD‑HHMM.md)
│   ├── issues/          # markdown files describing open problems / enhancements
│   └── commentary/      # design discussions, decision records, retrospectives
├── crawler/             # Scrapy spiders + Playwright helpers
├── parser/              # HTML → Element pipeline
├── ingestion/           # Embeddings, chunking, vector upload
├── retrieval/           # Search, re‑rank, citation checker
├── api/                 # FastAPI routes
├── ui/                  # React dashboard (Vite)
├── scheduler/           # APScheduler jobs
├── cli/                 # Click‑based CLI tools
├── tests/               # Pytest suite (≥ 90 % coverage)
└── docker/              # Compose & k8s helm charts
```

### 3.1 `docs/` – Documentation Hub

* Store **all design artefacts** that require narrative explanation: architecture diagrams, ADRs, threat models, how‑to guides, etc.
* Prefer Markdown; embed diagrams as SVG/PNG inside the same folder.
* Auto‑generate `docs/README.md` that contains a table of contents linking every document in `docs/`.

### 3.2 `codex/` – Agent Memory & Transparency Layer

* **Purpose:** provide a durable, inspectable trail of what the agents did, why they did it, and what they plan next.
* **Sub‑folders:**

  * `logs/` – append‑only execution transcripts in Markdown; name files `YYYY‑MM‑DD‑HHMM.md`.
  * `issues/` – each file describes a discrete improvement or bug (use Conventional Commit style headers).
  * `commentary/` – higher‑level design debates, post‑mortems, or decision records (one per topic).
* Agents MUST write to these folders **before opening every pull‑request**:

  1. **Log** what prompt / diff was executed.
  2. **Summarise** outcome, performance metrics, and open questions.
  3. **Create / update** an `issues/` file if new work is uncovered.
* Human maintainers will review these artefacts and leave feedback—agents should read updated commentary before next run.

## 4 Coding Conventions & Tooling (unchanged)

* Python 3.11, `mypy --strict`, `ruff`, `black` (line length = 100).
* Tests via `pytest`; target ≥ 90 % line coverage.
* Commit style: Conventional Commits; branch prefix: `codex/`.

## 5 Workflow Rules for Agents

1. **Respect directory owners.** Only modify files inside directories listed in §3. Requests to edit MRD must be approved by a human.
2. **Write‑ahead logging.** Update `codex/logs/` *before* committing code.
3. **Memory usage.** Read relevant `codex/commentary/` and open `issues/` at session start; incorporate feedback.
4. **Documentation first.** When adding substantial features, create or update a doc in `docs/` explaining rationale and usage.
5. **Pull‑request checklist:**

   * All CI checks pass (`make lint`, `make test`, `make citations`).
   * New/changed docs included.
   * Appropriate log + issue files updated.
6. **No secrets.** Never commit secrets; use `.env.example` placeholders.

## 6 Environment Setup (quick start)

```bash
# Clone & bootstrap
git clone https://github.com/msawczynk/crm.git && cd crm
poetry install --with dev

# Run vector DB (default community stack)
docker compose up -d qdrant  # or chroma

# Launch all services & scheduler
make dev
```

## 7 Non‑Functional Targets (must‑meet)

| Metric                        | Target   |
| ----------------------------- | -------- |
| P95 static query latency      | ≤ 700 ms |
| P95 JS‑rendered query latency | ≤ 2 s    |
| Citation accuracy             | ≥ 95 %   |
| Test coverage                 | ≥ 90 %   |

## 8 Roadmap Snapshot

* **2025‑10‑30** – core RAG prototype (F‑1 → F‑4) complete.
* **2026‑02‑28** – integrated Docker stack inc. UI dashboards.
* **2026‑05‑31** – v 1.0 public release.

## 9 Contact

For questions ping **Warlack** on Slack or open an issue in `codex/issues/`.

---

> **Remember:** keep `codex/` updated—it is the project’s living memory and the bridge between autonomous agents and human oversight.
