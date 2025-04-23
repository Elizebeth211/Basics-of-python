import xml.etree.ElementTree as ET
person = ET.Element("person")
tree = ET.ElementTree(person)
ET.ElementTree(root).write("file.xml")


