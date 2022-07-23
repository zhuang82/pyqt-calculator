import sys
from PyQt5 import QtCore,QtWidgets, uic
from time import ctime

form_class = uic.loadUiType(r"计算器.ui")[0]

class MainWindowClass(QtWidgets.QMainWindow,form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setFixedSize(310, 280)
        self.setupUi(self)
        #数字按钮
        self.pushButton_1.clicked.connect(self.button_1)
        self.pushButton_2.clicked.connect(self.button_2)
        self.pushButton_3.clicked.connect(self.button_3)
        self.pushButton_4.clicked.connect(self.button_4)
        self.pushButton_5.clicked.connect(self.button_5)
        self.pushButton_6.clicked.connect(self.button_6)
        self.pushButton_7.clicked.connect(self.button_7)
        self.pushButton_8.clicked.connect(self.button_8)
        self.pushButton_9.clicked.connect(self.button_9)
        self.pushButton_0.clicked.connect(self.button_0)
        #操作符
        self.pushButton_equal.clicked.connect(self.button_equal)
        self.pushButton_C.clicked.connect(self.c)
        self.pushButton_addition.clicked.connect(self.button_addition)
        self.pushButton_subtraction.clicked.connect(self.button_subtraction)
        self.pushButton_multiplication.clicked.connect(self.button_multiplication)
        self.pushButton_division.clicked.connect(self.button_division)
        #菜单
        self.actionExit.triggered.connect(self.exit)
        self.actionC_2.triggered.connect(self.c)
        #功能键
        self.pushButton_.clicked.connect(self.Button_)
        self.pushButton__.clicked.connect(self.Button__)

        self.result = ""
        
        ##print("[%s]"%ctime(),"done.")

    def button_1(self):
        self.result += "1"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'1',",self.result)

    def button_2(self):
        self.result += "2"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'2',",self.result)

    def button_3(self):
        self.result += "3"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'3',",self.result)

    def button_4(self):
        self.result += "4"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'4',",self.result)

    def button_5(self):
        self.result += "5"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'5',",self.result)

    def button_6(self):
        self.result += "6"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'6',",self.result)

    def button_7(self):
        self.result += "7"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'7',",self.result)

    def button_8(self):
        self.result += "8"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'8',",self.result)

    def button_9(self):
        self.result += "9"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'9',",self.result)

    def button_0(self):
        self.result += "0"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'0',",self.result)

    def button_equal(self):
        try:
            self.result = str(eval(self.result))
            self.label.setText(self.result)
            ##print("[%s]"%ctime(),"event:","'=',",self.result)
        except :
            self.label.setText("错误！")
            self.result = ""
            ##print("[%s]"%ctime(),"error:%s"%e)

    def button_addition(self):
        self.result += "+"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'+',",self.result)

    def button_subtraction(self):
        self.result += "-"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'-',",self.result)

    def button_multiplication(self):
        self.result += "*"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'*',",self.result)

    def button_division(self):
        self.result += "/"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'/',",self.result)

    def exit(self):
        self.close()
        ##print("[%s]"%ctime(),"exit.")

    def c(self):
        self.result = ""
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","清除")

    def Button_(self):
        self.result += "("
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","'(',",self.result)

    def Button__(self):
        self.result += ")"
        self.label.setText(self.result)
        ##print("[%s]"%ctime(),"event:","')',",self.result)

app = QtWidgets.QApplication(sys.argv)
window = MainWindowClass()
window.show()
app.exec_()
