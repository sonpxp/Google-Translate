import re
import xml.etree.ElementTree as ET

from translation.translate_tool import Translator


def openXml():
    with open("strings.xml", encoding='UTF-8') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines


def trans(st: str):
    sl = "en"
    tl = "vi"
    # st = "Will, you listen"
    translate = Translator.google_translate_api(sl, tl, st)
    return translate


def readXml():
    data = openXml()
    lst_data_trans = []

    for i in data:
        try:
            root = ET.fromstring(i)
            xml_content = root.text
            tran = trans(xml_content)
            output = re.sub(r"(?<=<string)*>(.*?)(?=</string>)", f'>{tran}', i)
            lst_data_trans.append(output)
        except:
            lst_data_trans.append(i)
            continue
    return lst_data_trans


def save_to_file(*text):
    with open('filename.xml', mode='wt', encoding='utf-8') as myfile:
        for lines in text:
            myfile.write('\n'.join(str(line) for line in lines))
            myfile.write('\n')


def testRegex():
    xml_str = '<string name="previous">Previous junior</string>'
    name = "chao cac ban"
    output = re.sub(r"(?<=<string)*>(.*?)(?=</string>)", f'>{name}', xml_str)
    print(output)

# save to xml file
save_to_file(readXml())

