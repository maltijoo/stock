import scrapy
from stock.items import StockItem
import time


class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['finance.naver.com/item/sise.nhn?code=326030']
    start_urls = ['https://finance.naver.com/item/sise.nhn?code=326030']

    def parse(self, response):
        data_time = response.xpath('//*[@id="time"]/em/text()').extract()
        qty = response.xpath('//*[@id="_quant"]/text()').extract()
        price = response.xpath('//*[@id="_nowVal"]/text()').extract()
        h_price = response.xpath('//*[@id="_high"]/text()').extract()
        l_price = response.xpath('//*[@id="_low"]/text()').extract()
        data_code = response.xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]/text()').extract()


        items=[]
        for idx in range(len(data_code)):
            item = StockItem()
            item['data_time']=data_time[idx]
            item['qty']=qty[idx]
            item['price']=price[idx]
            item['h_price']=h_price[idx]
            item['l_price']=l_price[idx] 
            item['data_code']=data_code[idx]         
            items.append(item)
        
        return items      