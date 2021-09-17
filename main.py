# This Python file uses the following encoding: utf-8
import sys
import os
import glob

from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QFileDialog
from PySide2.QtCore import QFile, QThread, Signal
from PySide2.QtUiTools import QUiLoader

## =====================
## Initializing
## check python version at least 3.8 with pip 21
## check dependencies: rembg, PIL, if not found run warning dialog

app_errors = None
inputSource_local = 0
list_of_inputfiles = []
list_of_outputfiles = []

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

class TheMainThread(QThread):

    export_finished = Signal(str, int)
    export_start = Signal(str)

    def __init__(self, t_input_files, t_output_files, removebg_args, parent = None ):
        super(TheMainThread, self).__init__(parent)
        self.t_input_files = t_input_files
        self.t_output_files = t_output_files
        self.removebg_args = removebg_args

    def run(self):
        for index,item in enumerate(self.t_input_files):
            self.export_start.emit( self.t_input_files[index])
            f = np.fromfile(item)
            result = removebg(
                f,
                alpha_matting=self.removebg_args['a_value'],
                alpha_matting_foreground_threshold=self.removebg_args['af_value'],
                alpha_matting_background_threshold=self.removebg_args['ab_value'],
                alpha_matting_erode_structure_size=self.removebg_args['ae_value'],
                alpha_matting_base_size=self.removebg_args['az_value'],
                )
            img = Image.open(io.BytesIO(result)).convert("RGBA")
            img.save( self.t_output_files[index])
            self.export_finished.emit( self.t_output_files[index], index + 1 )

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
    outputDir = the_window.outputFile_local.text()

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

    removebg_args = {
        "a_value": a_value,
        "af_value": af_value,
        "ab_value": ab_value,
        "ae_value": ae_value,
        "az_value": az_value
    }

    # If blank
    if inputFile == "":
        show_error(msg="Please select input file/folder first!")
    if outputDir == "":
        show_error(msg="Input file/folder not found!")

    if inputSource_local == 0:
        list_of_inputfiles.append(inputFile)
        list_of_outputfiles.append( outputDir + "/" + fileName + ".png" )
    else:
        for entry in os.scandir(inputFile):
            if entry.is_file():
                the_file = inputFile + "/" + entry.name
                if the_file.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                    outputFiles = the_window.outputFile_local.text() + "/" + os.path.basename(os.path.splitext(entry.name)[0]) + ".png"
                    print("Processsing: " + entry.name)
                    list_of_inputfiles.append(the_file)
                    list_of_outputfiles.append(outputFiles)

    # create the main process
    main_process = TheMainThread(list_of_inputfiles, list_of_outputfiles, removebg_args, parent=the_window)
    # conecting Signal
    main_process.export_start.connect(set_currentFile)
    main_process.export_finished.connect(push_notification)
    # show progressbar
    progressbar.progressBar.setMaximum(len(list_of_inputfiles))
    progressbar.show()
    # starting process
    main_process.start()

def push_notification(exported_file, progression):
    if progression >= progressbar.progressBar.maximum():
        progressbar.close()
        show_message(msg=f"{progression} file(s) exported successfully!")
    else:
        progressbar.currentFile.setText(f"{exported_file} processed!")
        progressbar.progressBar.setValue(progression)

def set_currentFile(inputed_file):
    progressbar.currentFile.setText(f"Processing: {inputed_file}")

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
    show_message(msg="Yes, this button works fine!")



if __name__ == "__main__":
    loader = QUiLoader()
    app = QApplication(sys.argv)
    main_window = loader.load("form.ui", None)
    progressbar = loader.load("dialog.ui", main_window)

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

    app.exec_()
