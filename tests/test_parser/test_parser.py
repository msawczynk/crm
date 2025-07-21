from parser import html_to_markdown, split_markdown


def test_html_to_markdown() -> None:
    html = "<html><body><h1>Title</h1><p>text</p></body></html>"
    md = html_to_markdown(html)
    assert "Title" in md
    assert "text" in md


def test_split_markdown() -> None:
    text = "word " * 600
    chunks = split_markdown(text, max_tokens=512)
    assert len(chunks) == 2
