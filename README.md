# Internet Data Management: XML and Web Scraping

- Authors: Kobie Hazon and Adi Eldar.

The supplied exercise files are in `assignment/`. My code is kept separately, along with the data and answers.

## Project Summary

XML/DTD/XPath answers plus small Python web-scraping scripts for extracting media and links from HTML pages.

## Tech Stack

Python 3, requests, lxml, XPath, XML, DTD, HTML.

## Validate

Run:

```sh
make test
```

Install Python dependencies with:

```sh
uv venv
uv pip install -r requirements.txt
```

The tests parse the submitted XML and execute both scraper entry points against local HTML. Live scraping is available separately with `make test-live`.

## Written answers

My submission with Adi Eldar is in [written-answers.pdf](solution/written-answers.pdf).

## Repository layout

- `src/`: Python implementations.
- `assignment/`: Exercise briefs and supplied inputs.
- `data/`: Input data and test fixtures.
- `solution/`: Written answers and submitted XML files.
- `tests/`: Executable regression tests.
- `scripts/`: Bounded live-web tests.

Run `make test` from the repository root. The tests use local fixtures; they do not scrape live websites.

For an explicitly selected live page, run `uv run --no-project --with-requirements requirements.txt python src/question5.py URL`. The file-output version is `src/question5b.py URL [OUTPUT]`; its default output is `run-results/question5c.txt`, not the preserved answer.

Run `make test-live` to execute both scraper entry points against the public Elizabeth I page. This bounded check makes two anonymous requests with timeouts and no account credentials, checks the extracted sections, and keeps temporary output outside the repository.
