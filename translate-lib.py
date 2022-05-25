from zhconv import convert, convert_for_mw

print(convert(u'人体内存在很多微生物', 'zh-tw'))
print(convert('我幹什麼不干你事。', 'zh-cn'))

print(convert_for_mw(u'在现代，机械计算-{}-机的应用已经完全被电子计算-{}-机所取代', 'zh-hk'))
print(convert_for_mw(u'-{zh-hant:資訊工程;zh-hans:计算机工程学;}-是电子工程的一个分支，主要研究计算机软硬件和二者间的彼此联系。', 'zh-tw'))
print(convert_for_mw(u'張國榮曾在英國-{zh:利兹;zh-hans:利兹;zh-hk:列斯;zh-tw:里茲}-大学學習。', 'zh-sg'))
print(convert_for_mw('毫米(毫公分)，符號mm，是長度單位和降雨量單位，-{zh-hans:台湾作-{公釐}-或-{公厘}-;zh-hant:港澳和大陸稱為-{毫米}-（台灣亦有使用，但較常使用名稱為毫公分）;zh-mo:台灣作-{公釐}-或-{公厘}-;zh-hk:台灣作-{公釐}-或-{公厘}-;}-。', 'zh-cn'))
