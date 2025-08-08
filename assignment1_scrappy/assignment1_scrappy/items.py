import scrapy

class BooksScraperItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    available_stocks = scrapy.Field()
    image_url = scrapy.Field()