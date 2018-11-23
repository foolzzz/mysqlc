
import MySQLdb

host = "192.168.30.242"
db = MySQLdb.connect(host=host,user='root',passwd='123455',db='test_DB')

conn = db.cursor()

conn.execute("select 123");


import pdb;pdb.set_trace()



