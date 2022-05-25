import requests
import json
from bs4 import BeautifulSoup
import re


def google_translate_api(sl: str = "en", tl: str = "vi", query: str = None):
    header = {
        "Host": "www.google.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0; Waterfox) Gecko/20100101 Firefox/56.2.5",
        "Accept": "*/*",
        "Referer": "https://www.google.com/",
        "Cookie": "NID=146=p-KPB8sQ6nqjr8I56LiEJzjdcsk7Wh91oDwr0jU0rfwOfN4Y_l9T4j_5uaSDg_6tDMSEXmPdhueoxwYM4w6meuHTK1R-Mej8-9Fm4kiEb8kFw8wVPnrgtaefkgNPq3W9ro81wpyImN-QtPVKILiNYq5UN07oTQWarcfgEXHOl0w6PR7uE4Xh14o; 1P_JAR=2018-11-12-04; OGP=-5061451:; DV=AwAhS-7BuJMeYH8oIYu_J3hJpKxjcBY",
        "Connection": "keep-alive",
        "Content-type": "application/x-www-form-urlencoded",
    }
    raw_data = f"async=translate,sl:{sl},tl:{tl},st:{query},id:1541997726654,qc:true,ac:true,_id:tw-async-translate,_pms:s,_fmt:pc"
    url = "https://www.google.com.vn/async/translate?vet=12ahUKEwjSgcPShM7eAhUH_GEKHaG2D5kQqDgwAHoECAYQFg..i&ei=EQTpW5K1EYf4hwOh7b7ICQ&yv=3"

    html = requests.post(url, data=raw_data.encode("utf-8"), headers=header)
    soup = BeautifulSoup(html.text, 'html.parser')
    data = soup.find('span', id="tw-answ-target-text").text
    print(data)
    return data


sl = "en"
tl = "vi"
# st = "welcome to vietnam"
st = "hello \n vietnam"
google_translate_api(sl, tl, st)
