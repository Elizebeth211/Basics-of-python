##XML processing
import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse("data.xml")  # Read XML file
root = tree.getroot()  # Get the root element
# Print root tag
print("Root Tag:", root.tag)
# Loop through child elements
for child in root:
    print(f"{child.tag}: {child.text}")

##Creating an xml file
person = ET.Element("person")
ET.SubElement(person, "name").text = "Liza"
ET.SubElement(person, "age").text = "25"
ET.SubElement(person, "city").text = "Ghent"
tree = ET.ElementTree(person)
tree.write("new_data.xml")

# Modify age value
for elem in root.iter("age"):
    elem.text = "26"
# Save the modified XML file
tree.write("updated_data.xml")


# Create root element
person = ET.Element("person")
# Add child elements
ET.SubElement(person, "name").text = "Liza"
ET.SubElement(person, "age").text = "25"
ET.SubElement(person, "city").text = "Ghent"
# Convert to XML tree and write to file
tree = ET.ElementTree(person)
tree.write("new_data.xml")


