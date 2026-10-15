from lxml import etree

parser = etree.XMLParser(dtd_validation=True)

try:
    etree.parse("courses.xml", parser)
    print("XML is valid")
except etree.XMLSyntaxError as e:
    print("XML is invalid")
    print(e)
