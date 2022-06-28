import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("pyqt04.ui")[0]

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
        dan = int(self.le.text()) #몇 단 출력할것인가
        str = "";
        self.te.clear() #te에 있는 내용 지우기
        
        for i in range(1, 9+1):
            str = "{} * {} = {}".format(dan, i, (dan*i))
            self.te.append(str) #te에 출력하기
            
    #쌤 답
    def myclick2(self):
        dan = int(self.le.text()) #몇 단 출력할것인가
        str = "";
        
        for i in range(1, 9+1):
            str += "{} * {} = {}".format(dan, i, (dan*i))
            self.te.setText(str) #te에 출력하기
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
