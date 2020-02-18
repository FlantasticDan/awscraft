import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QFontDatabase
from launcher import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.fonts()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.connectButton.clicked.connect(lambda: self.ui.launchButton.setEnabled(True))
    
    def fonts(self):
        QFontDatabase.addApplicationFont(u':/fonts/Minecraftia.ttf')

def printer(string):
    print(string)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())