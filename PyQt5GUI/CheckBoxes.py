import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt




class MainWindow(QMainWindow):
    def __init__(self):
         super().__init__()
         self.setWindowTitle("Python GUI")
         self.setGeometry(700, 300, 500, 500)
         self.checkbox = QCheckBox("Do you Like food?", self)
         self.checkbox1 = QCheckBox("Do you Like food?", self)
         self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(0, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px'"
                                    "font-family: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkedbox_changed)

    def checkedbox_changed(self, state):
        if state == Qt.Checked:
         print("You Like Food")
        else:
            print("You do NOT like food")
         

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()