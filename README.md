# Internet Data Management: XML and Web Scraping

A historical archive of my CS BSc coursework.

## Project Summary

XML/DTD/XPath answers plus small Python web-scraping scripts for extracting media and links from HTML pages.

## Tech Stack

Python 3, requests, lxml, XPath, XML, DTD, HTML.

## Provenance

The supplied exercise material is preserved under `assignment/`. Recovered authored source, data, and answers are organized separately; earlier commits remain unchanged.

Submission ZIP wrappers, Apple metadata, official solution PDFs, and office-document/PDF answer exports were intentionally omitted from this repository.

## Validate

Run:

```sh
make check
```

Install Python dependencies with:

```sh
uv venv
uv pip install -r requirements.txt
```

The validator includes strict parsing of every submitted XML file and does not access the network. Original scraping scripts may require live web access if run directly.

## Repository layout

- `src/`: authored Python scripts, preserving the coursework filenames and sibling imports.
- `data/`: recovered reference data or HTML/CSV fixtures.
- `assignment/`: supplied exercise material, unchanged.
- `tests/` and `scripts/`: offline regression checks and repository validation.
- `results/` or `solution/` (where present): recovered outputs and written/XML answers.
- `run-results/` (where used): ignored output from new runs, separate from recovered evidence.

Run `make check` and `make test` from the repository root. The tests use local fixtures; they do not scrape live websites.

For an explicitly selected live page, run `uv run --no-project --with-requirements requirements.txt python src/question5.py URL`. The file-output version is `src/question5b.py URL [OUTPUT]`; its default output is `run-results/question5c.txt`, not the preserved answer.
