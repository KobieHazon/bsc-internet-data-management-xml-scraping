import sys
import public_web
import lxml.html

req = public_web.get(sys.argv[1])
doc = lxml.html.fromstring(req.content)

print('a:')
for attr in doc.xpath("//img[not(@alt='')]/@src"):
    print(attr)

print ("##################")

print('b:')
for link in doc.xpath("//a/@href[contains(.,'co.uk')]"):
    print(link)

print ("##################")

print('c:')
print(doc.xpath("//table[1]/tbody/tr[2]//text()[not(.='\n')]"))

print ("##################")

print('d:')
for word in doc.xpath("//b/text()"):
    print(word)
