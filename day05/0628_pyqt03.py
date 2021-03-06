import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("pyqt03.ui")[0]

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
        
        '''
        text()는 C++에서 온 문법.
        '''
        
    def myclick(self):
        a = int(self.le.text())
        b = int(self.le2.text())
        sum = a+b
        self.le3.setText("{}".format(sum))
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
