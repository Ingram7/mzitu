# -*- coding: utf-8 -*-
import scrapy
from mzitu.items import MzituItem

class MzituspdSpider(scrapy.Spider):
    name = 'mzituspd'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/all/']

    def parse(self, response):
        for href in response.xpath('//ul[@class="archives"]/li//a/@href').extract():
            yield scrapy.Request(url=href, callback=self.get_parse, dont_filter=True)

    def get_parse(self, response):
        # print(response.request.headers['User-Agent'])
        item = MzituItem()
        item['title'] = response.xpath('//div[@class="main-image"]//img/@alt').extract()[0]
        item['imgurl'] = response.xpath('//div[@class="main-image"]//img/@src').extract()
        yield item

        # print(item)

        next_page = response.xpath("//a/span[contains(text(),'下一页»')]/../@href")#..  ：当前节点父节点
        if next_page:
            url = next_page[0].extract()
            yield scrapy.Request(url, callback=self.get_parse)


