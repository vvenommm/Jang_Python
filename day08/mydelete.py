import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password = 'aa', db='python', charset='utf8', port=3305)

cur = conn.cursor()

sql = "delete from emp where e_id = %s"
cnt = cur.execute(sql, (3))

print(cnt)

conn.commit()
cur.close()
conn.close() # DB 연결 종료
