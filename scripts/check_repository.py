#!/usr/bin/env python3
from pathlib import Path
import ast
import sys
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRECTORIES = {".git", ".venv", "__pycache__", ".pytest_cache", ".ruff_cache", "run-results"}
FILES = [p for p in ROOT.rglob("*") if not (set(p.relative_to(ROOT).parts) & EXCLUDED_DIRECTORIES)]

required_files = ['assignment/HW1_2018.pdf', 'solution/xml/question2a.DTD', 'solution/xml/question2c1.xml', 'solution/xml/question2c2.xml', 'solution/xml/question2c3.xml', 'solution/xml/question2c4.xml', 'solution/xml/question3b.xml', 'src/question5.py', 'src/question5b.py', 'data/question5a.html', 'solution/question5c.txt']
missing = [name for name in required_files if not (ROOT / name).exists()]
if missing:
    print("Missing required files: " + ", ".join(missing), file=sys.stderr)
    sys.exit(1)

for path in FILES:
    rel = path.relative_to(ROOT).as_posix()
    if any(part.startswith("._") for part in path.parts):
        print(f"Apple metadata file is tracked candidate: {rel}", file=sys.stderr)
        sys.exit(1)
    if path.suffix in {".pyc", ".zip", ".docx"}:
        print(f"Forbidden wrapper/generated artifact: {rel}", file=sys.stderr)
        sys.exit(1)

for path in (ROOT / "src").rglob("*.py"):
    try:
        ast.parse(path.read_text(encoding="utf-8", errors="ignore"), filename=str(path))
    except SyntaxError as exc:
        print(f"Python syntax check failed in {path.name}: {exc}", file=sys.stderr)
        sys.exit(1)

for path in (ROOT / "solution" / "xml").glob("*.xml"):
    try:
        ElementTree.parse(path)
    except ElementTree.ParseError as exc:
        print(f"Strict XML parse failed in {path.name}: {exc}", file=sys.stderr)
        sys.exit(1)

text_files = [p for p in FILES if p.is_file() and p.suffix.lower() in {".py", ".md", ".csv", ".txt", ".xml", ".html", ".dtd", ".nt", ""}]
combined = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in text_files)
markers = ["".join(["208", "234", "161"]), "/" + "Users" + "/", "/" + "home" + "/"]
if any(marker in combined for marker in markers):
    print("Privacy or machine-path marker found in tracked text", file=sys.stderr)
    sys.exit(1)

required_markers = ['lxml.html', 'xpath', '<!ELEMENT catalog', '<result>']
missing_markers = [marker for marker in required_markers if marker not in combined]
if missing_markers:
    print("Missing expected project markers: " + ", ".join(missing_markers), file=sys.stderr)
    sys.exit(1)

print("Repository static checks passed.")
