import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("pyqt06.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 버튼과 연결하기
        # self.pb.clicked.connect(self.myclick)
        
        # enter 치면 작동하는 이벤트 주기
        # lineEdit_search 이랑 Enter Key랑 Mapping
        self.le3.returnPressed.connect(self.myclick)
        # 화면을 보여준다.
        self.show()
        
    def myclick(self):
        start = int(self.le1.text())
        end = int(self.le2.text())
        num = int(self.le3.text())
        result = 0;
        
        for i in range(start, end+1):
            if(i%num == 0):
                result += i;
        
        self.le4.setText(str(result))
            
    #쌤 답
    def myclick2(self):
       pass
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
