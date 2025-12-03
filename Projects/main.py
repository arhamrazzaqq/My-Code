import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
#window costumization
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To Do List")
        self.setGeometry(700, 300, 400, 400)
        self.setStyleSheet("background-color: #161722;") 
        self.label  = QLabel("TODAY'S TO DO LIST!", self)
        self.check1 = QCheckBox("BreakFast", self)
        self.check2 = QCheckBox("Office", self)
        self.check3 = QCheckBox("Lunch", self)
        self.check4 = QCheckBox("Meeting", self)
        self.check5 = QCheckBox("Snack Time", self)
        self.check6 = QCheckBox("Dinner", self)
        self.check1.setGeometry(10,40,300,40)
        self.check2.setGeometry(10,100,300,40)
        self.check3.setGeometry(10,160,300,40)
        self.check4.setGeometry(10,220,300,40)
        self.check5.setGeometry(10,280,300,40)
        self.check6.setGeometry(10,340,300,40)
        self.label.setGeometry(10,0,299,39)
        self.initUI()
#Font design
    def initUI(self):
        
        self.label.setStyleSheet("color: #34cceb;"
                                  "font-size: 20px;"
                                  "font-weight: Bold;"
                                  "font-family: Georgia;")
        
        
        self.check1.setStyleSheet("color: #34cceb;"
                                  "font-size: 20px;"
                                  "font-weight: Bold;"
                                  "font-family: Georgia;")
        self.check2.setStyleSheet("color: #34cceb;"
                                  "font-size: 20px;"
                                  "font-weight: Bold;"
                                  "font-family: Georgia;")
        self.check3.setStyleSheet("color: #34cceb;"
                                  "font-size: 20px;"
                                  "font-weight: Bold;"
                                  "font-family: Georgia;")
        self.check4.setStyleSheet("color: #34cceb;"
                                  "font-size: 20px;"
                                  "font-weight: Bold;"
                                  "font-family: Georgia;")
        self.check5.setStyleSheet("color: #34cceb;"
                                  "font-size: 20px;"
                                  "font-weight: Bold;"
                                  "font-family: Georgia;")
        self.check6.setStyleSheet("color: #34cceb;"
                                  "font-size: 20px;"
                                  "font-weight: Bold;"
                                  "font-family: Georgia;")
#checkbox confirmation        
        self.check1.setChecked(False)
        self.check1.stateChanged.connect(self.checkedbox_changed)
        self.check2.setChecked(False)
        self.check2.stateChanged.connect(self.checkedbox_changed)
        self.check3.setChecked(False)
        self.check3.stateChanged.connect(self.checkedbox_changed)
        self.check4.setChecked(False)
        self.check4.stateChanged.connect(self.checkedbox_changed)        
        self.check5.setChecked(False)
        self.check5.stateChanged.connect(self.checkedbox_changed)        
        self.check6.setChecked(False)
        self.check6.stateChanged.connect(self.checkedbox_changed)

#if else statement for change                
    def checkedbox_changed(self, state):
        if state == Qt.Checked:
         print("Task Completed")
        else:
            print("Task remaining")

        total_checked = (
            self.check1.isChecked() +
            self.check2.isChecked() +
            self.check3.isChecked() +
            self.check4.isChecked() +
            self.check5.isChecked() +
            self.check6.isChecked() 
            )
        if total_checked ==6:
            print("done")

        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
