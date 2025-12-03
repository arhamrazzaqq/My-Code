import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
         super().__init__()
         self.setGeometry(700, 300, 500, 500)
         Label = QLabel("Hello", self)
         Label.setFont(QFont("Arial", 30))
         Label.setGeometry(0, 0, 500, 100)
         Label.setStyleSheet("color: #fca903;"
                             "Background-color: #6e1414;"
                             "font-style: italic;"
                             "font-weight: bold;"
                             "text-decoration: underline")
         #Label.setAlignment(Qt.AlignTop)  #vertically top
         Label.setAlignment(Qt.AlignBottom) #vertically bottoj
         #Label.setAlignment(Qt.AlignVCenter) #certically center
         #Label.setAlignment(Qt.AlignRight) #Horizontally right
         #Label.setAlignment(Qt.AlignHCenter) #Horizontally center
         #Label.setAlignment(Qt.AlignHRight) #Horizontally right
         #Label.setAlignment(Qt.AlignHLeft) #Horizontally left
         #Label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #center & top
         #Label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #center & bottom
         #Label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #center & center
         #Label.setAlignment(Qt.AlignCenter) #center & center
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()