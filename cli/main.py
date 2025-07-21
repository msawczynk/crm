from __future__ import annotations

import json
from typing import List

import click

from crawler import check_links, crawl


@click.group()
def main() -> None:
    """CRM CLI entry point."""


@main.command()
@click.argument("domain")
def crawl_domain(domain: str) -> None:
    pages = crawl(domain)
    click.echo(json.dumps({"pages": len(pages)}))


@main.command()
@click.argument("urls", nargs=-1)
def check(urls: List[str]) -> None:
    broken = check_links(list(urls))
    for url in broken:
        click.echo(url)


if __name__ == "__main__":
    main()
