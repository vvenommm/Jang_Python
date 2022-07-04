import pymysql

class EmpDao:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password = 'aa', db='python', charset='utf8', port=3305)
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def myselects(self):
        sql = "select * from emp"
        self.curs.execute(sql)
        
        rows = self.curs.fetchall()
        return rows[0]
    
    def selectone(self, e_id):
        sql = f"select e_id, e_name, sex, addr from emp where e_id = '{e_id}'"
        self.curs.execute(sql)
        
        row = self.curs.fetchall()
        return row
    
    def myinsert(self, e_id, e_name, sex, addr):
        sql = f"insert into emp values('{e_id}', '{e_name}', '{sex}', '{addr}')"
        cnt = self.curs.execute(sql)
        
        self.conn.commit()
        return cnt
        
    def mydelete(self, e_id):
        sql = f"delete from emp where e_id = '{e_id}'"
        cnt = self.curs.execute(sql)
        
        self.conn.commit()
        return cnt
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    ed = EmpDao()
    # list = ed.myselects() #튜플로 나옴
    # print(list)
    
    # emp = ed.selectone('1')
    # print(emp)
    
    # cnt = ed.myinsert('4', 'haha', '09kok9m0oi ,ljiiiiiiiF', "ferari")
    # print(cnt)
    
    cnt = ed.mydelete('4')
    print(cnt)
        
