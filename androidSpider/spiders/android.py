# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re
from androidSpider.items import AndroidspiderItem
import sys

class AndroidSpider(scrapy.Spider):
    name = 'android'
    allowed_domains = ['source.android.com']
    start_urls = ['https://source.android.com/security/bulletin/']

    def parse(self, response):
        url = response.xpath('//table/tr/td//a/@href').extract()
        for i in url:
            if str(i).find("?hl=") == -1:
                file = open('url','a')
                file.write(i)
                file.write('\n')
                file.close()
                year = re.findall(r'bulletin/(.*?).html',i)[0]
                yield Request(url=str(i), callback=self.parse_detail, meta={"patch_date" : year})

    def parse_detail(self, response):
        cve_list = response.xpath('//table/tr//td[1]/text()').extract()
        patch_date_list = response.meta.get("patch_date")
        type_list = response.xpath('//table/tr//td[3]/text()').extract()
        level_list = response.xpath('//table/tr//td[4]/text()').extract()
        aosp_model_list = response.xpath('//table/tr//td[5]/text()').extract()
        for i in cve_list:
            if str(i).find("CVE") == -1:
                cve_list.remove(str(i))
        useful_length = len(cve_list)
        for i in range(0, useful_length):
            item = AndroidspiderItem()
            item['cve_id'] = cve_list[i]
            item['patch_date'] = patch_date_list
            item['type'] = type_list[i]
            item['level'] = level_list[i]
            item['affect_version'] = aosp_model_list[i]
            yield item

