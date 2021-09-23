# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_progressbarDialog(object):
    def setupUi(self, progressbarDialog):
        if not progressbarDialog.objectName():
            progressbarDialog.setObjectName(u"progressbarDialog")
        progressbarDialog.setWindowModality(Qt.WindowModal)
        progressbarDialog.resize(400, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(progressbarDialog.sizePolicy().hasHeightForWidth())
        progressbarDialog.setSizePolicy(sizePolicy)
        progressbarDialog.setMinimumSize(QSize(400, 150))
        progressbarDialog.setMaximumSize(QSize(400, 150))
        icon = QIcon()
        icon.addFile(os.path.join(os.path.dirname(__file__), "assets/logo.png"), QSize(), QIcon.Normal, QIcon.Off)
        progressbarDialog.setWindowIcon(icon)
        progressbarDialog.setModal(True)
        self.progressBar = QProgressBar(progressbarDialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 50, 371, 31))
        self.progressBar.setValue(0)
        self.currentFile = QLabel(progressbarDialog)
        self.currentFile.setObjectName(u"currentFile")
        self.currentFile.setGeometry(QRect(14, 91, 361, 20))

        self.retranslateUi(progressbarDialog)

        QMetaObject.connectSlotsByName(progressbarDialog)
    # setupUi

    def retranslateUi(self, progressbarDialog):
        progressbarDialog.setWindowTitle(QCoreApplication.translate("progressbarDialog", u"Sapulatar: Processing File(s)", None))
        self.currentFile.setText("")
    # retranslateUi

