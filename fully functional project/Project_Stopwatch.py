import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QPushButton
from PyQt5.QtCore import QTime,QTimer,Qt



class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time =QTime(0,0,0,0)
        self.timer = QTimer(self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.time_label = QLabel("00:00:00:00",self)
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle("Stopwatch")

        #Add Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        #Styling
        self.time_label.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
            QPushButton,QLabel{
                   font-family: calibri;
                   padding:20px; 
                   border-radius: 20px;
            }
            
            QPushButton{
                background-color:#96744d;
                font-size:30px;
            }
            
            QLabel{
                background-color: #ebb678;
                font-size: 120px;
            }
            
            QPushButton:hover{
                background-color:#413221;
            }
            
        """)
        #connectors
        self.start_button.clicked.connect(self.start_time)
        self.stop_button.clicked.connect(self.stop_time)
        self.reset_button.clicked.connect(self.reset_time)

        self.timer.timeout.connect(self.update_time)


    def start_time(self):
        self.timer.start()
    def stop_time(self):
        self.timer.stop()
    def reset_time(self):
        self.timer.stop()
        self.time_label.setText("00:00:00:00")

    def format_time(self, time):
        hour = time.hour()
        minute = time.minute()
        seconds = time.second()
        mil_seconds = time.msec()
        return f"{hour:02}:{minute:02}:{seconds:02}:{mil_seconds:03}"

    def update_time(self):
        self.time = self.time.addMSecs(1)
        self.time_label.setText(self.format_time(self.time))






if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())