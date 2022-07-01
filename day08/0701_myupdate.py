import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password = 'aa', db='python', charset='utf8', port=3305)

cur = conn.cursor()

e_id = "3"
e_name = "4"
sex = "4"
addr = "4"

#python 3.5 이상부터 f스트링
sql = f"update emp set e_name = '{e_name}', sex = '{sex}', addr = '{addr}' where e_id = '{e_id}'"
cnt = cur.execute(sql)

print(cnt)

conn.commit()
cur.close()
conn.close() # DB 연결 종료
