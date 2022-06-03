import webbrowser
import requests
import time


def parse_string(text):
    """Replace the following characters in the text"""
    special_characters = (
        ("%", "%25"),
        (" ", "%20"),
        (",", "%2C"),
        ("?", "%3F"),
        ("\n", "%0A"),
        ('\"', "%22"),
        ("<", "%3C"),
        (">", "%3E"),
        ("#", "%23"),
        ("|", "%7C"),
        ("&", "%26"),
        ("=", "%3D"),
        ("@", "%40"),
        ("#", "%23"),
        ("$", "%24"),
        ("^", "%5E"),
        ("`", "%60"),
        ("+", "%2B"),
        ("\'", "%27"),
        ("{", "%7B"),
        ("}", "%7D"),
        ("[", "%5B"),
        ("]", "%5D"),
        ("/", "%2F"),
        ("\\", "%5C"),
        (":", "%3A"),
        (";", "%3B")
    )

    for pair in special_characters:
        text = text.replace(*pair)

    return text


def open_google_trans(source_language="en", target_language="pt", text_to_translate=None):
    """
        Translate the text from the source_language to the target_language, by opening the
        Google Translate site with this info.
        Parameters are all strings.
        Return is None
    """

    # exit the function if no text is submitted
    if not text_to_translate:
        print("No text submitted to translation.\nPlease insert a text.\n")
        return None

    if text_to_translate.startswith("http"):
        text_to_translate = requests.get(text_to_translate).text

    elif text_to_translate.endswith(".txt"):
        with open(text_to_translate) as file:
            text_to_translate = file.read()

    # variables to be used in the url:
    # source language
    sl = source_language
    # target language
    tl = target_language
    # operation
    operation = "translate"

    text_to_translate = parse_string(text_to_translate)

    # f-string with variables:
    link = f"https://translate.google.com/?sl={sl}&tl={tl}&text={text_to_translate}&op={operation}"

    # This function, from the webbrowser module, opens a link in the default browser
    webbrowser.open(link)


if __name__ == "__main__":
    languages = ["pt", "es", "eo", "la", "tr", "ko", "ja"]
    url = "https://raw.githubusercontent.com/fabricius1/Google-Translate-Automation/master/textToTranslate.txt"
    text_to_translate = url

    for language in languages:
        open_google_trans("en", language, text_to_translate)
        time.sleep(5)
