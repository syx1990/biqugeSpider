# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):
    name = scrapy.Field()  # 小说名字
    url = scrapy.Field()  # 小说章节目录
    title_url = scrapy.Field()  # 小说章节地址
    novel = scrapy.Field()  # 小说章节内容
    title = scrapy.Field()  # 小说章节标题
