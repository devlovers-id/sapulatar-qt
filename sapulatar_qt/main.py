# This Python file uses the following encoding: utf-8
import argparse
import sys
import os
import glob

from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QFileDialog, QDialog
from PySide2.QtCore import QFile, QThread, Signal
from PySide2.QtUiTools import QUiLoader

from sapulatar_qt import __version__
from sapulatar_qt.ui.main_window import Ui_MainWindow
from sapulatar_qt.ui.progress_dialog import Ui_progressbarDialog

## =====================
## Initializing
## check python version at least 3.8 with pip 21
## check dependencies: rembg, PIL, if not found run warning dialog

app_errors = None

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
        super(TheMainThread, self).__init__(parent=parent)
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

class SapulatarProgressDialog(Ui_progressbarDialog, QDialog):

    def __init__(self, parent=None, *args, **kwargs):
        super(SapulatarProgressDialog, self).__init__(parent=parent)
        self.setupUi(self)
    
    ## Process callbacks function =========================================================================
    def push_notification(self, exported_file, progression):
        if progression >= self.progressBar.maximum():
            self.close()
            show_message(msg=f"{progression} file(s) exported successfully!")
        else:
            self.currentFile.setText(f"{exported_file} processed!")
            self.progressBar.setValue(progression)

    def set_currentFile(self, inputed_file):
        self.currentFile.setText(f"Processing: {inputed_file}")

class SapulatarQtMain(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None, args=None):
        super(SapulatarQtMain, self).__init__(parent=parent)
        self.setupUi(self)

        self.inputSource_local = 0

        # parse the input argument
        if not args is None:
            inputpath = args.input if args.input != "-" else ""
            if os.path.exists(inputpath):
                if os.path.isdir(inputpath):
                    self.inputSource_local = 1
                    self.batchProcess_local.setChecked(True)
                self.inputFile_local.setText(inputpath)
                self.outputFile_local.setText(os.path.dirname(inputpath))

        self.singleProcess_local.clicked.connect(self.dialogTypeFile)
        self.batchProcess_local.clicked.connect(self.dialogTypefolder)
        self.btnBrowse_local.clicked.connect(self.selectFile)
        self.btnSave_local.clicked.connect(self.selectOutputDir)
        self.btn_processLocal.clicked.connect(self.processLocal)
        
        self.btnBrowse_remote.clicked.connect(self.selectFile_remote)
        self.btnSave_remote.clicked.connect(self.selectOutputdir_remote)
        self.btn_processRemote.clicked.connect(self.processRemote)

    def dialogTypeFile(self):
        if self.singleProcess_local.isChecked:
            print ("Single process selected!")
            self.inputSource_local = 0
            self.inputFile_local.setText("")

    def dialogTypefolder(self):
        if self.batchProcess_local.isChecked:
            print ("Batch process selected!")
            self.inputSource_local = 1
            self.inputFile_local.setText("")

    ## Local Tab Functions ================================================================================
    def selectFile(self):
        if self.inputSource_local == 0:
          opened_file, _ = QFileDialog.getOpenFileName(None, "Open Image", "", "Images (*.jpg *.png *.jpeg *.JPG)")
        else:
          opened_file = QFileDialog.getExistingDirectory(None, "Select Input Directory", "", QFileDialog.DontUseNativeDialog)
        if opened_file:
            self.inputFile_local.setText(opened_file)
            self.outputFile_local.setText(os.path.dirname(opened_file))

    def selectOutputDir(self):
        output_dir = QFileDialog.getExistingDirectory(None, "Select Output Directory", "", QFileDialog.DontUseNativeDialog)
        if output_dir:
            self.outputFile_local.setText(output_dir)

    def processLocal(self):
        ## Get Input Value
        inputFile = self.inputFile_local.text()
        fileName = os.path.basename(os.path.splitext(inputFile)[0])
        outputDir = self.outputFile_local.text()

        # Arg. values
        # alphamatting
        if self.opt_alphaMating.currentText() == "Use alpha matting cutout":
            a_value = True
        else:
            a_value = False

        af_value = self.val_fgThreshold.value()
        ab_value = self.val_bgThreshold.value()
        ae_value = self.val_erodeSize.value()
        az_value = self.val_baseSize.value()

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

        list_of_inputfiles = []
        list_of_outputfiles = []
        
        if self.inputSource_local == 0:
            list_of_inputfiles.append(inputFile)
            list_of_outputfiles.append( outputDir + "/" + fileName + ".png" )
        else:
            for entry in os.scandir(inputFile):
                if entry.is_file():
                    the_file = inputFile + "/" + entry.name
                    if the_file.endswith(('.jpg', '.jpeg', '.png', '.JPG', '.JPEG')):
                        outputFiles = self.outputFile_local.text() + "/" + os.path.basename(os.path.splitext(entry.name)[0]) + ".png"
                        print("Processsing: " + entry.name)
                        list_of_inputfiles.append(the_file)
                        list_of_outputfiles.append(outputFiles)

        # create the main process
        main_process = TheMainThread(list_of_inputfiles, list_of_outputfiles, removebg_args, parent=self)
        progressdialog = SapulatarProgressDialog(parent=self)
        # conecting Signal
        main_process.export_start.connect(progressdialog.set_currentFile)
        main_process.export_finished.connect(progressdialog.push_notification)
        # show progressbar
        progressdialog.progressBar.setMaximum(len(list_of_inputfiles))
        progressdialog.show()
        # starting process
        main_process.start()
    
    ## Remote Tab Functions ================================================================================
    def selectFile_remote(self):
        opened_file, _ = QFileDialog.getOpenFileName(None, "Open Image", "", "Images (*.jpg, *.png)")
        if opened_file:
            self.inputFile_remote.setText(opened_file)

    def selectOutputdir_remote(self):
        output_dir = QFileDialog.getExistingDirectory(None, "Select Output Directory", "", QFileDialog.ShowDirsOnly)
        if output_dir:
            self.outputFile_remote.setText(output_dir)
    
    def processRemote(self):
        # TODO do remote processing
        print ("Remote process button clicked")
        show_message(msg="Yes, this button works fine!")


def main():

    ap = argparse.ArgumentParser()
    ap.add_argument(
            "input",
            nargs="?",
            default="-",
            type=str,
            help="Input 1 file or directory path"
    )

    ap.add_argument(
            "--version",
            action="version",
            version=__version__
    )

    args = ap.parse_args()

    loader = QUiLoader()
    app = QApplication(sys.argv)

    main_window = SapulatarQtMain(None, args)
    main_window.show()

    if app_errors:
        show_message(msg_type=QMessageBox.Critical, msg=app_errors)

    app.exec_()


if __name__ == "__main__":
    main()
