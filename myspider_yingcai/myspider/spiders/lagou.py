# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import datetime
from datetime import timedelta
# from myspider.items import LagouItem

from scrapy_redis.spiders import RedisSpider       #爬虫类需要继承 RedisSpider
from scrapy_redis.spiders import RedisCrawlSpider  #爬虫集成 RedisCrawlSpider

class LagouSpider(RedisCrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    # start_urls = ['http://lagou.com/']
    redis_key = 'LagouSpider:start_urls'
    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/.*'), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'),callback='parse_item',follow=False)
    )

    num_pattern = re.compile(r'\d+')
    def parse_item(self, response):
        # item = LagouItem()
        url = response.url
        pname = response.css('.job-name::attr(title)').extract()[0]
        money = response.css('.job_request .salary::text').extract()[0]
        smoney = money.lower().replace('k','').split('-')[0]
        emoney = money.lower().replace('k','').split('-')[1]

        location = response.xpath('//*[@class="job_request"]/p/span[2]/text()').extract()[0]
        location = self.remove_splash(location)

        year = response.xpath('//*[@class="job_request"]/p/span[3]/text()').extract()[0]
        syear,eyear = self.process_year(year)

        degree = response.xpath('//*[@class="job_request"]/p/span[4]/text()').extract()[0]
        degree = self.remove_splash(degree)

        ptype = response.xpath('//*[@class="job_request"]/p/span[5]/text()').extract()[0]
        ptype = self.remove_splash(ptype)

        tags = response.css('.job-advantage p::text').extract()[0]
        tags = ','.join(tags)

        date_pub = response.css('.publish_time::text').extract()[0]
        date_pub = self.process_date(date_pub)

        advantage = response.css('.job-advantage p::text').extract()[0]

        jobdesc = response.css('.job_bt div p::text').extract()
        jobdesc = ''.join(jobdesc)

        jobaddr1 = response.css('.work_addr a::text').extract()[:-1]
        jobaddr2 = response.css('.work_addr::text').extract()[-2].strip()
        jobaddr = ''.join(jobaddr1) + jobaddr2

        company = response.css('#job_company dt a img::attr(alt)').extract()[0]
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')

        yield {
            "url" : url,
            "pname" : pname,
            "smoney" : smoney,
            "emoney" : emoney,
            "location" : location,
            "syear" : syear,
            "eyear" : eyear,
            "degree" : degree,
            "ptype" : ptype,
            "tags" : tags,
            "date_pub" : date_pub,
            "advantage" : advantage,
            "jobdesc" : jobdesc,
            "jobaddr" : jobaddr,
            "company" : company,
            "crawl_time" : crawl_time,
        }


    def process_date(self,date_pub):
        if '天前' in date_pub:
            res = self.num_pattern.search(date_pub).group()
            date_pub = (datetime.datetime.now() - timedelta(days=int(res))).strftime('%Y-%m-%d')
        else:
            date_pub = datetime.datetime.now().strftime('%Y-%m-%d')
        return date_pub


    def process_year(self,year):
        if '-' in year:
            res = self.num_pattern.findall(year)
            syear = res[0]
            eyear = res[1]
        elif '以上' in year:
            res = self.num_pattern.findall(year)
            syear = res.group()
            eyear = res.group()
        else:
            syear = 0
            eyear = 0
        return syear,eyear


    #去掉'/'
    def remove_splash(self,value):
        #先去掉'/' , 再去掉空格
        value = value.replace('/','').strip()
        return value

