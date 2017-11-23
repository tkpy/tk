# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql
class MyspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class TencentPipeline(object):
    def __init__(self):
        self.fp = open('tencent.json','w',encoding='utf-8')

    def process_item(self,item,spider):
        self.fp.write(json.dumps(dict(item),ensure_ascii=False)+ '\n')
        return item

    def close_spider(self,spider):
        self.fp.close()

class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1','root','123456','mydb',charset='utf8')
        self.cursor = self.conn.cursor()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()


class LagouPipeline(MysqlPipeline):
    def process_item(self, item, spider):
        if spider.name == 'lagou':
            sql = 'insert into lagou_job(url,pname,smoney,emoney,location,syear,eyear,degree,ptype,tags,date_pub,advantage,jobdesc,jobaddr,company,crawl_time) ' \
                  'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update date_pub=values(date_pub),smoney=VALUES(smoney),emoney=values(emoney)'
            try:
                self.cursor.execute(sql, (
                item["url"], item["pname"], item["smoney"], item["emoney"], item["location"], item["syear"],
                item["eyear"], item["degree"], item["ptype"], item["tags"], item["date_pub"], item["advantage"],
                item["jobdesc"], item["jobaddr"], item["company"], item["crawl_time"]))
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
                print('执行语句失败')
                # 返回交给下一个管道文件处理
        return item
