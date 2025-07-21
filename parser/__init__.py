from __future__ import annotations

from typing import List

from bs4 import BeautifulSoup


def html_to_markdown(html: str) -> str:
    """Convert HTML to a simplified Markdown string."""
    soup = BeautifulSoup(html, "html.parser")
    text_parts = []
    for element in soup.find_all(text=True):
        text = str(element).strip()
        text_parts.append(text)
    return "\n".join(part for part in text_parts if part)


def split_markdown(markdown: str, max_tokens: int = 512) -> List[str]:
    """Split Markdown by words with a maximum token count."""
    words = markdown.split()
    chunks = []
    for i in range(0, len(words), max_tokens):
        chunk = " ".join(words[i : i + max_tokens])
        chunks.append(chunk)
    return chunks
