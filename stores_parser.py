import json

from bs4 import BeautifulSoup
import requests

from web_helper.secrets import DATABASE_NAME, USER, PASSWORD


class Parser:
    def __init__(self, link):
        self.link = link

    def get_html(self):
        r = requests.get(self.link)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup


class AirsoftstoreParser(Parser):

    def parser(self):
        data = []
        title = 'AirsoftStore'
        description = ''
        discount = ''
        logo = ''
        html = self.get_html().find('ul', class_='thumbnails').findAll('li', class_='span3')
        for i in html:
            item_pic = i.find('div', class_='prodpic').find('img')
            item_pic = self.link[:27] + item_pic['data-src']
            item_name = i.find('p', class_='prodname').text.replace('\n', '')
            link = self.link[:27] + i.find('a', href=True)['href']
            try:
                price = i.find('span', class_='newprice').text[:-5].replace(' ', '')
                price = int(price)
            except AttributeError:
                price = None
            if i.find('span', class_='label in-stock'):
                in_stock = True
            else:
                in_stock = False
            data.append((item_pic, item_name, link, price, in_stock))
        return data


if __name__ == '__main__':
    url = ['https://www.airsoftstore.ru/oruzhie/m-seriia?showall=999999',
           'https://www.airsoftstore.ru/oruzhie/ak-seriia?showall=999999']
    for i in url:
        print(AirsoftstoreParser(i).parser())
