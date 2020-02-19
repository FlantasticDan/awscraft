# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import resources_rc

class Ui_settingsDialog(object):
    def setupUi(self, settingsDialog):
        if settingsDialog.objectName():
            settingsDialog.setObjectName(u"settingsDialog")
        settingsDialog.setWindowModality(Qt.ApplicationModal)
        settingsDialog.setEnabled(True)
        settingsDialog.resize(320, 510)
        settingsDialog.setContextMenuPolicy(Qt.ActionsContextMenu)
        icon = QIcon()
        icon.addFile(u":/images/settingsIcon.png", QSize(), QIcon.Normal, QIcon.On)
        settingsDialog.setWindowIcon(icon)
        settingsDialog.setStyleSheet(u"QDialog{\n"
"	background-color: white\n"
"}")
        settingsDialog.setModal(True)
        self.serverInput = QLineEdit(settingsDialog)
        self.serverInput.setObjectName(u"serverInput")
        self.serverInput.setGeometry(QRect(10, 80, 301, 31))
        font = QFont()
        font.setFamily(u"Minecraftia")
        font.setPointSize(12)
        self.serverInput.setFont(font)
        self.serverInput.setCursor(QCursor(Qt.IBeamCursor))
        self.serverInput.setAcceptDrops(False)
        self.serverInput.setStyleSheet(u"QLineEdit{\n"
"	background-color: white;\n"
"	border: 2px solid #D9D9D9\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	background-color: white;\n"
"	border: 2px solid black\n"
"}")
        self.serverInput.setAlignment(Qt.AlignCenter)
        self.titleLabel = QLabel(settingsDialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(10, 10, 301, 31))
        font1 = QFont()
        font1.setFamily(u"Minecraftia")
        font1.setPointSize(18)
        self.titleLabel.setFont(font1)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.serverLabel = QLabel(settingsDialog)
        self.serverLabel.setObjectName(u"serverLabel")
        self.serverLabel.setEnabled(True)
        self.serverLabel.setGeometry(QRect(10, 53, 301, 20))
        self.serverLabel.setFont(font)
        self.serverLabel.setStyleSheet(u"QLabel:disabled{\n"
"	color: #ED0008;\n"
"}")
        self.userLabel = QLabel(settingsDialog)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setEnabled(True)
        self.userLabel.setGeometry(QRect(10, 133, 301, 20))
        self.userLabel.setFont(font)
        self.userLabel.setStyleSheet(u"QLabel:disabled{\n"
"	color: #ED0008;\n"
"}")
        self.userInput = QLineEdit(settingsDialog)
        self.userInput.setObjectName(u"userInput")
        self.userInput.setGeometry(QRect(10, 160, 301, 31))
        self.userInput.setFont(font)
        self.userInput.setCursor(QCursor(Qt.IBeamCursor))
        self.userInput.setAcceptDrops(False)
        self.userInput.setStyleSheet(u"QLineEdit{\n"
"	background-color: white;\n"
"	border: 2px solid #D9D9D9\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	background-color: white;\n"
"	border: 2px solid black\n"
"}")
        self.userInput.setAlignment(Qt.AlignCenter)
        self.dataLabel = QLabel(settingsDialog)
        self.dataLabel.setObjectName(u"dataLabel")
        self.dataLabel.setGeometry(QRect(10, 210, 301, 20))
        self.dataLabel.setFont(font)
        self.dataLabel.setStyleSheet(u"QLabel:disabled{\n"
"	color: #ED0008;\n"
"}")
        self.dataInput = QLineEdit(settingsDialog)
        self.dataInput.setObjectName(u"dataInput")
        self.dataInput.setEnabled(True)
        self.dataInput.setGeometry(QRect(10, 280, 301, 31))
        self.dataInput.setFont(font)
        self.dataInput.setCursor(QCursor(Qt.IBeamCursor))
        self.dataInput.setAcceptDrops(False)
        self.dataInput.setStyleSheet(u"QLineEdit{\n"
"	background-color: white;\n"
"	border: 2px solid #D9D9D9\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	background-color: white;\n"
"	border: 2px solid black\n"
"}")
        self.dataInput.setAlignment(Qt.AlignCenter)
        self.dataInput.setReadOnly(True)
        self.dataDetectButton = QPushButton(settingsDialog)
        self.dataDetectButton.setObjectName(u"dataDetectButton")
        self.dataDetectButton.setEnabled(True)
        self.dataDetectButton.setGeometry(QRect(10, 240, 146, 31))
        font2 = QFont()
        font2.setFamily(u"Minecraftia")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.dataDetectButton.setFont(font2)
        self.dataDetectButton.setStyleSheet(u"QPushButton{\n"
"	background: #2FC15D;\n"
"	border: 5px solid #2FC15D;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #2C5E2E;\n"
"	border: 5px solid #2C5E2E;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background: #2FC15D;\n"
"	border: 5px solid #2FC15D;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background: white;\n"
"	border: 5px solid #2FC15D;\n"
"	border-radius: 0px;\n"
"	color: #2FC15D;\n"
"}")
        self.dataDetectButton.setFlat(False)
        self.dataBrowseButton = QPushButton(settingsDialog)
        self.dataBrowseButton.setObjectName(u"dataBrowseButton")
        self.dataBrowseButton.setEnabled(False)
        self.dataBrowseButton.setGeometry(QRect(165, 240, 146, 31))
        self.dataBrowseButton.setFont(font2)
        self.dataBrowseButton.setStyleSheet(u"QPushButton{\n"
"	background: #00C9ED;\n"
"	border: 5px solid #00C9ED;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #0C273D;\n"
"	border: 5px solid #0C273D;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background: #00C9ED;\n"
"	border: 5px solid #00C9ED;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background: white;\n"
"	border: 5px solid #D9D9D9;\n"
"	border-radius: 0px;\n"
"	color: #D9D9D9;\n"
"}")
        self.dataBrowseButton.setFlat(False)
        self.launcherBrowseButton = QPushButton(settingsDialog)
        self.launcherBrowseButton.setObjectName(u"launcherBrowseButton")
        self.launcherBrowseButton.setEnabled(False)
        self.launcherBrowseButton.setGeometry(QRect(165, 360, 146, 31))
        self.launcherBrowseButton.setFont(font2)
        self.launcherBrowseButton.setStyleSheet(u"QPushButton{\n"
"	background: #00C9ED;\n"
"	border: 5px solid #00C9ED;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #0C273D;\n"
"	border: 5px solid #0C273D;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background: #00C9ED;\n"
"	border: 5px solid #00C9ED;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background: white;\n"
"	border: 5px solid #D9D9D9;\n"
"	border-radius: 0px;\n"
"	color: #D9D9D9;\n"
"}")
        self.launcherBrowseButton.setFlat(False)
        self.launcherDetectButton = QPushButton(settingsDialog)
        self.launcherDetectButton.setObjectName(u"launcherDetectButton")
        self.launcherDetectButton.setEnabled(True)
        self.launcherDetectButton.setGeometry(QRect(10, 360, 146, 31))
        self.launcherDetectButton.setFont(font2)
        self.launcherDetectButton.setStyleSheet(u"QPushButton{\n"
"	background: #2FC15D;\n"
"	border: 5px solid #2FC15D;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #2C5E2E;\n"
"	border: 5px solid #2C5E2E;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background: #2FC15D;\n"
"	border: 5px solid #2FC15D;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background: white;\n"
"	border: 5px solid #2FC15D;\n"
"	border-radius: 0px;\n"
"	color: #2FC15D;\n"
"}")
        self.launcherDetectButton.setFlat(False)
        self.launcherLabel = QLabel(settingsDialog)
        self.launcherLabel.setObjectName(u"launcherLabel")
        self.launcherLabel.setGeometry(QRect(10, 330, 301, 20))
        self.launcherLabel.setFont(font)
        self.launcherLabel.setStyleSheet(u"QLabel:disabled{\n"
"	color: #ED0008;\n"
"}")
        self.launcherInput = QLineEdit(settingsDialog)
        self.launcherInput.setObjectName(u"launcherInput")
        self.launcherInput.setEnabled(True)
        self.launcherInput.setGeometry(QRect(10, 400, 301, 31))
        self.launcherInput.setFont(font)
        self.launcherInput.setCursor(QCursor(Qt.IBeamCursor))
        self.launcherInput.setAcceptDrops(False)
        self.launcherInput.setStyleSheet(u"QLineEdit{\n"
"	background-color: white;\n"
"	border: 2px solid #D9D9D9\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	background-color: white;\n"
"	border: 2px solid black\n"
"}")
        self.launcherInput.setAlignment(Qt.AlignCenter)
        self.launcherInput.setReadOnly(True)
        self.saveButton = QPushButton(settingsDialog)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(True)
        self.saveButton.setGeometry(QRect(10, 450, 301, 50))
        font3 = QFont()
        font3.setFamily(u"Minecraftia")
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setWeight(75)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.saveButton.setFont(font3)
        self.saveButton.setStyleSheet(u"QPushButton{\n"
"	background: #2FC15D;\n"
"	border: 5px solid #2FC15D;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #2C5E2E;\n"
"	border: 5px solid #2C5E2E;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background: #2FC15D;\n"
"	border: 5px solid #2FC15D;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background: white;\n"
"	border: 5px solid #2FC15D;\n"
"	border-radius: 0px;\n"
"	color: #2FC15D;\n"
"}")
        self.saveButton.setFlat(False)
        QWidget.setTabOrder(self.serverInput, self.userInput)
        QWidget.setTabOrder(self.userInput, self.dataDetectButton)
        QWidget.setTabOrder(self.dataDetectButton, self.dataBrowseButton)
        QWidget.setTabOrder(self.dataBrowseButton, self.launcherDetectButton)
        QWidget.setTabOrder(self.launcherDetectButton, self.launcherBrowseButton)
        QWidget.setTabOrder(self.launcherBrowseButton, self.launcherInput)
        QWidget.setTabOrder(self.launcherInput, self.dataInput)

        self.retranslateUi(settingsDialog)

        self.dataDetectButton.setDefault(True)
        self.dataBrowseButton.setDefault(True)
        self.launcherBrowseButton.setDefault(True)
        self.launcherDetectButton.setDefault(True)
        self.saveButton.setDefault(True)


        QMetaObject.connectSlotsByName(settingsDialog)
    # setupUi

    def retranslateUi(self, settingsDialog):
        settingsDialog.setWindowTitle(QCoreApplication.translate("settingsDialog", u"AWScraft Configuration", None))
        self.titleLabel.setText(QCoreApplication.translate("settingsDialog", u"Configuration", None))
#if QT_CONFIG(tooltip)
        self.serverLabel.setToolTip(QCoreApplication.translate("settingsDialog", u"URL or IP Address the AWScraft instance is controlled by.\n"
"This is not the address you would enter to connect directly within Minecraft.", None))
#endif // QT_CONFIG(tooltip)
        self.serverLabel.setText(QCoreApplication.translate("settingsDialog", u"Server Host Address", None))
#if QT_CONFIG(tooltip)
        self.userLabel.setToolTip(QCoreApplication.translate("settingsDialog", u"Unique ID issued to you by your server administrator.\n"
"It is not necessarily your Minecraft username.", None))
#endif // QT_CONFIG(tooltip)
        self.userLabel.setText(QCoreApplication.translate("settingsDialog", u"User ID", None))
#if QT_CONFIG(tooltip)
        self.dataLabel.setToolTip(QCoreApplication.translate("settingsDialog", u"The '.minecraft' directory, typically found in a User's AppData folder.", None))
#endif // QT_CONFIG(tooltip)
        self.dataLabel.setText(QCoreApplication.translate("settingsDialog", u"Minecraft Data Directory", None))
        self.dataDetectButton.setText(QCoreApplication.translate("settingsDialog", u"Auto Detect", None))
        self.dataBrowseButton.setText(QCoreApplication.translate("settingsDialog", u"Browse", None))
        self.launcherBrowseButton.setText(QCoreApplication.translate("settingsDialog", u"Browse", None))
        self.launcherDetectButton.setText(QCoreApplication.translate("settingsDialog", u"Auto Detect", None))
#if QT_CONFIG(tooltip)
        self.launcherLabel.setToolTip(QCoreApplication.translate("settingsDialog", u"The '.minecraft' directory, typically found in a User's AppData folder.", None))
#endif // QT_CONFIG(tooltip)
        self.launcherLabel.setText(QCoreApplication.translate("settingsDialog", u"Minecraft Launcher", None))
        self.saveButton.setText(QCoreApplication.translate("settingsDialog", u"Save", None))
    # retranslateUi

