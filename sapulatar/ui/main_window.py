# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(500, 700))
        MainWindow.setMaximumSize(QSize(500, 700))
        icon = QIcon()
        icon.addFile(os.path.join(os.path.dirname(__file__), "assets/logo.png"), QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.bgcleaner = QWidget(MainWindow)
        self.bgcleaner.setObjectName(u"bgcleaner")
        self.bgcleaner.setMinimumSize(QSize(500, 700))
        self.bgcleaner.setMaximumSize(QSize(500, 700))
        self.textBrowser = QTextBrowser(self.bgcleaner)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(140, 20, 341, 111))
        self.textBrowser.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setTabStopWidth(80)
        self.textBrowser.setOpenExternalLinks(True)
        self.mainTab = QTabWidget(self.bgcleaner)
        self.mainTab.setObjectName(u"mainTab")
        self.mainTab.setGeometry(QRect(0, 140, 501, 541))
        self.mainTab.setMinimumSize(QSize(0, 0))
        self.mainTab.setStyleSheet(u"")
        self.mainTab.setTabPosition(QTabWidget.West)
        self.mainTab.setTabShape(QTabWidget.Rounded)
        self.mainTab.setIconSize(QSize(32, 32))
        self.mainTab.setElideMode(Qt.ElideNone)
        self.mainTab.setUsesScrollButtons(True)
        self.mainTab.setDocumentMode(False)
        self.mainTab.setTabsClosable(False)
        self.mainTab.setMovable(False)
        self.tabLocal = QWidget()
        self.tabLocal.setObjectName(u"tabLocal")
        self.groupBox = QGroupBox(self.tabLocal)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 451, 201))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(11, 70, 411, 17))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 130, 411, 17))
        self.btnSave_local = QToolButton(self.groupBox)
        self.btnSave_local.setObjectName(u"btnSave_local")
        self.btnSave_local.setGeometry(QRect(350, 150, 81, 31))
        self.btnBrowse_local = QToolButton(self.groupBox)
        self.btnBrowse_local.setObjectName(u"btnBrowse_local")
        self.btnBrowse_local.setGeometry(QRect(352, 90, 81, 31))
        self.inputFile_local = QLineEdit(self.groupBox)
        self.inputFile_local.setObjectName(u"inputFile_local")
        self.inputFile_local.setGeometry(QRect(10, 90, 331, 31))
        self.outputFile_local = QLineEdit(self.groupBox)
        self.outputFile_local.setObjectName(u"outputFile_local")
        self.outputFile_local.setGeometry(QRect(10, 150, 331, 31))
        self.singleProcess_local = QRadioButton(self.groupBox)
        self.singleProcess_local.setObjectName(u"singleProcess_local")
        self.singleProcess_local.setEnabled(True)
        self.singleProcess_local.setGeometry(QRect(10, 40, 141, 23))
        self.singleProcess_local.setCheckable(True)
        self.singleProcess_local.setChecked(True)
        self.batchProcess_local = QRadioButton(self.groupBox)
        self.batchProcess_local.setObjectName(u"batchProcess_local")
        self.batchProcess_local.setGeometry(QRect(170, 40, 231, 23))
        self.groupBox_3 = QGroupBox(self.tabLocal)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 220, 451, 241))
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        self.groupBox_3.setFont(font)
        self.opt_alphaMating = QComboBox(self.groupBox_3)
        self.opt_alphaMating.addItem("")
        self.opt_alphaMating.addItem("")
        self.opt_alphaMating.setObjectName(u"opt_alphaMating")
        self.opt_alphaMating.setGeometry(QRect(10, 30, 421, 31))
        self.val_fgThreshold = QSpinBox(self.groupBox_3)
        self.val_fgThreshold.setObjectName(u"val_fgThreshold")
        self.val_fgThreshold.setGeometry(QRect(300, 70, 131, 31))
        self.val_fgThreshold.setMinimum(-100)
        self.val_fgThreshold.setMaximum(10000)
        self.val_fgThreshold.setValue(240)
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 70, 281, 31))
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 110, 271, 31))
        self.val_bgThreshold = QSpinBox(self.groupBox_3)
        self.val_bgThreshold.setObjectName(u"val_bgThreshold")
        self.val_bgThreshold.setGeometry(QRect(300, 110, 131, 31))
        self.val_bgThreshold.setMinimum(-100)
        self.val_bgThreshold.setMaximum(10000)
        self.val_bgThreshold.setValue(10)
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 150, 271, 31))
        self.val_erodeSize = QSpinBox(self.groupBox_3)
        self.val_erodeSize.setObjectName(u"val_erodeSize")
        self.val_erodeSize.setGeometry(QRect(300, 150, 131, 31))
        self.val_erodeSize.setMinimum(-100)
        self.val_erodeSize.setMaximum(10000)
        self.val_erodeSize.setSingleStep(0)
        self.val_erodeSize.setValue(10)
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 190, 271, 31))
        self.val_baseSize = QSpinBox(self.groupBox_3)
        self.val_baseSize.setObjectName(u"val_baseSize")
        self.val_baseSize.setGeometry(QRect(300, 190, 131, 31))
        self.val_baseSize.setMinimum(-100)
        self.val_baseSize.setMaximum(10000)
        self.val_baseSize.setValue(1000)
        self.btn_processLocal = QPushButton(self.tabLocal)
        self.btn_processLocal.setObjectName(u"btn_processLocal")
        self.btn_processLocal.setGeometry(QRect(320, 480, 121, 41))
        self.mainTab.addTab(self.tabLocal, "")
        self.tabRemote = QWidget()
        self.tabRemote.setObjectName(u"tabRemote")
        self.groupBox_2 = QGroupBox(self.tabRemote)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 451, 91))
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(11, 31, 251, 17))
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(320, 30, 121, 17))
        self.input_serverPort = QLineEdit(self.groupBox_2)
        self.input_serverPort.setObjectName(u"input_serverPort")
        self.input_serverPort.setGeometry(QRect(320, 50, 121, 31))
        self.input_serverUrl = QLineEdit(self.groupBox_2)
        self.input_serverUrl.setObjectName(u"input_serverUrl")
        self.input_serverUrl.setGeometry(QRect(10, 50, 291, 31))
        self.groupBox_4 = QGroupBox(self.tabRemote)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 110, 451, 151))
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(11, 30, 411, 17))
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 90, 411, 17))
        self.btnSave_remote = QToolButton(self.groupBox_4)
        self.btnSave_remote.setObjectName(u"btnSave_remote")
        self.btnSave_remote.setGeometry(QRect(360, 110, 81, 31))
        self.btnBrowse_remote = QToolButton(self.groupBox_4)
        self.btnBrowse_remote.setObjectName(u"btnBrowse_remote")
        self.btnBrowse_remote.setGeometry(QRect(362, 50, 81, 31))
        self.inputFile_remote = QLineEdit(self.groupBox_4)
        self.inputFile_remote.setObjectName(u"inputFile_remote")
        self.inputFile_remote.setGeometry(QRect(10, 50, 341, 31))
        self.outputFile_remote = QLineEdit(self.groupBox_4)
        self.outputFile_remote.setObjectName(u"outputFile_remote")
        self.outputFile_remote.setGeometry(QRect(10, 110, 341, 31))
        self.btn_processRemote = QPushButton(self.tabRemote)
        self.btn_processRemote.setObjectName(u"btn_processRemote")
        self.btn_processRemote.setGeometry(QRect(320, 480, 121, 41))
        self.mainTab.addTab(self.tabRemote, "")
        self.tabAbout = QWidget()
        self.tabAbout.setObjectName(u"tabAbout")
        self.textBrowser_2 = QTextBrowser(self.tabAbout)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(20, 10, 421, 501))
        self.textBrowser_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.textBrowser_2.setOverwriteMode(False)
        self.textBrowser_2.setTabStopWidth(80)
        self.textBrowser_2.setOpenExternalLinks(True)
        self.mainTab.addTab(self.tabAbout, "")
        self.label_10 = QLabel(self.bgcleaner)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 131, 111))
        self.label_10.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), "assets/logo.png")))
        self.label_10.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.bgcleaner)

        self.retranslateUi(MainWindow)

        self.mainTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sapulatar-qt by DevloversID", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Sapulatar-qt by Devlovers ID</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A simple gui apps to help you remove background from various images. This tool need rembg module to done its job. Please install it first if the module not exist yet in your system.</p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Files/Folder", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Files/Folder", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Directory to save results", None))
        self.btnSave_local.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.btnBrowse_local.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.inputFile_local.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select file/folder", None))
        self.outputFile_local.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a directory to save the result", None))
        self.singleProcess_local.setText(QCoreApplication.translate("MainWindow", u"Process Single File", None))
        self.batchProcess_local.setText(QCoreApplication.translate("MainWindow", u"Process Multiple Files in a Directory", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"  Extra Parameter", None))
        self.opt_alphaMating.setItemText(0, QCoreApplication.translate("MainWindow", u"Don't use alpha matting cutout", None))
        self.opt_alphaMating.setItemText(1, QCoreApplication.translate("MainWindow", u"Use alpha matting cutout", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Alpha matting foreground threshold (def. 240)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Alpha matting background threshold (def. 10)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Alpha matting erode size (def. 10)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Alpha matting base size (def. 1000)", None))
        self.btn_processLocal.setText(QCoreApplication.translate("MainWindow", u"Process Now!", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tabLocal), QCoreApplication.translate("MainWindow", u"Local Process", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Server Settings", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Server Url (i.e http://192.168.1.10)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Port (i.e 5000)", None))
        self.input_serverPort.setPlaceholderText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.input_serverUrl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"http://192.168.1.10", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Files/Folder", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Select Files/Folder", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Directory to save results", None))
        self.btnSave_remote.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.btnBrowse_remote.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.inputFile_remote.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.outputFile_remote.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a directory to save the result", None))
        self.btn_processRemote.setText(QCoreApplication.translate("MainWindow", u"Process Now!", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tabRemote), QCoreApplication.translate("MainWindow", u"Remote Process (WIP)", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'DejaVu Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sapulatar-qt v1.0.0-alpha </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">made with \u2764\ufe0f with Qt Creator by Devlovers ID.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Links:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; m"
                        "argin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Sapulatar-qt Repo (<a href=\"https://github.com/devlovers-id/bgcleaner-qt\"><span style=\" text-decoration: underline; color:#1c7eff;\">https://github.com/devlovers-id/bgcleaner-qt</span></a>)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Rembg by <span style=\" font-weight:600;\">Danielgatis</span> (<a href=\"https://github.com/danielgatis/rembg\"><span style=\" text-decoration: underline; color:#1c7eff;\">https://github.com/danielgatis/rembg</span></a>)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Version: </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\">Qt Creator 4.12.2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Based on Qt 5.14.2</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Devlovers ID Team: </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Rania Amina </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Sofyan Sugianto </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Nugroho Dwi H. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin"
                        "-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Donate to This Project:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://support.dev-is.my.id/\"><span style=\" font-weight:600; text-decoration: underline; color:#007af4;\">https://support.dev-is.my.id/</span></a></p></body></html>", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tabAbout), QCoreApplication.translate("MainWindow", u"About", None))
        self.label_10.setText("")
    # retranslateUi

