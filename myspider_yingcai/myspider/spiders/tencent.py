# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor #LinkExtractor 提取页面所有超链接
from scrapy.spiders import CrawlSpider, Rule
from myspider.items import TencentItem

class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com']

    #定义提取url链接的规则
    rules = (
        #Rule构造请求
        #如果LinkExtractor不指定参数,则获取页面的所有超链接
        #follow是否跟进页面 , 继续按照规则进行匹配 ,生成请求, True继续跟进 , False不跟进
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),

        #列表页的信息
        Rule(LinkExtractor(allow=(r'position.php')),follow=True),
        #详情页的信息
        Rule(LinkExtractor(allow=(r'position_detail')),callback='parse_item',follow=False)
    )

    #页面解析函数 , 是否提取页面信息内容
    def parse_item(self, response):
        # print(response.text)
        # print('1231212312312')
        info_list = response.xpath('//table')
        item = TencentItem()
        for info in info_list:
            title = info.xpath('.//tr//td/text()').extract()[0]
            workplace = info.xpath('.//tr//td/text()').extract()[1]
            post = info.xpath('.//tr//td/text()').extract()[2]
            number = info.xpath('.//tr//td/text()').extract()[3].strip('人')
            duties = info.xpath('.//tr[@class="c"][1]//ul[@class="squareli"]/li/text()').extract()
            duties = ''.join(duties)
            require = info.xpath('//tr[@class="c"][2]//ul[@class="squareli"]/li/text()').extract()
            require = ''.join(require)
            print(title,workplace,post,number,duties,require)

            item['title'] = title
            item['workplace'] = workplace
            item['post'] = post
            item['number'] = number
            item['duties'] = duties
            item['require'] = require

            yield item

