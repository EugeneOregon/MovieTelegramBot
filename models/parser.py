import requests
from bs4 import BeautifulSoup


class Parser:
    URL = 'https://rezka.ag/'
    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/92.0.4 515.159 Safari/537.36', 'accept': '*/*'}

    def __init__(self):
        self.url = None
        self.movies = None
        self.movie_update = None

    def get_html(self):
        response = requests.get(self.url, headers=self.HEADERS, params=None)
        return response

    async def get_content(self, html, page):
        soup = BeautifulSoup(html, 'html.parser')
        if page == self.URL:
            new_content = soup.find('div', class_='b-newest_slider__inner')
            items = new_content.find_all('div', class_='b-content__inline_item-cover')
            self.movies = []
            for item in items:
                links = item.find_all('a', href=True)
                for link in links:
                    if link and item.find('i', class_="entity").get_text() == 'Фильм':
                        self.movies.append({
                            'link': 'https://rezka.ag' + link.get('href'),
                            'title': '',
                            'url': '',
                            'poster': ''
                        })
        else:
            content = soup.find('div', class_='b-sidecover')
            item = soup.find('div', class_='b-post__title')
            images = content.find_all('img', src=True)
            self.movie_update = []
            for image in images:
                self.movie_update.append({
                    'poster': image.get('src'),
                    'title': item.find('h1', itemprop="name").get_text(),
                })

    async def parse(self, url=URL):
        self.url = url
        html = self.get_html()
        if html.status_code == 200:
            await self.get_content(html.text, self.url)
        else:
            print('Error')
