import sys
import requests
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QLabel,QPushButton,QLineEdit
from PyQt5.QtCore import QTime,QTimer,Qt



class weather_app(QWidget):
    def __init__(self):
        super().__init__()
        self.title_label =QLabel("Enter A City",self)
        self.line_edit = QLineEdit(self)
        self.Get_weather = QPushButton("Get Weather", self)
        self.display_temperature = QLabel( self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel( self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Weather App")

        #layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.title_label)
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.Get_weather)
        vbox.addWidget(self.display_temperature)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        #styling
        self.emoji_label.setObjectName("emoji_label")
        self.title_label.setObjectName("title_label")
        self.display_temperature.setObjectName("temperature")
        self.description_label.setObjectName("description_label")
        self.line_edit.setObjectName("line_edit")

        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.display_temperature.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.line_edit.setAlignment(Qt.AlignCenter)



        self.setStyleSheet("""
            QLabel{
                font-family: calibri;
            }
            QLabel#emoji_label{
              font-family: Segoe ui emoji;
              font-size:120px;  
            }
            QLabel#title_label{
                font-size:30px;
                font-style: italic;
            }
            QLineEdit#line_edit{
               font-size:40px;
               
            }
             QLabel#description_label{
               font-size:60px;
            }
             QLabel#temperature{
               font-size:35px;
            }
            QPushButton{
                font-size:20px;
                font-weight:bold;
                background-color: grey;
            }
            
        """)

        #connector
        self.Get_weather.clicked.connect(self.get_weather)

#displays error message
    def display_error(self,message):
        self.display_temperature.setStyleSheet("font-size: 24px;")
        self.display_temperature.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()
#displays weather degree and weather condition
    def display_weather(self,data):
        self.display_temperature.setStyleSheet("font-size: 30px;")
        temperature_k = data["main"]["temp"]
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        self.description_label.setText(f"{weather_description}")
        self.display_temperature.setText(f"{temperature_k:.0f}K")
        self.emoji_label.setText(self.display_emoji(weather_id))
#gets weather checks api keys and check for error
    def get_weather(self):
        api_key = "d4c82a00491057f3e1ade1296a9ed627"
        city_name =  self.line_edit.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()


            if data["cod"]== 200:
                self.display_weather(data)
        except   requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("bad request\n please check your input ")
                case 401:
                    self.display_error("Unauthorized\n invalid api key ")
                case 403:
                    self.display_error("Forbidden\n access denied ")
                case 404:
                    self.display_error("Not Found\n city not found ")
                case 500:
                    self.display_error("Internal Server Error\n please try again")
                case _:
                    self.display_error(f"{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error \n Check Your Internet ")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error \n The Request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too mant redirect\n check the url")
        except requests.exceptions.RequestException as req_Error:
             self.display_error(f"request error\n{req_Error}" )
#displays emoji
    @staticmethod
    def display_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <=321:
            return"🌦️"
        elif 500 <= weather_id <=531:
            return"🌧️"
        elif 600 <= weather_id <=622:
            return"❄️"
        elif 701 <= weather_id <=781:
            return "🌪️"
        elif 800== weather_id:
            return"🌥️"
        elif 801 <= weather_id <=804:
            return "☁️"
        return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = weather_app()
    weather_app.show()
    sys.exit(app.exec_())