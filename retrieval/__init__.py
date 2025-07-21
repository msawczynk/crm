from __future__ import annotations

from typing import Dict, List, Tuple

from ingestion import embed

# simple in-memory vector store
_STORE: List[Tuple[str, List[float], str]] = []


def index(pages: Dict[str, str]) -> None:
    """Index pages into the in-memory store."""
    texts = list(pages.values())
    embeddings = embed(texts)
    for (url, text), emb in zip(pages.items(), embeddings):
        _STORE.append((url, emb, text))


def search(query: str, top_k: int = 3) -> List[Tuple[str, str]]:
    """Return ``top_k`` URLs and snippets matching the query."""
    if not _STORE:
        return []

    q_emb = embed([query])[0]

    def score(item: Tuple[str, List[float], str]) -> float:
        url, vec, text = item
        base = sum(q * v for q, v in zip(q_emb, vec))
        if query.lower() in text.lower():
            base += 1.0
        return base

    ranked = sorted(_STORE, key=score, reverse=True)
    return [(url, text) for url, _, text in ranked[:top_k]]
