
class Xi:
    def __init__(self):
        self.money = 1000;
    
    def copycopy(self, money):
        self.money += money;
        
###############################################

class Putin:
    def __init__(self):
        self.cnt_hair = 300;
    
    def stress(self, cnt):
        self.cnt_hair -= cnt;

###############################################

class Jeongeun2:
    def __init__(self):
        self.nuclear = 20;
    
    def ssorau(self, cnt):
        self.nuclear -= cnt;

###############################################

class SeungJe(Xi, Putin, Jeongeun2):
    def __init__(self):
        Xi.__init__(self)
        Putin.__init__(self)
        Jeongeun2.__init__(self)
        
###############################################


if __name__ == '__main__':
    sj = SeungJe()
    print(sj.money)
    print(sj.cnt_hair)
    print(sj.nuclear)
    sj.copycopy(1)
    sj.stress(50)
    sj.ssorau(20)
    print(sj.cnt_hair)
    print(sj.money)
    print(sj.nuclear)
