import pymysql

con = pymysql.connect(host='127.0.0.1', user='root', password = 'aa', db='python', charset='utf8', port=3305)

cur = con.cursor()

sql = "select * from emp"
cur.execute(sql)

rows = cur.fetchall()
con.close() # DB 연결 종료
print(rows)
