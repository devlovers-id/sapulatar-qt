# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

def show_message(msg_type=QMessageBox.Information, msg="Info", scrollable=False):
    box = QMessageBox(msg_type, "Notification", msg)
    box.exec_()

def inputFiles_local():
    print ("Local browse button clicked")
    show_message(msg="Browse files")

def outputFiles_local():
    print ("Local save button clicked")
    show_message(msg="Browse directory to save result")

def processLocal():
    print ("Local process button clicked")
    show_message(msg="Process Complete!")

def inputFiles_remote():
    print ("Remote browse button clicked")
    show_message(msg="Browse files (remote)")

def outputFiles_remote():
    print ("Remote save button clicked")
    show_message(msg="Browse directory to save result (remote)")

def processRemote():
    print ("Remote process button clicked")
    show_message(msg="Remote process Complete!")



if __name__ == "__main__":
    loader = QUiLoader()
    app = QApplication(sys.argv)
    main_window = loader.load("form.ui", None)

    main_window.btnBrowse_local.clicked.connect(inputFiles_local)
    main_window.btnSave_local.clicked.connect(outputFiles_local)
    main_window.btn_processLocal.clicked.connect(processLocal)

    main_window.btnBrowse_remote.clicked.connect(inputFiles_remote)
    main_window.btnSave_remote.clicked.connect(outputFiles_remote)
    main_window.btn_processRemote.clicked.connect(processRemote)

    main_window.show()
    app.exec_()



## =====================
## Initializing
## check python version at least 3.8 with pip 21
## check dependencies: rembg, PIL, if not found run warning dialog

## =====================
## For Tab local
## Get input info, file, files, or directory
## Get input info of directory output

## if input is file
## the command is: rembg "input.foo" -o "OUTPUTDIR/output.png" (if parameter active, add paramater after command)

## if input is random files
## the command is loop command (bash equiv): for i in list; do rembg "$i" -o "OUTPUTDIR/${i%.*}.png"; done (if parameter active, add paramater after command)

## if input is directory
## the command is: rembg -p "INPUTDIR" "OUTPUTDIR" (if parameter active, add paramater after command)

## Run warning dialog if:
## - path/file input/output not found or blank
## - output folder or output file name already exist

## =====================
## For Tab Remote
## Get server url and port info
## Get input info, file, files, or directory
## Get input info of directory output

## if input is file
## the command is: wget -c http://192.168.1.55:5000/\?url=file://FULL/PATH/URL/INPUT.jpg -O OUTPUTDIR/OUTPUT.png
## space in url should replace by %

## if input is random files
## the command is loop command (bash equiv): for i in list; do wget -c http://192.168.1.55:5000/\?url=file://FULL/PATH/URL/$i -O "OUTPUTDIR/${i%.*}.png"; done (if parameter active, add paramater after command)
## space in url should replace by %

## Run warning dialog if:
## - path/file input/output not found or blank
## - output folder or output file name already exist
