import MySqldb

def conectadb():
    con = MySQLdb.connect(host="mysqlm.br", user="ord3", passwd="bale", db="ord3")
    con.select_db('ordebroc03')
    return "A"

print(conectadb())

