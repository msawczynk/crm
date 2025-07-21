from typing import Dict, Callable
from _pytest.monkeypatch import MonkeyPatch

import requests
from requests.models import Response

from crawler import crawl, check_links


def fake_get_factory(responses: Dict[str, Response]) -> Callable[[str, int], Response]:
    def fake_get(url: str, timeout: int = 5) -> Response:
        return responses[url]

    return fake_get


def build_response(status: int, text: str = "") -> Response:
    r = Response()
    r.status_code = status
    r._content = text.encode()
    return r


def test_crawl(monkeypatch: MonkeyPatch) -> None:
    sitemap = (
        "<?xml version='1.0' encoding='UTF-8'?><urlset>"
        "<url><loc>http://example.com/a</loc></url>"
        "</urlset>"
    )
    responses = {
        "http://example.com/sitemap.xml": build_response(200, sitemap),
        "http://example.com/a": build_response(200, "<html><body>a</body></html>"),
        "http://example.com/robots.txt": build_response(200, ""),
    }
    monkeypatch.setattr(requests, "get", fake_get_factory(responses))
    pages = crawl("http://example.com")
    assert list(pages.keys()) == ["http://example.com/a"]


def test_check_links(monkeypatch: MonkeyPatch) -> None:
    responses = {
        "http://broken": build_response(404),
        "http://ok": build_response(200),
    }
    monkeypatch.setattr(requests, "get", fake_get_factory(responses))
    broken = check_links(["http://broken", "http://ok"])
    assert broken == ["http://broken"]
