import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("pyqt08.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 버튼과 연결하기
        self.pb.clicked.connect(self.myclick)
        # self.pb.clicked.connect(self.myclick2)
        
        # enter 치면 작동하는 이벤트 주기
        # lineEdit_search 이랑 Enter Key랑 Mapping
        # self.le3.returnPressed.connect(self.myclick)
        # 화면을 보여준다.
        self.show()
        
    def myclick(self):
        start = int(self.le1.text())
        end = int(self.le2.text())
        
        self.te.clear()
        
        str = "";
        if(start < end):
            for i in range(start):
                str += "*"
            for i in range(end-(start-1)):
                self.te.append(str)
                str += "*"
        else:
            for i in range(end):
                str += "*"
            for i in range(end-(start-1)):
                self.te.append(str)
                str.replace('*', '', 1)
                    
        # str = add(start);
            
    def getStar(self, cnt):
        str = ""
        for i in range(cnt):
            str += "*"
        str += "/n"
        return str;
    
    #쌤 답
    def myclick2(self):
        a - int(self.le1.text())
        b - int(self.le2.text())
        
        txt = ""
        
        for i in range (a, b+1):
            txt += self.getStar(i)
            
        self.te.setText(txt);
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
