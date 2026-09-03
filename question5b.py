import sys
import requests
import lxml.html

f = open('question5c.txt', 'w')
req = requests.get(sys.argv[1])
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
