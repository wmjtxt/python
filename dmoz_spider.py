#-*-coding:utf-8-*-
import scrapy

class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = ["qq.com"]
    start_urls = [
        "http://sports.qq.com/a/20180501/010077.htm"
    ]
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
