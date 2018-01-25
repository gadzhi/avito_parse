
from scrapy.spiders import CrawlSpider


class HabrSpider(CrawlSpider):
    name = "avito"  # имя для crawl команды
    allowed_domains = ["avito.ru"]  # на страницы с каких сайтов переходить
    start_urls = [
        "https://www.avito.ru/rossiya?q=opteron&i=1&s=104"  # откуда начинать
    ]

    def parse(self, response):  # метод обработки ответа
        for i in response.xpath('//div[@class="catalog-main catalog_table"]//div[@class="description item_table-description"]'):
            yield {
                'name': i.xpath('.//a[@class="item-description-title-link"]/text()').extract_first(),
                'link': i.xpath('.//a[@class="item-description-title-link"]/@href').extract_first(),
                'price': i.xpath('.//div[@class="about"]/text()').extract_first(),
                'data': i.xpath('.//div[@class="data"]/div[@class=""]/div[@class="date c-2"]/text()').extract_first(),
            }
#        next_page = response.xpath('//a[@class="pagination-page js-pagination-next"]/@href').extract_first()
#       if next_page is not None:
#            yield scrapy.Request(response.urljoin(next_page))

