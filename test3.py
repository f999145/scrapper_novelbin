from config import headers, Cookies, url
from bs4 import BeautifulSoup as BS
import requests

# url = 'https://www.reg.ru/web-tools/myip'
req = requests.get(url=url, headers=headers, cookies=Cookies)
print(req.status_code)

# soup = BS(req.text, 'html.parser')
with open('data/test_test.html', 'w', encoding='utf-8') as file:
    file.write(req.text)
# print(soup.find('span', {'id':"headings", 'class':"b-myip-info__stats-value"}).text)