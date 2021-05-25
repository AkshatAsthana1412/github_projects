# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3 as lite

class StoreInDBPipeline:
    # def __init__(self):
    #     self.setup_db_connection()
    #     self.drop_topfilms_table()
    #     self.create_topfilms_table()
    
    # def setup_db_connection(self):
    #     self.con = lite.connect('topfilms.db')
    #     self.cur = self.con.cursor()
    
    # def drop_topfilms_table(self):
    #     self.cur.execute('DROP TABLE IF EXISTS topfilms')
    
    # def create_topfilms_table(self):
    #     self.cur.execute('CREATE TABLE IF NOT EXISTS topfilms(\
    #         id INTEGER PRIMARY KEY NOT NULL,\
    #         title TEXT,\
    #         channel TEXT,\
    #         start_ts TEXT,\
    #         film_date_long TEXT,\
    #         film_date_short TEXT,\
    #         rating TEXT,\
    #         genre TEXT,\
    #         plot TEXT,\
    #         tmdb_link TEXT,\
    #         release_date TEXT,\
    #         nb_votes INTEGER)')
        
    # def store_in_db(self, item):
    #     self.cur.execute("INSERT INTO topfilms(\
    #         title, \
    #         channel, \
    #         start_ts, \
    #         film_date_long, \
    #         film_date_short, \
    #         rating, \
    #         genre, \
    #         plot, \
    #         tmdb_link, \
    #         release_date, \
    #         nb_votes \
    #         ) \
    #         VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )",
    #         (
    #         item['title'],
    #         item['channel'],
    #         item['start_ts'],
    #         item['film_date_long'],
    #         item['film_date_short'],
    #         float(item['rating']),
    #         item['genre'],
    #         item['plot'],
    #         item['tmdb_link'],
    #         item['release_date'],
    #         item['nb_votes']
    #         ))
    #     self.con.commit()

    # def process_item(self, item, spider):
    #     self.store_in_db(item)
    #     return item

    # def __del__(self):
    #     self.close_db()

    # def close_db(self):
    #     self.con.close()
    pass