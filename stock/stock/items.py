# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    data_time = scrapy.Field()
    qty = scrapy.Field()
    price = scrapy.Field()
    h_price = scrapy.Field()
    l_price = scrapy.Field()
    data_code = scrapy.Field()

