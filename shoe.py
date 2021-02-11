import requests
from bs4 import BeautifulSoup
import re

# code ro mide b url va size o gheimat ro mide
def find_shoe(adress):
    headers = {'accept-language': 'fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7',
               'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36'}

    r = requests.get('https://www.amazon.com/dp/' + adress + '?th=1&psc=1', headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    size = soup('span', {'class': 'a-size-base a-color-base inline-twister-dim-title-value'})[0].get_text().strip()
    print(size, end=' : ')
    int_price = soup('span', {'class': 'price-large'})[0].get_text().strip()
    float_price = soup('span', {'class': 'a-size-small price-info-superscript'})[1].get_text().strip()
    price = '$' + int_price + '.' + float_price
    print(price)
    dictionary[size] = price


# ******************************************************


headers = {'accept-language': 'fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7',
           'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36'}
# url = input('give me your shoe url(+\' \' ,ex:\'google.com \'):\n').strip()
url = 'https://www.amazon.com/dp/B002JK6QTS'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
sp = soup('script', {'type': 'a-state'})
codes = ''
for i in sp:
    if '<script data-a-state=\'{"key":"mobile-inline-twister-dims-to-asin-list"}\'' in str(i):
        codes = str(i)
        break

dictionary = {}
lst_codes = re.findall(r'\"\d+\":\"(.+?)\"', codes)
print('please waite this may take some time ...\nafter that the dictionary will appear : ')

for i in lst_codes:
    find_shoe(i)

print(dictionary)
