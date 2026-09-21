from pathlib import Path

import sys
import public_web
import lxml.html

output = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parents[1] / "run-results" / "question5c.txt"
output.parent.mkdir(parents=True, exist_ok=True)
f = output.open("w")
req = public_web.get(sys.argv[1])
doc = lxml.html.fromstring(req.content)

f.write('a:\n')
for attr in doc.xpath("//img[not(@alt='')]/@src"):
    f.write(attr)
    f.write('\n')

f.write('\n')
f.write('b:\n')
for link in doc.xpath("//a/@href[contains(.,'co.uk')]"):
    f.write(link)
    f.write('\n')

f.write('\n')
f.write('c:\n')
f.write(str(doc.xpath("(//table/tbody/tr[2])[1]//text()[not(.='\n')]")))

f.write('\n\n')
f.write('d:\n')
f.write(str(doc.xpath("//b//text()")))

f.close()
