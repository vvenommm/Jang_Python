import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("pyqt07.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 버튼과 연결하기
        # self.pb.clicked.connect(self.myclick)
        # self.pb.clicked.connect(self.myclick2)
        self.pb.clicked.connect(self.myclick3)
        
        # enter 치면 작동하는 이벤트 주기
        # lineEdit_search 이랑 Enter Key랑 Mapping
        # self.le3.returnPressed.connect(self.myclick)
        # 화면을 보여준다.
        self.show()
        
    def myclick(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45]
        
        for i in range(50):
            rnd = int(random()*45)
            temp = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = temp
        
        self.lbl1.setText(str(arr[0]))
        self.lbl2.setText(str(arr[1]))
        self.lbl3.setText(str(arr[2]))
        self.lbl4.setText(str(arr[3]))
        self.lbl5.setText(str(arr[4]))
        self.lbl6.setText(str(arr[5]))
            
    #쌤 답 1
    def myclick2(self):
       #myRandom 1 방법으로
       
        arr45 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45]
        
        for i in range(100):
            #random이 임포트 안 된 상태면 random.random()으로 해야함
            rnd = int(random()*len(arr45))
            a = arr45[rnd];
            b = arr45[0];
            arr45[0] = a;
            arr45[rnd] = b;
        
        self.lbl1.setText(str(arr45[0]))
        self.lbl2.setText(str(arr45[1]))
        self.lbl3.setText(str(arr45[2]))
        self.lbl4.setText(str(arr45[3]))
        self.lbl5.setText(str(arr45[4]))
        self.lbl6.setText(str(arr45[5]))
    
    #쌤 답 2
    def myclick3(self):
        #myRandom 3 방법으로
        
        arr45 = list(range(1, 45+1))
        arr6 = []
       
        for i in range(6):
            rnd = int(random()*len(arr45))
            a = arr45.pop(rnd)
            arr6.append(a)
        self.lbl1.setText(str(arr6[0]))
        self.lbl2.setText(str(arr6[1]))
        self.lbl3.setText(str(arr6[2]))
        self.lbl4.setText(str(arr6[3]))
        self.lbl5.setText(str(arr6[4]))
        self.lbl6.setText(str(arr6[5]))
       
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
