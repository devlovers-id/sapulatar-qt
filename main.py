# This Python file uses the following encoding: utf-8
import sys
import os
import glob


from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QFileDialog
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

## =====================
## Initializing
## check python version at least 3.8 with pip 21
## check dependencies: rembg, PIL, if not found run warning dialog

app_errors = None
inputSource_local = 0

try:
    from rembg.bg import remove as removebg
    import numpy as np
    from PIL import Image, ImageFile
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    import io
    print ("rembg module found!")
except ImportError as e:
    print(e)
    app_errors = "Ups! rembg module not found! \n\nPlease install it first by running \n\"pip install rembg\" (or equivalent command) \n\nSapu Latar will exit now!"

## General functions ================================================================================

def show_message(msg_type=QMessageBox.Information, msg="Info", scrollable=False):
    box = QMessageBox(msg_type, "Notification", msg)
    box.exec_()

def show_error(msg_type=QMessageBox.Warning, msg="Error!", scrollable=False):
    box = QMessageBox(msg_type, "Notification", msg)
    box.exec_()

## Local Tab Functions ================================================================================
## select file

def dialogType_file():
    global inputSource_local
    if main_window.singleProcess_local.isChecked:
        print ("Single process selected!")
        inputSource_local = 0
        main_window.inputFile_local.setText("")

def dialogType_folder():
    global inputSource_local
    if main_window.batchProcess_local.isChecked:
        print ("Batch process selected!")
        inputSource_local = 1
        main_window.inputFile_local.setText("")

def selectFile(input_textfield):
    if inputSource_local == 0:
      opened_file, _ = QFileDialog.getOpenFileName(None, "Open Image", "", "Images (*.jpg *.png *.jpeg *.JPG)")
    else:
      opened_file = QFileDialog.getExistingDirectory(None, "Select Input Directory", "", QFileDialog.DontUseNativeDialog)
    if opened_file:
        input_textfield.setText(opened_file)
        main_window.outputFile_local.setText(os.path.dirname(opened_file))
## select output directory
def selectOutputdir(input_textfield):
    output_dir = QFileDialog.getExistingDirectory(None, "Select Output Directory", "", QFileDialog.DontUseNativeDialog)
    if output_dir:
        input_textfield.setText(output_dir)

def processLocal(the_window):
    ## Get Input Value
    inputFile = the_window.inputFile_local.text()
    fileName = os.path.basename(os.path.splitext(inputFile)[0])
    outputDir = the_window.outputFile_local.text() + "/" + fileName + ".png"

    # Arg. values
    # alphamatting
    if the_window.opt_alphaMating.currentText() == "Use alpha matting cutout":
        a_value = True
    else:
        a_value = False

    af_value = the_window.val_fgThreshold.value()
    ab_value = the_window.val_bgThreshold.value()
    ae_value = the_window.val_erodeSize.value()
    az_value = the_window.val_baseSize.value()    

    # If blank
    if inputFile == "":
        show_error(msg="Please select input file/folder first!")
    if outputDir == "":
        show_error(msg="Input file/folder not found!")

    if inputSource_local == 0:
        f = np.fromfile(inputFile)
        print(a_value)
        result = removebg(
            f, 
            alpha_matting=a_value, 
            alpha_matting_foreground_threshold=af_value, 
            alpha_matting_background_threshold=ab_value, 
            alpha_matting_erode_structure_size=ae_value, 
            alpha_matting_base_size=az_value,
            )
        img = Image.open(io.BytesIO(result)).convert("RGBA")
        img.save(outputDir)
        show_message(msg="Process Complete for " + fileName + "!")
    else:
        for entry in os.scandir(inputFile):
            if entry.is_file():
                files = inputFile + "/" + entry.name
                outputFiles = the_window.outputFile_local.text() + "/" + os.path.basename(entry.name) + ".png"
                print("Processsing: " + entry.name)
                f = np.fromfile(files)
                result = removebg(f)
                img = Image.open(io.BytesIO(result)).convert("RGBA")
                img.save(outputFiles)
        show_message(msg="Process Complete! for " + fileName + "!")

## Remote Tab Functions ================================================================================
## select file (remote)
def selectFile_remote(input_textfield):
    opened_file, _ = QFileDialog.getOpenFileName(None, "Open Image", "", "Images (*.jpg, *.png)")
    if opened_file:
        input_textfield.setText(opened_file)

## select directory (remote)
def selectOutputdir_remote(input_textfield):
    output_dir = QFileDialog.getExistingDirectory(None, "Select Output Directory", "", QFileDialog.ShowDirsOnly)
    if output_dir:
        input_textfield.setText(output_dir)

def processRemote():
    print ("Remote process button clicked")
    show_message(msg="Remote process Complete!")



if __name__ == "__main__":
    loader = QUiLoader()
    app = QApplication(sys.argv)
    main_window = loader.load("form.ui", None)

    main_window.singleProcess_local.clicked.connect(dialogType_file)
    main_window.batchProcess_local.clicked.connect(dialogType_folder)
    main_window.btnBrowse_local.clicked.connect(lambda: selectFile(main_window.inputFile_local))
    main_window.btnSave_local.clicked.connect(lambda: selectOutputdir(main_window.outputFile_local))
    main_window.btn_processLocal.clicked.connect(lambda: processLocal(main_window))

    
    main_window.btnBrowse_remote.clicked.connect(lambda: selectFile_remote(main_window.inputFile_remote))
    main_window.btnSave_remote.clicked.connect(lambda: selectOutputdir_remote(main_window.outputFile_remote))
    main_window.btn_processRemote.clicked.connect(processRemote)

    main_window.show()

    if app_errors:
        show_message(msg_type=QMessageBox.Critical, msg=app_errors)
        exit(1)

    app.exec_()





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
