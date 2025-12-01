#CSS = Cadcading Style Sheets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout




class MainWindow(QMainWindow):
    def __init__(self):
         super().__init__()
         self.button1 = QPushButton("#1")
         self.button2 = QPushButton("#2")
         self.button3 = QPushButton("#3")
         self.setWindowTitle("Python GUI")
         self.initUI()

    def initUI(self):
         central_widget = QWidget()
         self.setCentralWidget(central_widget)

         hbox = QHBoxLayout()

         hbox.addWidget(self.button1)
         hbox.addWidget(self.button2)
         hbox.addWidget(self.button3)

         central_widget.setLayout(hbox)

         self.button1.setObjectName("button1")
         self.button2.setObjectName("button2")
         self.button3.setObjectName("button3")

         self.setStyleSheet("""
              QPushButton{
                    font-size: 20px;
                    font-family: Arial;
                    padding: 15px 50px;
                    margin: 15px;
                    border: 3px solid;
                    border-radius: 15px;
                }
                QPushButton#button1{
                   background-color: RED;
                }
                QPushButton#button2{
                   background-color: green;
                }
                QPushButton#button3{
                   background-color: blue;
                                  }
                         
             """)
         

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()