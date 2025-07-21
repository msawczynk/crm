from __future__ import annotations

from typing import Dict, List
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def find_sitemap(domain: str) -> str:
    """Return sitemap URL discovered via robots.txt or default to /sitemap.xml."""
    robots_url = urljoin(domain, "/robots.txt")
    try:
        resp = requests.get(robots_url, timeout=5)
        if resp.status_code == 200:
            for line in resp.text.splitlines():
                if line.lower().startswith("sitemap:"):
                    return line.split(":", 1)[1].strip()
    except requests.RequestException:
        pass
    return urljoin(domain, "/sitemap.xml")


def crawl(domain: str) -> Dict[str, str]:
    """Crawl pages listed in the site's sitemap."""
    sitemap_url = find_sitemap(domain)
    pages: Dict[str, str] = {}
    try:
        sitemap_resp = requests.get(sitemap_url, timeout=5)
        sitemap_resp.raise_for_status()
        soup = BeautifulSoup(sitemap_resp.text, "html.parser")
        for loc in soup.find_all("loc"):
            url = loc.text.strip()
            try:
                page = requests.get(url, timeout=5)
                if page.status_code == 200:
                    pages[url] = page.text
            except requests.RequestException:
                continue
    except requests.RequestException:
        pass
    return pages


def check_links(urls: List[str]) -> List[str]:
    """Return URLs that return 404."""
    broken = []
    for url in urls:
        try:
            resp = requests.get(url, timeout=5)
            if resp.status_code == 404:
                broken.append(url)
        except requests.RequestException:
            broken.append(url)
    return broken
