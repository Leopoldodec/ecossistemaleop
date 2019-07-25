import pymysql
from googletrans import Translator

conn = pymysql.connect(host='mysql.ordebroc.com.br', port=3306, user='ordebroc03', passwd='baleopleop19', db='ordebroc03')

cur = conn.cursor()
cur.execute("SELECT * FROM tb_forma_pgto")

print(cur.description)
print()

translator=Translator()
for row in cur:
    print(translator.translate(str(row[1]), dest="zh-CN").text)

cur.close()
conn.close()
