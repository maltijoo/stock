# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class StockPipeline:
    def __init__(self):
        self.setupDBConect()
        self.createTable()

    def process_item(self, item, spider):
        self.storeInDb(item)
        return item

    def storeInDb(self, item):
        # 각 아이템을 Table에 저장

        data_time = item.get('data_time','').strip()
        qty = item.get('qty','').strip()
        price = item.get('price','').strip()
        h_price = item.get('h_price','').strip()
        l_price = item.get('l_price','').strip()
        data_code = item.get('data_code','').strip()

        sql = "INSERT INTO stock_table(id,data_time,qty,price,h_price,l_price,data_code) VALUES(null,%s,%s,%s,%s,%s,%s)"
        self.cur.execute(sql, (data_time,qty,price,h_price,l_price,data_code))
        self.conn.commit()        

    def setupDBConect(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='mydb', charset='utf8')
        self.cur = self.conn.cursor()
        print("DB Connected")

    def createTable(self):
        self.cur.execute("DROP TABLE IF EXISTS stock_table")

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS stock_table(
            id INT AUTO_INCREMENT PRIMARY KEY,
            data_time VARCHAR(100),
            qty VARCHAR(60),
            price VARCHAR(20),
            h_price VARCHAR(20),
            l_price VARCHAR(50),
            data_code VARCHAR(20))
        ''')