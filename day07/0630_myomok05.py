import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton, QSize
from sqlalchemy.sql.expression import except_
# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myomok04.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        #흑백 번갈아하게 해줄 불린
        self.flagWB = True;
        #렌더링
        self.arr2D = [
            [0,0,0,0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,0,0,0,],
            
            [0,0,0,0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,0,0,0,]
        ]
        
        self.pb2D = []
        
        #버튼을 반복해서 생성하기
        for i in range(10):
            line = []
            for j in range(10):
                btn = QPushButton('', self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setIconSize(QSize(40, 40))
                btn.setGeometry((j*40), (i*40), 40, 40)
                btn.setToolTip('{},{}'.format(i, j))
                
                # 버튼과 연결하기
                btn.clicked.connect(self.myclick)
                
                # 배열에 생성한 버튼 넣기
                line.append(btn)
            
            # line 배열을 pbs 배열에 넣기
            self.pb2D.append(line)
        
        #돌 놓기
        self.myrender();
        
        # 화면을 보여준다.
        self.show()
        
    def myrender(self):
        # 이건 1차원 배열 -> 우린 2차원 배열로 해서 넣을 것
        # self.pbs[5].setIcon(QtGui.QIcon('1.png'))
        
        # 이건 2차원 배열에서 하나 찍기
        # self.pb2D[1][2].setIcon(QtGui.QIcon('1.png'))
        
        '''
            이벤트란?
            언제 발생할지 모르는 어떠한 일이 생기기 전까지 대기
        '''
        
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                elif self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                elif self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
    
    def myclick(self):
        str_ij = self.sender().toolTip()
        
        arr_ij = str_ij.split(",")
        j = arr_ij[0] #y값
        i = arr_ij[1] #x값
        
        y = int(j)
        x = int(i)
        
        if self.arr2D[y][x] > 0:
            return;
        
        stone = -1
        
        if self.flagWB and self.arr2D[y][x] == 0:
            self.arr2D[y][x] = 1
            self.flagWB = not self.flagWB
            
            stone = 1;
        elif not self.flagWB and self.arr2D[y][x] == 0:
            self.arr2D[y][x] = 2
            self.flagWB = not self.flagWB

            stone=2;
            
        up = self.checkUP(x, y, stone)
        dw = self.checkDW(x, y, stone)
        ri = self.checkRI(x, y, stone)
        le = self.checkLE(x, y, stone)
        
        ur = self.checkUR(x, y, stone)
        ul = self.checkUL(x, y, stone)
        dr = self.checkDR(x, y, stone)
        dl = self.checkDL(x, y, stone)
        
        print("↖ ul {} / ↑ up {} / ↗ ur {}".format(ur, up, ul))
        print("← le {} ////////// → ri {} ".format(le, ri))
        print("↙ dl {} / ↓ dw {} / ↘ dr {}".format(dr, dw, dl))
        
        print("\n===============\n")
        
        self.myrender()
            
    def checkUP(self, i, j, stone):
        cnt = 0;
        
        try:
            while(True):
                j += -1
                
                if(j < 0):
                    return cnt;
                
                if(i < 0):
                    return cnt;
                
                if self.arr2D[j][i] == stone:
                    cnt += 1;
                else :
                    return cnt;
        except:
            return cnt;
    
    def checkDW(self, i, j, stone):
        cnt = 0;
        
        try:
            while(True):
                j += 1
                
                if(j < 0):
                    return cnt;
                
                if(i < 0):
                    return cnt;
                
                if self.arr2D[j][i] == stone:
                    cnt += 1;
                else :
                    return cnt;
        except:
            return cnt;
    
    def checkRI(self, i, j, stone):
        cnt = 0;
        
        try:
            while(True):
                i += 1
                
                if(j < 0):
                    return cnt;
                
                if(i < 0):
                    return cnt;
                
                if self.arr2D[j][i] == stone:
                    cnt += 1;
                else :
                    return cnt;
        except:
            return cnt;
        
    def checkLE(self, i, j, stone):
        cnt = 0;
        
        try:
            while(True):
                i += -1
                
                if(j < 0):
                    return cnt;
                
                if(i < 0):
                    return cnt;
                
                if self.arr2D[j][i] == stone:
                    cnt += 1;
                else :
                    return cnt;
        except:
            return cnt;
        
    def checkUR(self, i, j, stone):
        cnt = 0;
        
        try:
            while(True):
                i += -1
                j += -1
                
                if(j < 0):
                    return cnt;
                
                if(i < 0):
                    return cnt;
                
                if self.arr2D[j][i] == stone:
                    cnt += 1;
                else :
                    return cnt;
        except:
            return cnt;
        
    def checkUL(self, i, j, stone):
        cnt = 0;
        
        try:
            while(True):
                i += 1
                j += -1
                
                if(j < 0):
                    return cnt;
                
                if(i < 0):
                    return cnt;
                
                if self.arr2D[j][i] == stone:
                    cnt += 1;
                else :
                    return cnt;
        except:
            return cnt;
        
    def checkDR(self, i, j, stone):
        cnt = 0;
        
        try:
            while(True):
                i += -1
                j += 1
                
                if(j < 0):
                    return cnt;
                
                if(i < 0):
                    return cnt;
                
                if self.arr2D[j][i] == stone:
                    cnt += 1;
                else :
                    return cnt;
        except:
            return cnt;
    
    def checkDL(self, i, j, stone):
        cnt = 0;
        
        try:
            while(True):
                i += 1
                j += 1
                
                if(j < 0):
                    return cnt;
                
                if(i < 0):
                    return cnt;
                
                if self.arr2D[j][i] == stone:
                    cnt += 1;
                else :
                    return cnt;
        except:
            return cnt;
        QMessageBox.about(self, 'Calling', str_tel)
    
    
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
