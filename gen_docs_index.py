# pragma: no cover
import pathlib

# This script is used only during development and is excluded from coverage.

docs_path = pathlib.Path("docs")
readme_path = docs_path / "README.md"
files = sorted([p for p in docs_path.glob("*.md") if p.name != "README.md"])

with readme_path.open("w") as f:
    f.write("# Documentation\n\n")
    if files:
        f.write("## Table of Contents\n")
        for p in files:
            rel = p.name
            f.write(f"- [{rel}](./{rel})\n")
    else:
        f.write("No documentation yet.\n")
