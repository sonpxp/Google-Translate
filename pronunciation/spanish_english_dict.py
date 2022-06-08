from bs4 import BeautifulSoup
import requests
import urllib.parse


def spanish(query):
    r = requests.get('https://www.spanishdict.com/translate/' + query)
    # soup = BeautifulSoup(r.text, 'lxml')
    soup = BeautifulSoup(r.text, 'html.parser')
    definition = soup.find_all('span', class_='dictionaryLink--QZMZSUqh')
    pronunciation = soup.find('div', class_='bold--A0fE9Mds').text
    print(pronunciation)

    for item in definition:
        print(item.text)


while True:
    query = input('Type in the word: ')
    spanish(query)
