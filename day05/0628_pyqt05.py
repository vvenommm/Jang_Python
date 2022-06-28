import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("pyqt05.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 버튼과 연결하기
        self.pb.clicked.connect(self.myclick)
        # 화면을 보여준다.
        self.show()
        
    def myclick(self):
        mine = self.leMine.text()
        com = ""
        
        rnd = int(random()*100)
        if(rnd % 2 == 0):
            self.leCom.setText("짝")
            com = self.leCom.text()
        else : 
            self.leCom.setText("홀")
            com = self.leCom.text()
        
        if(mine == com):
            self.leResult.setText("승리! 정답입니다!")
        else :
            self.leResult.setText("패배! 틀렸습니다!")
            
    #쌤 답
    def myclick2(self):
       pass
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
