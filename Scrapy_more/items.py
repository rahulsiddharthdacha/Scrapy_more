# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyMoreItem(scrapy.Item):
    # define the fields for your item here like:
    StoreName = scrapy.Field()
    city=scrapy.Field()
    State=scrapy.Field()
    Address=scrapy.Field()
    Pincode=scrapy.Field()
    Phone=scrapy.Field()
    StoreType=scrapy.Field()
    StoreTimings=scrapy.Field()
    
