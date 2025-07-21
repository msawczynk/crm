# Architecture Overview

This project implements a minimal Retrieval-Augmented Generation pipeline as described in the MRD.

- **Crawler**: fetches pages listed in a site's sitemap and provides manual link checking.
- **Parser**: converts HTML to simplified Markdown and splits text into chunks.
- **Ingestion**: creates deterministic pseudo-embeddings for content.
- **Retrieval**: stores embeddings in-memory and performs a basic similarity search.
- **API**: exposes a `/query` endpoint via FastAPI.
- **Scheduler**: very small timer-based scheduler used to run tasks periodically.

These modules form the basis for MRD features F-1 through F-7.
