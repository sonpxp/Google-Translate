from bs4 import BeautifulSoup
import requests
import urllib.parse
from urllib.parse import quote


def spanish(query):
    # will web_scrape from spanishdict
    r = requests.get('https://www.spanishdict.com/pronunciation/' + quote(query))
    # soup = BeautifulSoup(r.text, 'lxml')
    soup = BeautifulSoup(r.text, 'html.parser')
    alphabet_section = soup.find_all('div', class_='alphabetSection--Pd8jhB6W')

    # print(type(alphabet_section))

    for item in alphabet_section:
        # print(item)
        header = item.find('div', class_='header--CRPPld7S').text
        pronunciation = item.find('div', class_='alphabet--AWGx23xG').text
        print(f"header: {header}")
        print(f"pronunciation: {pronunciation}")
        print("-----------")


# spanish("personne")
spanish("hola")
