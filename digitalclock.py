import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt,QDateTime,QDate
from PyQt5.QtGui import QFont,QFontDatabase


class Digitalclock(QWidget):
    def __init__(self):
        super().__init__()
        self.initui()
        self.setWindowTitle("Digitalclock")
        self.timer = QTimer(self)
        self.time_label = QLabel(self)
        self.date_label = QLabel("ggg",self)


        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.date_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.date_label.setAlignment(Qt.AlignRight)
        # self.time_label.setStyleSheet(
        #                               "color: hsl(111,100%,50%)")
        self.time_label.setStyleSheet("color: red;")
        self.date_label.setStyleSheet("color: lime; "
                                      "font-size: 50px;"
                                      "font-style: italic;"
                                      "margin: 10px;"
                                      )

        self.setStyleSheet("background-color: black;")
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()


        clock_font = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(clock_font)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)



    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        current_date = QDate.currentDate().toString("dd,MM,yyyy")
        self.time_label.setText(current_time)
        self.date_label.setText(current_date)



    def initui(self):
        self.setGeometry(0,200,500,200)


def main():
    app = QApplication(sys.argv)
    clock = Digitalclock()
    clock.show()
    sys.exit(app.exec_())


if __name__ =='__main__':
    main()