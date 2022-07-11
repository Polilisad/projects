import requests
from bs4 import  BeautifulSoup

URL = "http://www.galaxylogistics.ru/analitika/kodyi-aeroportov-mira-po-iata-iata.html"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36', 'accept':'*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

### парсинг страницы и основная логика

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    tags = soup.select(".post-1315 .entry-content p")
    avia =[]
    towns = []
    for tag in tags:
        for k in tag:
            a = repr(k.text)
            b = a[a.find("—")+1:]
            c = a[1:5]
            if len(b) > 3 and len(c) > 2 and len(b) < 100 and b != "'\\xa0'" and c != "'\\xa0'" :
                avia.append(b)
                towns.append(c)
            else:
                pass
    iata_kod = dict(zip(towns, avia))
    iata_kod = {x.replace(" ", ""): v
                for x, v in iata_kod.items()}
    user_choic = input("Введите город:")
    if user_choic in iata_kod.keys():
        print(iata_kod.setdefault(user_choic))
    else:
        print("Error")

### статус подключения
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("Error1")





parse()

