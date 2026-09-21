"""Bounded, anonymous integration check against public Wikipedia pages."""
import contextlib
import io
from pathlib import Path
import runpy
import sys
import tempfile
import time
from urllib.parse import urlsplit
from unittest.mock import patch

import requests

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
session = requests.Session()
session.trust_env = False  # Do not use machine credentials, proxies, or .netrc.
session.headers["User-Agent"] = "CourseworkIntegrationCheck/1.0 (bounded anonymous test)"
calls = []

def get(url, **kwargs):
    parsed = urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname != "en.wikipedia.org" or parsed.username:
        raise ValueError("Only anonymous HTTPS Wikipedia requests are allowed")
    if len(calls) >= 12:
        raise RuntimeError("Request budget exhausted")
    if calls:
        time.sleep(0.4)
    calls.append(url)
    session.cookies.clear()
    response = session.get(url, timeout=20, allow_redirects=False)
    response.raise_for_status()
    if response.is_redirect:
        raise RuntimeError("Unexpected redirect; inspect the public URL before retrying")
    return response

with patch("public_web.get", side_effect=get):
    with tempfile.TemporaryDirectory() as directory:
        output = Path(directory) / "answer.txt"
        for name in ("question5.py", "question5b.py"):
            with patch.object(sys, "argv", [name, "https://en.wikipedia.org/wiki/Elizabeth_I", str(output)]):
                with contextlib.redirect_stdout(io.StringIO()) as captured:
                    runpy.run_path(str(ROOT / "src" / name), run_name="__main__")
            result = output.read_text() if name == "question5b.py" else captured.getvalue()
            assert all(label + ":" in result for label in "abcd")
            assert "wikimedia.org" in result, "No image links extracted"
            assert len(result) > 500, "Unexpectedly empty page extraction"
        print("Both live scraper entry points passed")
print("Anonymous requests: %d" % len(calls))
