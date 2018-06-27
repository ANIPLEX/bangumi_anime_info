# -*- coding: utf-8 -*-

import pymongo
from scrapy.conf import settings

class BangumiAnimeInfoPipeline(object):
    def __init__(self):
        conn = pymongo.MongoClient(settings['MONGODB_HOST'],settings['MONGODB_PORT'])
        db = conn[settings['MONGODB_DBNAME']]
        self.connection = db[settings['MONGODB_TABLE']]
    def process_item(self, item, spider):
        bangumi_info = dict(item)
        self.connection.insert(bangumi_info)
        return item
