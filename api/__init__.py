from __future__ import annotations

from fastapi import FastAPI

from retrieval import search

app = FastAPI()


@app.get("/query")
async def query(q: str) -> list[dict[str, str]]:
    results = search(q)
    return [{"url": url, "snippet": text[:200]} for url, text in results]
