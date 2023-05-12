import sys

from PyQt5.QtWidgets import *
import PyQt5.QtGui as qg
from PyQt5.QtCore import * 

# app = QApplication(sys.argv) #create application

# main_window = QMainWindow() # create main GUI window
# main_window.setWindowTitle("Trumpf request") 
# main_window.setGeometry(200, 200, 900, 800) 

# main_window.show() # show main GUI window
# app.exec_() # run loop until user press x

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 900, 800)
        self.setWindowTitle("Trumpf request")
        self.setWindowIcon(qg.QIcon("img/Logo_Trumpf.svg.png"))
        logo_trumpf_size = QSize(100, 100)
        self.setIconSize(logo_trumpf_size)
        
        self.top_label = QLabel("Trumpf tools", self)
        self.top_label.setGeometry(400, 0, 200, 60)
        self.top_label.setFont(qg.QFont("Times New Roman", 20)) #"Times New Roman", 16


        self.company_text = QLineEdit(None, self)
        self.company_text.setGeometry(200, 80, 300, 30)
        self.company_text.setFont(qg.QFont("Times New Roman", 16))

        self.company_label = QLabel("Компания: ", self)
        self.company_label.setGeometry(10, 80, 100, 20)
        self.company_label.setFont(qg.QFont("Times New Roman", 16))

        self.lable_top_logo = QLabel(self)
        self.lable_top_logo.setGeometry(50, 200, 100, 100)

        logo_top_img = qg.QPixmap("img/Logo_Trumpf.svg.png")

        self.lable_top_logo.setPixmap(logo_top_img)
        logo_top_img = logo_top_img.scaled(100, 100)
        
        #self.resize(self.logo_top_img.width(), self.logo_top_img.height())

        self.model_machine_text = QLineEdit(None, self)
        self.model_machine_text.setGeometry(200, 160, 300, 30)
        self.model_machine_text.setFont(qg.QFont("Times New Roman", 16))

        self.model_machine_label = QLabel("Модель верстата: ", self)
        self.model_machine_label.setGeometry(10, 160, 250, 20)
        self.model_machine_label.setFont(qg.QFont("Times New Roman", 16))

        self.test_label = QLabel("TEST", self)
        self.test_label.setGeometry(10, 300, 100, 20)
        self.test_label.setFont(qg.QFont("Times New Roman", 16))

        self.btnUpdate = QPushButton("Company and model", self)
        self.btnUpdate.setGeometry(300, 400, 200, 20)
        self.btnUpdate.clicked.connect(self.evt_btn_update_clicked)

        
    
    def evt_btn_update_clicked(self):
        a = self.company_text.text()
        b = self.model_machine_text.text()
        c = a + " " + b
        self.test_label.setText(c)



if __name__ == '__main__':
    my_app = QApplication(sys.argv) # create application
    main_window = MainWindow() # create main GUI
    main_window.show()
    sys.exit(my_app.exec_())
