import xml.etree.ElementTree as ET

root = ET.Element("html")

head = ET.SubElement(root, "head")
title = ET.SubElement(head, "title")
title.text = "Title"

body = ET.SubElement(root, "body")
body.set("bgcolor","#ffffff")

body.text = "hello, world!"

tree = ET.ElementTree(root)
tree.write("hello.xhtml")
