import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
                            



class MainWindow(QMainWindow):
    def __init__(self):
         super().__init__()
         self.setWindowTitle("Python GUI")
         self.setGeometry(700, 300, 500, 500)
         self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: blue;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: red;")
        label4.setStyleSheet("background-color: green;")
        label5.setStyleSheet("background-color: purple;")

        vbox = QGridLayout()
       #vbox = QHBoxLayout()  @for horizontal box
       #Vbox = QVBoxLayout()  @for vertical box

        vbox.addWidget(label1, 0, 0)
        vbox.addWidget(label2, 0, 1)
        vbox.addWidget(label3, 1, 0) #you do not need to write rows or coloumn for H & V 
        vbox.addWidget(label4, 1, 1)
        vbox.addWidget(label5, 2, 2)

        central_widget.setLayout(vbox)



         

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
