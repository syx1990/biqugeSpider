# -*- coding: utf-8 -*-
# !/usr/bin/python3
# author by : yuxiangShi
# tell  by: 18538187569

import scrapy

from bqgSpider.items import BiqugeItem
import os


class bqgSpider(scrapy.Spider):
    name = 'bqgSpider'
    allowed_domains = ['www.xbiquge.la']
    start_urls = [
        'http://www.xbiquge.la/xiaoshuodaquan/'
    ]

    def parse(self, response):
        bqg = response.xpath("//div[@class='novellist']/ul/li/a/@href").extract()
        name = response.xpath("//div[@class='novellist']/ul/li/a/text()").extract()
        for i in range(len(name)):
            item = BiqugeItem()
            item['name'] = name[i]
            item['url'] = bqg[i]
            if not os.path.exists(name[i]):
                os.makedirs(name[i])
            yield scrapy.Request(url=item['url'], meta={'meta1': item}, callback=self.parseBqg,dont_filter=True)

    # 对于返回的小类的url，再进行递归请求
    def parseBqg(self, response):
        meta1 = response.meta['meta1']
        bqgInfo = response.xpath('//*[@id="list"]/dl/dd/a/@href').extract()  # 获取所有的链接地址
        self.log("获取所有的链接地址:" + str(bqgInfo))
        for i in range(len(bqgInfo)):
            item = BiqugeItem()
            item['title_url'] = "http://www.xbiquge.la" + str(bqgInfo[i])
            item['name'] = meta1['name']
            item['url'] = meta1['url']
            yield scrapy.Request(url=item['title_url'], meta={'meta2': item}, callback=self.parseBqgInfo,
                                 dont_filter=True)

    # 获取所有内容
    def parseBqgInfo(self, response):
        meta2 = response.meta['meta2']
        item = BiqugeItem()
        title = response.xpath("//div[@class='bookname']/h1/text()").extract()[0]
        print("内容页：" + title)
        item['title'] = title
        self.log("标题：" + str(title))
        content = response.xpath('//*[@id="content"]/text()').extract()
        item['novel'] = "\n".join(content).replace("&nbsp", " ")
        item['name'] = meta2['name']
        yield item
