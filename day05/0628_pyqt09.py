import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("pyqt09.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 버튼과 연결하기
        self.pb11.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.clickpb0)
        self.pb1.clicked.connect(self.clickpb1)
        self.pb2.clicked.connect(self.clickpb2)
        self.pb3.clicked.connect(self.clickpb3)
        self.pb4.clicked.connect(self.clickpb4)
        self.pb5.clicked.connect(self.clickpb5)
        self.pb6.clicked.connect(self.clickpb6)
        self.pb7.clicked.connect(self.clickpb7)
        self.pb8.clicked.connect(self.clickpb8)
        self.pb9.clicked.connect(self.clickpb9)
        # self.pb.clicked.connect(self.myclick2)
        
        # enter 치면 작동하는 이벤트 주기
        # lineEdit_search 이랑 Enter Key랑 Mapping
        # self.le3.returnPressed.connect(self.myclick)
        # 화면을 보여준다.
        self.show()
        
    def clickpb1(self):
        a = self.le.text()
        a += self.pb1.text()
        self.le.setText(a)
    
    # '''
    def clickpb2(self):
        a = self.le.text()
        a += self.pb2.text()
        self.le.setText(a)
    
    def clickpb3(self):
        a = self.le.text()
        a += self.pb3.text()
        self.le.setText(a)
    
    def clickpb4(self):
        a = self.le.text()
        a += self.pb4.text()
        self.le.setText(a)
    
    def clickpb5(self):
        a = self.le.text()
        a += self.pb5.text()
        self.le.setText(a)
    
    def clickpb6(self):
        a = self.le.text()
        a += self.pb6.text()
        self.le.setText(a)
    
    def clickpb7(self):
        a = self.le.text()
        a += self.pb7.text()
        self.le.setText(a)
    
    def clickpb8(self):
        a = self.le.text()
        a += self.pb8.text()
        self.le.setText(a)
    
    def clickpb9(self):
        a = self.le.text()
        a += self.pb9.text()
        self.le.setText(a)
    
    def clickpb0(self):
        a = self.le.text()
        a += self.pb0.text()
        self.le.setText(a)
    # '''
    
    def myclick(self):
        # self.pb1.
        pass
            
    
    #쌤 답
    def myclick2(self):
        pass
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
