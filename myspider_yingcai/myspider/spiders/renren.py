# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    # start_urls = ['http://renren.com/']

    #解析start_urls
    def start_requests(self):
        start_urls = 'http://www.renren.com/PLogin.do'
        data = {
            'email': '1752570559@qq.com',
            'password': '1234qwer',
        }
        # FormRequest 发起post请求
        yield scrapy.FormRequest(start_urls, formdata=data, callback=self.parse)

    #解析函数
    def parse(self,response):
        # print('1111111')
        print(response.text)