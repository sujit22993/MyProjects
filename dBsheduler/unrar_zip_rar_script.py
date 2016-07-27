
# import gzip
# with gzip.open("db-2016_07_24_18_00.sql.gz", 'rb') as infile:
#         with open("abc.sql", 'wb') as outfile:
#             for line in infile:
#                 outfile.write(line)


import MySQLdb
import datetime

import glob
print 

now = datetime.datetime.now()
month_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
db = MySQLdb.connect("localhost","root","root")
cursor = db.cursor()
month = month_list[now.month - 1]
day = str(now.day - 1)

cdate = 'dg_' + day + '_' + month
 
sql = '''create schema ''' + cdate

# cursor.execute(sql)
db.close()

file = open("sql_dump.bat", "w")

dbName = glob.glob("*.sql")

line1 = "mysql -uroot -proot " + cdate + ' < ' + dbName[0]  + ';\n'
line2 = "PAUSE"

file.write(line1)
file.write(line2)
