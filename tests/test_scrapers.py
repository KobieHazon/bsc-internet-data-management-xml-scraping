import contextlib
import io
from pathlib import Path
import runpy
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

from lxml import etree

ROOT = Path(__file__).resolve().parents[1]


class ScraperTests(unittest.TestCase):
    def test_submitted_xml_remains_well_formed(self):
        files = list((ROOT / "solution/xml").glob("*.xml"))
        self.assertEqual(len(files), 5)
        for path in files:
            etree.parse(str(path), etree.XMLParser(no_network=True))

    def test_both_scrapers_with_local_html(self):
        response = Mock(content=b'<html><body><img alt="x" src="example.png"/><a href="https://example.co.uk">example</a><b>bold</b></body></html>')
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "answer.txt"
            for name in ("question5.py", "question5b.py"):
                with patch("public_web.get", return_value=response) as request:
                    with patch.object(sys, "argv", [name, "https://example.test", str(output)]):
                        with contextlib.redirect_stdout(io.StringIO()) as captured:
                            runpy.run_path(str(ROOT / "src" / name), run_name="__main__")
                    request.assert_called_once_with("https://example.test")
                result = output.read_text() if name == "question5b.py" else captured.getvalue()
                self.assertIn("example.png", result)
                self.assertIn("https://example.co.uk", result)
