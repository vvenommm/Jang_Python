import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton, QSize
# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myomok02.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        #MainClass 바깥에 써도 되지만 그건 그냥 파일을 읽으면서 memory에 올라간 것 뿐이지, oop 개념에 해당하는 전역변수는 아님. 따라서 파이썬의 경우 전역변수는 이 위치에 적는 것이 문법이고 규칙이고 FM이다.
        self.flag = True;
        
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        #버튼을 반복해서 생성하기
        for j in range(10):
            for i in range(10):
                btn = QPushButton('', self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setIconSize(QSize(40, 40))
                btn.setGeometry((i*40), (j*40), 40, 40)
                btn.clicked.connect(self.myclick)
            
        '''
        btn = QPushButton('', self)
        btn.setIcon(QtGui.QIcon('0.png'))
        btn.setIconSize(QSize(40, 40))
        btn.setGeometry(0, 0, 40, 40)
        
        btn = QPushButton('', self)
        btn.setIcon(QtGui.QIcon('0.png'))
        btn.setIconSize(QSize(40, 40))
        btn.setGeometry(40, 0, 40, 40)
        '''
            
        # 버튼과 연결하기
        # self.btn.clicked.connect(self.myclick)
        # 화면을 보여준다.
        self.show()
        
    def myclick(self):
        if(self.flag):
            btn = self.sender()
            btn.setIcon(QtGui.QIcon('1.png'))
            # self.flag = False;
        else :
            self.sender().setIcon(QtGui.QIcon('2.png'))
            # self.flag = True;
        
        self.flag = not self.flag
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
