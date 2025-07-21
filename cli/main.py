from __future__ import annotations

import click


@click.command()
def main() -> None:
    """Entry point for CRM CLI."""
    click.echo("CRM CLI placeholder")


if __name__ == "__main__":
    main()
