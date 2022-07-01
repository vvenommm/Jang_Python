import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password = 'aa', db='python', charset='utf8', port=3305)

cur = conn.cursor()

"""이걸 쓰면 엔터를 쳐도 다 문자열로 인식"""
'''주석'''

sql = "insert into emp values(%s, %s, %s, %s)"
cnt = cur.execute(sql, (3, 3, 3, 3))

print(cur.rowcount)
print(cnt)

conn.commit()
cur.close()
conn.close() # DB 연결 종료
