#import requests
import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QPushButton
,QCheckBox,QRadioButton,QButtonGroup,QLineEdit)
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt,pyqtSignal,QObject



class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Gpyks Gui")
        self.button = QPushButton("Submit",self)
        # self.label = QLabel("Waiting",self)
        # self.checkbox = QCheckBox("Are you Straight", self)
        self.setGeometry(500,200,500,500)
        # self.botton_group1 = QButtonGroup(self)
        # self.botton_group2 = QButtonGroup(self)
        # self.botton1 = QRadioButton("offline", self)
        # self.botton2 = QRadioButton("online", self)
        # self.botton3 = QRadioButton("yes", self)
        # self.botton4= QRadioButton("no", self)
        self.line_edit = QLineEdit(self)
        self.initui()




        # label = QLabel("Hello ", self)
        # label.setGeometry(0,0,250,250)
        # label.setFont(QFont("Ariel", 24))
        # label.setStyleSheet("color: White;"
        #                     "background-color: Black;"
        #                     "font-style : italic"
        #                     )
        # label.setAlignment(Qt.AlignCenter)
        #


#to manipulate the position of the image
        # label.setGeometry((self.width()- label.width()) //2 ,
        #                   (self.height()-label.height()) // 2,
        #                   label.width(),
        #                   label.height())

    def initui (self):
        central_widget = QWidget()
        # self.setCentralWidget(central_widget)
        #
        #
        #
        # label1 = QLabel("Section 1",self)
        # label2 = QLabel("section 2",self)
        # label3 = QLabel("section 3",self)
        #
        #
        # pixmap = QPixmap("Screenshot 2025-08-15 130702.png")
        # label1.setPixmap(pixmap)
        # label1.setScaledContents(True)
        # label2.setStyleSheet("background-color: Black; color: white;")
        # label3.setStyleSheet("background-color: Green;")
        #
        # vbox = QVBoxLayout()
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        #
        # central_widget.setLayout(vbox)
        self.button.setGeometry(320,10,100,50)
        self.button.clicked.connect(self.on_click)
        self.line_edit.setGeometry(10,10,300,50)
        self.line_edit.setStyleSheet("font-size: 20px;"
                                     )
        self.line_edit.setPlaceholderText("Enter Your Name")
        # self.label.setGeometry(100,300,500,100)
        # self.label.setStyleSheet("font-weight: bold;"
        #                          "font-size: 50px;")
        #
        # self.checkbox.setGeometry(10,0,400,100)
        # self.checkbox.setStyleSheet("font-size: 30px;")
        # # self.checkbox.setChecked(False)
        # self.checkbox.stateChanged.connect(self.on_check)

        # self.botton1.setGeometry(0,0,300,100)
        # self.botton2.setGeometry(0, 50, 300, 100)
        # self.botton3.setGeometry(0, 100, 300, 100)
        # self.botton4.setGeometry(0, 150, 300, 100)
        # self.setStyleSheet("QRadioButton{""font-size: 15px;"
        #                    "font-style: bold;"
        #                    "padding: 10px;""}")
        #
        #
        # self.botton_group1.addButton(self.botton1)
        # self.botton_group1.addButton(self.botton2)
        # self.botton_group2.addButton(self.botton3)
        # self.botton_group2.addButton(self.botton4)
        #
        # self.botton1.toggled.connect(self.on_toggled)
        # self.botton2.toggled.connect(self.on_toggled)
        # self.botton3.toggled.connect(self.on_toggled)
        # self.botton4.toggled.connect(self.on_toggled)



    def on_toggled(self):
        radio_clicked = self.sender()
        if radio_clicked.isChecked():
            print(f"{radio_clicked.text( )} is selected")


    def on_check(self,state):
        if state ==  Qt.Checked:
            print("you are not Gay")
        else:
            print("You are Gay")

    def on_click(self):
        text_click = self.line_edit.text()
        print(f"Hello {text_click}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()#to show the window dor a few seconds
    sys.exit(app.exec_())#to stay for some time until, we close it

if __name__ == '__main__':
    main()
