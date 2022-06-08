from gruut import sentences
# https://pypi.org/project/gruut/
# text = 'Adelante'
#
# for sent in sentences(text, lang="es-es"):
#     for word in sent:
#         if word.phonemes:
#             print(*word.phonemes)


text = 'hola'

for sent in sentences(text, lang="es"):
    for word in sent:
        if word.phonemes:
            print(word.text, *word.phonemes)