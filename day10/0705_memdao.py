import pymysql

class MemDao:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password = 'aa', db='python', charset='utf8', port=3305)
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def memSelects(self):
        sql = "select * from mem"
        self.curs.execute(sql)
        
        rows = self.curs.fetchall()
        return rows
    
    def memSelect(self, m_id):
        sql = f"select m_id, m_name, m_tel, m_addr from mem where m_id = '{m_id}'"
        self.curs.execute(sql)
        
        row = self.curs.fetchone()
        return row
    
    def memInsert(self, m_name, m_tel, m_addr):
        sql = f"insert into mem (m_name, m_tel, m_addr) values('{m_name}', '{m_tel}', '{m_addr}'"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def memUpdate(self, m_id, m_name, m_tel, m_addr):
        sql = f"update mem set m_name='{m_name}', m_tel='{m_tel}', m_addr='{m_addr}' where m_id='{m_id}'"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close();
        self.conn.close();
