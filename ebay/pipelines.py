import json
import os
import re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class EbayPipeline:
    def process_item(self, item, spider):

        if not os.path.exists("products"):
            os.makedirs("products")

        id = re.search(r'/(\d+)(?:$|\?)', item.get("product_url")).group(1)
        file_name = f"{id}.json"
        file_path = os.path.join("products", file_name)

        with open(file_path, 'w') as json_file:
            json.dump(item, json_file, indent=4)
        return item
