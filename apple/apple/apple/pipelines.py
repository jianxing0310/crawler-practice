# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ApplePipeline(object):
	def open_spider(self, spider):
		self.conn = sqlite3.connect("apple.sqlite")
		self.cur = self.conn.cursor()
		self.cur.execute("creat table if not exists apple(title varcher(100),content text, time varcher(50)")
		#pass
		
	def close_spider(self, spider):
		self.conn.commit()
		self.conn.close()
		#pass
		
	def process_item(self, item, spider):
		col = ",".join(item.key())
		placeholders = ",".join(len(item) * "?")
		sql = "insert into apple({}) values({})"
		self.cur.execute(sql.format(col,placeholders),item.values())
		return item