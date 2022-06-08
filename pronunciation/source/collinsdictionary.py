from bs4 import BeautifulSoup
import requests
import urllib.parse

w_fr = []
w_es = []
w_de = []


def french(query):
    url = 'https://www.collinsdictionary.com/dictionary/french-english/' + urllib.parse.quote(query)
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
    headers = {'User-Agent': user_agent}
    web_request = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_request.text, "html.parser")
    pronunciation = soup.find('span', class_='pron').text
    pronounce = f"/{pronunciation}/"
    print({f"{query.lower()}": pronounce})


# def spanish(query):
#     url = 'https://www.howtopronounce.com/spanish/' + urllib.parse.quote(query)
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
#     headers = {'User-Agent': user_agent}
#     web_request = requests.get(url, headers=headers)
#     soup = BeautifulSoup(web_request.text, "html.parser")
#     pronunciation = soup.find('span', class_='pr-10px wordBreakWord').text
#     pronounce = f"/{pronunciation}/"
#     # print(pronounce)
#     print({f"{query.lower()}": pronounce})


def german(query):
    url = 'https://www.collinsdictionary.com/dictionary/german-english/' + urllib.parse.quote(query)
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
    headers = {'User-Agent': user_agent}
    web_request = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_request.text, "html.parser")
    pronunciation = soup.find('span', class_='form pron').text
    pronounce = f"/{pronunciation}/"
    # print(pronounce)
    print({f"{query.lower()}": pronounce})


french("Salut")
# spanish("hogar")
german("heimat")
