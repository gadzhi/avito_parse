
from scrapy.spiders import CrawlSpider


class HabrSpider(CrawlSpider):
    name = "avito"  # имя для crawl команды
    allowed_domains = ["avito.ru"]  # на страницы с каких сайтов переходить
    start_urls = [
        "https://www.avito.ru/rossiya?q=opteron&i=1&s=104"  # откуда начинать
    ]

    def parse(self, response):  # метод обработки ответа
        with open('response.html', 'wb') as f:
            f.write(response.body)