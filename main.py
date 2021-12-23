import requests
import bs4
from pprint import pprint

KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'Кэш'}

HEADERS  = {
    'Cookie': '_ga=GA1.2.1002797372.1631887203; _ym_uid=163188720360074783; _ym_d=1631887203; __gads=ID=d2e112c13a9c792f:T=1631887202:S=ALNI_MbBN-i1HGjEvKeeESglTFZ8ogffKg; hl=ru; fl=ru; habr_web_home=ARTICLES_LIST_ALL; cto_bundle=suKUXF9QWSUyRnJ3SUtoJTJGdElNVmF1WiUyQmNuYm4lMkJKd0NhJTJGOXlLcWNaSEdSa2NtY0JCVE9hczJnTE9CZUZSY3BNMm1USVRWVzR2eDFueE9ReXhZcWFkY0I2SEFuNWNEeU16cEJOZURHJTJGZmRFako1cXdpRHU4YzVyNHdnSGhHSHZnelVTMDVDdnFkR3FzeWt5cWxZOVdWVGJEVDRwWnclM0QlM0Q; visited_articles=112327:531472:311586:286918:559544:272711:483202:464261; _gid=GA1.2.21783333.1640289520; _ym_isad=2',
    'If-None-Match': 'W/"389fd-h203vV/+UZl18kP8/sdHHsVRpyQ"',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
for article in articles:
    titles = article.find_all('a', class_='tm-article-snippet__title-link')
    titles = set(title.find('span').text for title in titles)
    for i in titles:
        words = set(i.split(' '))
        if KEYWORDS & words:
            href = article.find('a', class_='tm-article-snippet__title-link').get('href')
            url = 'https://habr.com/ru/all' + href
            data = article.find('span', class_='tm-article-snippet__datetime-published').text
            pprint(titles)
            pprint(url)
            pprint(data)
