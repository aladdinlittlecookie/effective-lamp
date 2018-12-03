# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JokePipeline(object):
    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host='',
            user='root',
            password='1234',
            port=3306,
            database='spider',
            charset='utf8',
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        title = item["title"]
        con = item["con"]
        sql1 = "insert into joke_all(title,con) values('{}','{}')".format(title,con)


        self.cursor.execute(sql1)

        self.conn.commit()
        return item



    def close_spider(self,spider):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()