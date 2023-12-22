from Controller import MainController
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainController()
    window.show()
    sys.exit(app.exec_())








