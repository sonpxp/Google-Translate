from phonemizer.backend import EspeakBackend
from phonemizer import phonemize

backend_es = EspeakBackend('es', with_stress=True)
backend_fr = EspeakBackend('fr-fr', with_stress=True)
backend_de = EspeakBackend('de', with_stress=True)
backend_us = EspeakBackend('en-us', with_stress=True)


# cmd: espeak-ng --voices
# https://github.com/espeak-ng/espeak-ng/blob/master/docs/languages.md


def english(query):
    phonemized = backend_us.phonemize(query, strip=True)
    return phonemized


def french(query):
    phonemized = backend_fr.phonemize(query, strip=True)
    return phonemized


def spanish(query: list):
    phonemized = backend_es.phonemize(query, strip=True)
    return phonemized


def german(query: list):
    phonemized = backend_de.phonemize(query, strip=True)
    return phonemized


print(spanish(["hola"]))
print(french(["maison", "encore", "construire", "mère"]))
print(german(["drei", "klein", "Zuhause", "hinzufügen", "folgen", "Veränderung", "Tier"]))
print(english(["Hello, world!", "Welcome to Medium!"]))
