import xml.etree.ElementTree as ET

tree1 = ET.parse('strings.xml')
root1 = tree1.getroot()

# tree2 = ET.parse('strings_translatable.xml')
# root2 = tree2.getroot()
#
# d = {x.text: x.attrib['name'] for x in root2.findall('string') if x.text}

for x in root1.findall('string'):
    key = x.text
    print(key)
    # if key in d:
    #     x.set('name', d[key])

# tree1.write('new_string.xml')