from __future__ import annotations

from hashlib import sha256
from typing import Iterable, List


def embed(texts: Iterable[str], model_name: str = "bge") -> List[List[float]]:
    """Return deterministic pseudo-embeddings for given texts."""
    embeddings: List[List[float]] = []
    for text in texts:
        digest = sha256(text.encode()).digest()
        vec = [int(b) / 255.0 for b in digest[:8]]
        embeddings.append(vec)
    return embeddings
