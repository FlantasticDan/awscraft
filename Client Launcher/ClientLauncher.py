import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2.QtGui import QFontDatabase
from PySide2.QtCore import Qt
from launcher import Ui_MainWindow
from config import Ui_settingsDialog
from settings import ConfigurationSettings

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.fonts()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.shutdownButton.hide()

        self.connect_buttons()

        self.settings = ConfigDialog(self)

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
        self.settings.exec_()

class ConfigDialog(QDialog):
    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__(parent, Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint)

        self.dialog = Ui_settingsDialog()
        self.dialog.setupUi(self)

        self.config = ConfigurationSettings()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    if window.settings.config.start():
        window.ui.settingsButton.click()

    window.show()

    sys.exit(app.exec_())
