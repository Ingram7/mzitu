# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy


# class MzituPipeline(object):
#     def process_item(self, item, spider):
#         return item

class MzituPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['imgurl']:
            # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
            yield scrapy.Request(image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        # 图片名字图片的url最后一个'/'后面内容
        image_name = request.url.split('/')[-1]

        path = u'{}/{}'.format(item['title'], image_name)
        return path