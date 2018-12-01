# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 导入这个包为了移动文件
import shutil
#此包不解释
import scrapy
# 导入项目设置
from scrapy.utils.project import get_project_settings
# 导入scrapy框架的图片下载类
from scrapy.pipelines.images import ImagesPipeline
#此包不解释
import os

class ImagesPipelinse(ImagesPipeline):
    #def process_item(self, item, spider):
    #    return item
    # 获取settings文件里设置的变量值
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")
    # 重写ImagesPipeline类的此方法
    # 发送图片下载请求
    def get_media_requests(self, item, info):
        image_url = item["imge_url"]
        #headers是请求头主要是防反爬虫
        yield scrapy.Request(image_url,headers={'Referer':item['Referer']})

    def item_completed(self, result, item, info):
        image_path = [x["path"] for ok, x in result if ok]
        # 定义分类保存的路径
        img_path = "%s\%s" % (self.IMAGES_STORE, item['title'])
        # 目录不存在则创建目录
        if os.path.exists(img_path) == False:
            os.mkdir(img_path)
        # 将文件从默认下路路径移动到指定路径下
        shutil.move(self.IMAGES_STORE + "\\" +image_path[0], img_path + "\\" +image_path[0][image_path[0].find("full\\")+6:])
        item['image_Path'] = img_path + "\\" + image_path[0][image_path[0].find("full\\")+6:]
        return item