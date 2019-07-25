import MySqldb

def conectadb():
    con = MySQLdb.connect(host="mysql.ordebroc.com.br", user="ordebroc03", passwd="baleopleop19", db="ordebroc03")
    con.select_db('ordebroc03')
    return "A"

print(conectadb())

