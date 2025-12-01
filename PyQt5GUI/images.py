import sys
import os.path
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python GUI")
        self.setGeometry(700, 300, 500, 500)

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        
        img_path = os.path.join(os.path.dirname("PyQt5GUI/images.py"),"profile_picture.jpeg")
        pixmap = QPixmap(img_path)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        
        label.setGeometry((self.width() - label.width()) // 2,#for centering the image in the window(do this with the height aswell;)
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height())
                          #self.width() - label.width()) #for top right corner
                          #self.height() - label.height() #for bottom right corner
                          # value of x to be zero for bottom left corner

        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

