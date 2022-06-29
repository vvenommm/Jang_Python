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
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        #버튼을 반복해서 생성하기
        for j in range(10):
            for i in range(10):
                btn = QPushButton('', self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setIconSize(QSize(40, 40))
                btn.setGeometry((i*40), (j*40), 40, 40)
            
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
        self.pb.clicked.connect(self.myclick)
        # 화면을 보여준다.
        self.show()
        
        
    def myclick(self):
        # myIcon = QtGui.QIcon("1.png")
        self.pb.setIcon(QtGui.QIcon("1.png"))
        
        pass
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
