# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BangumiAnimeItem(scrapy.Item):
    #名称
    title = scrapy.Field()
    #原名
    primitive = scrapy.Field()
    #排名
    rank = scrapy.Field()
    #评分
    grade = scrapy.Field()
    #图片
    imgurl = scrapy.Field()
