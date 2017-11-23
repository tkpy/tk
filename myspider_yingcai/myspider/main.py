from scrapy import cmdline
import os
# cmdline.execute('scrapy crawl lagou'.split())

os.chdir('spiders')
cmdline.execute('scrapy runspider lagou.py'.split())