from phonemizer import phonemize

'''
language_code:
gmw, de, West Germanic,	German
roa, fr, Romance French, France
roa, es, Romance Spanish,Spain
roa, es-419, Romance Spanish, Latin American
'''

# https://pypi.org/project/phonemizer/
text = ["Hello, world!", "Welcome to Medium!"]
text_es = ["hola", "Gracias", "Salud", "Lo siento", "Por favor", "Adiós"]

pronunciation = phonemize(text, language='en-us', backend='espeak')
print(pronunciation)



# def french(query):
#     pronunciation = phonemize(query, language='fr', backend='espeak')
#     return pronunciation
#
# french(["french"])
#
#
# def spanish(query):
#     pronunciation = phonemize(query, language='es', backend='espeak')
#     return pronunciation
#
#
# def german(query):
#     pronunciation = phonemize(query, language='de', backend='espeak')
#     return pronunciation
