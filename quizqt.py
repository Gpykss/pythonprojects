import sys
from PyQt5.QtWidgets import QCheckBox, QApplication, QLabel, QPushButton, QMainWindow, QHBoxLayout, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.checkbox = QCheckBox("Dark mode", self)
        # self.label = QLabel("Hello Gpyks", self)
        # self.setGeometry(0,0,500,500)
        self.pushbutton1 = QPushButton("1")
        self.pushbutton2 = QPushButton("2")
        self.pushbutton3 = QPushButton("3")
        self.pushbutton4 = QPushButton("4")
        self.initui()




    def initui(self):
        central_Widget   = QWidget()
        self.setCentralWidget(central_Widget)
        # self.label.setGeometry(0, 0, 500, 50)
        # self.label.setStyleSheet("font-size: 10px;"
        #                     "background-color: yellow;")
        # self.label.setAlignment(Qt.AlignCenter)
        # self.pushbutton.setGeometry(200,80,100,50)
        # self.pushbutton.clicked.connect(self.on_click)
        #
        # self.checkbox.setGeometry(200,100,300,100)
        # self.checkbox.setStyleSheet("font-size:20px;")
        # self.checkbox.setChecked(False)
        # self.checkbox.stateChanged.connect(self.on_check)
        hbox = QHBoxLayout()

        hbox.addWidget(self.pushbutton1)
        hbox.addWidget(self.pushbutton2)
        hbox.addWidget(self.pushbutton3)
        hbox.addWidget(self.pushbutton4)
        central_Widget.setLayout(hbox)

        self.pushbutton1.setObjectName("pushbotton1")
        self.pushbutton2.setObjectName("pushbotton2")
        self.pushbutton3.setObjectName("pushbotton3")
        self.pushbutton4.setObjectName("pushbotton4")

        self.setStyleSheet("""
           
            QPushButton{
                font-size: 15px;
                padding: 20px 50px;
                margin: 40px 20px;
                border: 2px solid;
                border-radius: 10px;
            }
            QPushButton#pushbotton1:hover{
                background-color:10% white;
            }
            
            QPushButton#pushbotton1{
                background-color: blue;
            }
            
            QPushButton#pushbotton2{
                background-color: green;
            }
            
            QPushButton#pushbotton3{
                background-color: red;
            }
            
            QPushButton#pushbotton4{
                background-color: yellow;
            }
            
        """)



    # def on_click(self):
    #     # self.label.setText("You clicked the button")
    #
    # def on_check(self,state):
    #     # if state == Qt.Checked:
    #     #     self.setStyleSheet("background-color: black;"
    #     #                        "color: white;")
    #     # else:
    #     #     self.setStyleSheet("background-color: white;"
    #     #                        "color: black;")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()