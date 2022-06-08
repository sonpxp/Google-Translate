import epitran
from epitran.backoff import Backoff

'''
https://pypi.org/project/epitran/

* Language "Spaces"
---
deu-Latn = German
eng-Latn = English
spa-Latn = Spanish
spa-Latn-eu  =	Spanish (Iberian)
==========
* Languages with limited support due to highly ambiguous orthographies
fra-Latn = French
fra-Latn-np = French†
---
fra-Latn	French
fra-Latn-np	French†
fra-Latn-p	French (more phonetic)

===
vie-Latn = Vietnamese
===
deu-Latn	German
deu-Latn-np	German†
deu-Latn-nar	German (more phonetic)

'''


def spanish(query):
    code = 'spa-Latn'
    # ligatures enables non-standard IPA ligatures like "ʤ" and "ʨ".
    # tones allows IPA tones (˩˨˧˦˥) to be included and is needed for tonal languages like Vietnamese and Hokkien.
    # By default, this value is false and will remove IPA tones from the transcription.
    epi = epitran.Epitran(code, ligatures=False, tones=True)
    ipa = epi.transliterate(f'{query}')
    print(f"a: /{ipa}/")


spanish("hola")
