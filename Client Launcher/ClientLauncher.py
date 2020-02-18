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
        self.ui.shutdownButton.hide()

        self.connect_buttons()

    def fonts(self):
        '''Add fonts to the application workspace.'''
        QFontDatabase.addApplicationFont(u':/fonts/Minecraftia.ttf')

    def connect_buttons(self):
        '''Connect button signals to handler functions.'''
        self.ui.connectButton.clicked.connect(self.connect_button_handler)
        self.ui.launchButton.clicked.connect(self.launch_button_handler)
        self.ui.shutdownButton.clicked.connect(self.shutdown_button_handler)
        self.ui.settingsButton.clicked.connect(self.settings_button_handler)

    def connect_button_handler(self):
        pass

    def launch_button_handler(self):
        pass

    def shutdown_button_handler(self):
        pass

    def settings_button_handler(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
