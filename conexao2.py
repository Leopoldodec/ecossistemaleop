import pymysql
from googletrans import Translator

conn = pymysql.connect(host='mbr', port=3306, user='03', passwd='b', db='or')

cur = conn.cursor()
cur.execute("SELECT * FROM tb_forma_pgto")

print(cur.description)
print()

translator=Translator()
for row in cur:
    print(translator.translate(str(row[1]), dest="zh-CN").text)

cur.close()
conn.close()
