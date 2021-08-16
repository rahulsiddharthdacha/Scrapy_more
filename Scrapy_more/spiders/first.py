import scrapy
from ..items import ScrapyMoreItem


class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['']
    start_urls = ['https://www.moreretail.in/api/store-api?city&pincode=&market=&pagination_count=1000']

    def parse(self, response):
        item=ScrapyMoreItem()
        json_r=response.json()
        stores=json_r.get('data',{}).get('data',[])
        for store in stores:
            item['StoreName']=store.get('name','')
            item['city']=store.get('city','')
            item['State']=store.get('state','')
            item['Address']=store.get('address','')
            item['Pincode']=store.get('pincode','')
            item['Phone']=store.get('contact','')
            item['StoreType']=store.get('store_type','')
            item['StoreTimings']=store.get('weekdays_timing','')
            yield item


