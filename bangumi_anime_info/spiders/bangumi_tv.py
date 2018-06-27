# -*- coding: utf-8 -*-
import scrapy
from bangumi_anime_info.items import BangumiAnimeItem

class Bangumi_Anime_Spider(scrapy.Spider):
    name = "bangumi.tv"
    #allowed_domains = ["http://bangumi.tv/anime/browser/"]
    start_urls = ['http://bangumi.tv/anime/browser/?page=1']

    def parse(self, response):
        item = BangumiAnimeItem()
        for anime in response.xpath('//*[@id="browserItemList"]/li'):
            try:
                item['primitive'] = anime.xpath("./div/h3/small/text()").extract()[0]
            except:
                item['primitive'] = anime.xpath("./div/h3/a/text()").extract()[0]
            item['title'] = anime.xpath("./div/h3/a/text()").extract()[0]
            try:
                item['imgurl'] = anime.xpath("./a/span/img/@src").extract()[0]
            except:
                item['imgurl'] = '暂时无图'
            try:
                item['grade'] = anime.xpath("./div/p[2]/small/text()").extract()[0]
            except:
                item['grade'] = '少于十人评分'
            try:
                item['rank'] = anime.xpath("./div/span/text()").extract()[0]
            except:
                item['rank'] = '4752名以外'
                #print(item)
                yield item
        next_url = response.xpath("//div[@class='page_inner']/a[last()-2]/@href").extract()
        if next_url:
            next_url = 'http://bangumi.tv/anime/browser/'+next_url[0]
            yield scrapy.Request(next_url,callback=self.parse,dont_filter=True)