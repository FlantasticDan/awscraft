import sys
import os
import asyncio
import threading
import subprocess
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from PySide2.QtGui import QFontDatabase, QIcon
from PySide2.QtCore import Qt, QSize
from launcher import Ui_MainWindow
from config import Ui_settingsDialog
from settings import ConfigurationSettings
import server_connection as server

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
        self.update_connect_button(1)
        ip = server.connect_to_server()
        self.update_connect_button(2)
        self.server = server.WebsocketHandler(ip, self.settings.config.get_display_name(), self)

        t = threading.Thread(target=self.thread_runner)
        t.start()

    def thread_runner(self):
        asyncio.run(self.server.connect())

    def update_connect_button(self, stage: int, ip=''):
        '''Updates the Connect Button with Relevant Status.'''
        stages = [
            'Connect to Server',
            '[1/2] Requesting Server',
            '[2/2] Waiting for Server',
            f'Connected to {ip}'
        ]
        self.ui.connectButton.setText(stages[stage])
        if stage > 0:
            self.ui.connectButton.setEnabled(False)
            if stage == 3:
                self.settings.config.update_server_address(ip)
                self.ui.launchButton.setEnabled(True)
        else:
            self.ui.connectButton.setEnabled(True)

    def launch_button_handler(self):
        subprocess.Popen(self.settings.config.launcher)

    def shutdown_button_handler(self):
        pass

    def settings_button_handler(self):
        self.settings.open_dialog()

class ConfigDialog(QDialog):
    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__(parent, Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint)

        self.dialog = Ui_settingsDialog()
        self.dialog.setupUi(self)

        self.connect_buttons()

        self.config = ConfigurationSettings()

    def connect_buttons(self):
        '''Connect button signals to handler functions.'''
        self.dialog.saveButton.clicked.connect(self.save_button_handler)
        self.dialog.dataDetectButton.clicked.connect(self.data_detect_button_handler)
        self.dialog.launcherDetectButton.clicked.connect(self.launcher_detect_button_handler)
        self.dialog.dataBrowseButton.clicked.connect(self.data_browse_button_handler)
        self.dialog.launcherBrowseButton.clicked.connect(self.launcher_browse_button_handler)


    def save_button_handler(self):
        self.config.host = self.dialog.serverInput.text()
        self.config.user_id = self.dialog.userInput.text()
        self.config.data_directory = self.dialog.dataInput.text()
        self.config.launcher = self.dialog.launcherInput.text()

        self.config.save()
        self.close()

    def data_detect_button_handler(self):
        if self.config.find_minecraft_data():
            self.dialog.dataDetectButton.setEnabled(False)
            self.dialog.dataDetectButton.setText('Success')
            self.dialog.dataInput.setText(self.config.data_directory)
            return
        else:
            self.dialog.dataDetectButton.setEnabled(False)
            self.dialog.dataDetectButton.setText('Failed')

    def data_browse_button_handler(self):
        path = QFileDialog.getExistingDirectory(self, 'Browse for .minecraft')
        self.dialog.dataInput.setText(os.path.abspath(path))
        self.auto_detect_button_reset(self.dialog.dataDetectButton)

    def launcher_browse_button_handler(self):
        path = QFileDialog.getOpenFileName(self, 'Browse for MinecraftLauncher.exe', '', 'Executables (*.exe)')
        self.dialog.launcherInput.setText(os.path.abspath(path[0]))
        self.auto_detect_button_reset(self.dialog.launcherDetectButton)

    def launcher_detect_button_handler(self):
        if self.config.find_minecraft_launcher():
            self.dialog.launcherDetectButton.setEnabled(False)
            self.dialog.launcherDetectButton.setText('Success')
            self.dialog.launcherInput.setText(self.config.launcher)
            return
        else:
            self.dialog.launcherDetectButton.setEnabled(False)
            self.dialog.launcherDetectButton.setText('Failed')
    
    def auto_detect_button_reset(self, button):
        '''Resets Configurations Settings 'Auto Detect' Buttons'''
        button.setEnabled(True)
        button.setText('Auto Detect')

    def open_dialog(self):
        '''Updates the Line Edit fields with currently stored values and executes the dialog.'''
        self.dialog.serverInput.setText(self.config.host)
        self.dialog.userInput.setText(self.config.user_id)
        self.dialog.dataInput.setText(self.config.data_directory)
        self.dialog.launcherInput.setText(self.config.launcher)

        self.auto_detect_button_reset(self.dialog.dataDetectButton)
        self.auto_detect_button_reset(self.dialog.launcherDetectButton)

        self.exec_()



if __name__ == "__main__":
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    app = QApplication(sys.argv)

    window = MainWindow()

    if window.settings.config.start():
        window.ui.settingsButton.click()

    window.show()

    sys.exit(app.exec_())
