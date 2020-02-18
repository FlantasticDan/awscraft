# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'launcher.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 500)
        MainWindow.setMinimumSize(QSize(900, 500))
        MainWindow.setMaximumSize(QSize(900, 500))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: white\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logoLabel = QLabel(self.centralwidget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setGeometry(QRect(180, 120, 550, 90))
        self.logoLabel.setPixmap(QPixmap(u":/images/awscraftTitle.png"))
        self.logoLabel.setScaledContents(False)
        self.logoLabel.setAlignment(Qt.AlignCenter)
        self.connectButton = QPushButton(self.centralwidget)
        self.connectButton.setObjectName(u"connectButton")
        self.connectButton.setEnabled(True)
        self.connectButton.setGeometry(QRect(180, 250, 550, 50))
        font1 = QFont()
        font1.setFamily(u"Minecraftia")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.connectButton.setFont(font1)
        self.connectButton.setStyleSheet(u"QPushButton{\n"
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
        self.connectButton.setFlat(False)
        self.launchButton = QPushButton(self.centralwidget)
        self.launchButton.setObjectName(u"launchButton")
        self.launchButton.setEnabled(False)
        self.launchButton.setGeometry(QRect(180, 320, 550, 50))
        self.launchButton.setFont(font1)
        self.launchButton.setStyleSheet(u"QPushButton{\n"
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
        self.launchButton.setFlat(False)
        self.settingsButton = QPushButton(self.centralwidget)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setEnabled(True)
        self.settingsButton.setGeometry(QRect(10, 10, 50, 50))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.settingsButton.setFont(font2)
        self.settingsButton.setStyleSheet(u"QPushButton{\n"
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
        icon = QIcon()
        icon.addFile(u":/images/settingsIcon.png", QSize(), QIcon.Normal, QIcon.On)
        self.settingsButton.setIcon(icon)
        self.settingsButton.setIconSize(QSize(40, 40))
        self.settingsButton.setFlat(False)
        self.shutdownButton = QPushButton(self.centralwidget)
        self.shutdownButton.setObjectName(u"shutdownButton")
        self.shutdownButton.setEnabled(True)
        self.shutdownButton.setGeometry(QRect(180, 320, 550, 50))
        self.shutdownButton.setFont(font1)
        self.shutdownButton.setStyleSheet(u"QPushButton{\n"
"	background: #ED0008;\n"
"	border: 5px solid #ED0008;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #822428;\n"
"	border: 5px solid #822428;\n"
"	border-radius: 0px;\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background: #ED0008;\n"
"	border: 5px solid #ED0008;\n"
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
        self.shutdownButton.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.connectButton, self.launchButton)

        self.retranslateUi(MainWindow)

        self.connectButton.setDefault(True)
        self.launchButton.setDefault(False)
        self.settingsButton.setDefault(False)
        self.shutdownButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AWScraft Launcher", None))
        self.logoLabel.setText("")
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Connect to Server", None))
        self.launchButton.setText(QCoreApplication.translate("MainWindow", u"Launch Minecraft", None))
        self.settingsButton.setText("")
        self.shutdownButton.setText(QCoreApplication.translate("MainWindow", u"Shutdown Server", None))
    # retranslateUi

