# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BiqugePipeline(object):
    def process_item(self, item, spider):
        # 同一个小说按章节名字保存txt文件
        print("test: "+str(item['name']) + '/' + str(item['title']) + ".txt")
        fp = open(str(item['name']) + '/' + str(item['title']) + ".txt", "a", encoding='utf8')
        fp.write(str(item['title']))
        fp.write('\n')
        novel = str(item['novel']).encode('GBK', 'ignore').decode('GBk')  # 转码，否则报错
        fp.write(novel)
        fp.write('\n')
        fp.close()
        return item
