# -*- coding: utf-8 -*-
import scrapy


class BangumiTvSpider(scrapy.Spider):
    name = "bangumi.tv"
    allowed_domains = ["bangumi.tv/anime/browser?sort=rank"]
    start_urls = ['http://bangumi.tv/anime/browser?sort=rank/']

    def parse(self, response):
        pass
