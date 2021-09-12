# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

if __name__ == "__main__":
    loader = QUiLoader()
    app = QApplication(sys.argv)
    main_window = loader.load("form.ui", None)
    main_window.show()
    app.exec_()


## =====================
## Initializing
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
