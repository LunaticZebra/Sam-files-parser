import time

from GtfReader import GtfReader
from SamReader import SamReader
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QObject, pyqtSignal, QThread
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit, QListWidget, QMainWindow, QVBoxLayout, QHBoxLayout, \
    QWidget, QMenuBar, QStatusBar, QMessageBox


class GtfWorker(QObject):
    finished = pyqtSignal()

    def __init__(self, fname, ui):
        super().__init__()
        self.fname = fname
        self.ui = ui

    def run(self):

        if self.fname != "":
            gtf_reader = GtfReader()
            self.ui.gtf_filepath.setText(self.fname)
            self.ui.set_status("loading " + self.fname)
            self.ui.gtf_filename = str(self.ui.gtf_filepath.text())
            gtf_reader.set_filepath(self.fname)
            self.ui.gene_dictionary = gtf_reader.create_dict()
            self.ui.update_gene_list(self.ui.gene_dictionary.keys())
        self.ui.set_status()
        self.finished.emit()


class SamWorker(QObject):
    finished = pyqtSignal()

    def __init__(self, sam_files, ui):
        super().__init__()
        self.sam_files = sam_files
        self.ui = ui
        self.start_time = time.time()

    def run(self):
        sam_reader = SamReader()
        sam_reader.set_genes(self.ui.genes_selected)
        self.ui.proceed_btn.setEnabled(False)
        counter = 1
        for filename in self.sam_files:
            self.ui.set_status(f"working on {filename} ({counter}/{len(self.sam_files)})")

            sam_reader.set_filepath(filename)
           
            sam_reader.read_file()
            filename_addon = ""
            for gene in self.ui.genes_selected:
                filename_addon += gene["gene_id"]
            sam_reader.save_file(self.ui.sam_dest_filepath.text() + "/" +
                                 filename_addon + "_" + filename.split("/")[-1])
            sam_reader.clear()
            counter += 1
        self.ui.proceed_btn.setEnabled(True)
        self.ui.set_status(f"All files loaded ({str(round(time.time() - self.start_time, 2))}s)")
        self.finished.emit()


class UiMainWindow(QMainWindow):

    def __init__(self):
        super(UiMainWindow, self).__init__()
        self.gtf_filename = ""
        self.gene_id_selected = ""
        self.genes_selected = []
        self.gene_dictionary = {}
        self.sam_files = []
        self.__setup_ui()

    def __setup_ui(self):
        self.setObjectName("MainWindow")
        self.resize(773, 589)
        self.setMaximumSize(QtCore.QSize(773, 589))
        self.centralwidget = QWidget(self)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 541))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gtf_filepath = QLineEdit(self.centralwidget)
        self.gtf_filepath.setObjectName("gtf_filepath")
        self.horizontalLayout.addWidget(self.gtf_filepath)
        self.gtf_browse_btn = QPushButton(self.centralwidget)
        self.gtf_browse_btn.setObjectName("gtf_browse_btn")
        self.horizontalLayout.addWidget(self.gtf_browse_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.gene_id_line = QLineEdit(self.centralwidget)
        self.gene_id_line.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.gene_id_line)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gene_list = QListWidget(self.centralwidget)
        self.gene_list.setObjectName("gene_list")
        self.verticalLayout_2.addWidget(self.gene_list)
        self.gene_load_btn = QPushButton(self.centralwidget)
        self.gene_load_btn.setMaximumSize(QtCore.QSize(64, 16777215))
        self.gene_load_btn.setObjectName("gtf_load_btn")
        self.genes_clear_btn = QPushButton(self.centralwidget)
        self.genes_clear_btn.setMaximumSize(QtCore.QSize(64, 16777215))
        self.genes_clear_btn.setObjectName("genes_clear_btn")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.addWidget(self.gene_load_btn)
        self.horizontalLayout_1.addWidget(self.genes_clear_btn)
        self.horizontalLayout_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout_2.addLayout(self.horizontalLayout_1)
        self.current_gene_label = QLabel("No gene currently selected")
        self.loaded_genes = QLabel("Currently loaded genes :")
        self.verticalLayout_2.addWidget(self.current_gene_label)
        self.verticalLayout_2.addWidget(self.loaded_genes)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.src_label = QLabel(self.centralwidget)
        self.src_label.setMinimumSize(QtCore.QSize(80, 30))
        self.src_label.setObjectName("src_label")
        self.horizontalLayout_2.addWidget(self.src_label)
        self.sam_src_filepath = QLineEdit(self.centralwidget)
        self.sam_src_filepath.setObjectName("sam_src_filepath")
        self.horizontalLayout_2.addWidget(self.sam_src_filepath)
        self.sam_src_btn = QPushButton(self.centralwidget)
        self.sam_src_btn.setObjectName("sam_src_btn")
        self.horizontalLayout_2.addWidget(self.sam_src_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dest_label = QLabel(self.centralwidget)
        self.dest_label.setMinimumSize(QtCore.QSize(80, 30))
        self.dest_label.setObjectName("dest_label")
        self.horizontalLayout_3.addWidget(self.dest_label)
        self.sam_dest_filepath = QLineEdit(self.centralwidget)
        self.sam_dest_filepath.setObjectName("sam_dest_filepath")
        self.horizontalLayout_3.addWidget(self.sam_dest_filepath)
        self.sam_dest_btn = QPushButton(self.centralwidget)
        self.sam_dest_btn.setObjectName("sam_dest_btn")
        self.horizontalLayout_3.addWidget(self.sam_dest_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.proceed_btn = QPushButton(self.centralwidget)
        self.proceed_btn.setMaximumSize(QtCore.QSize(120, 16777215))
        self.proceed_btn.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.proceed_btn)
        self.status_label = QLabel("Status:")
        self.verticalLayout.addWidget(self.status_label)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(self)
        self.statusBar.setObjectName("statusBar")
        self.setStatusBar(self.statusBar)
        self.__set_widgets_functions()
        self.__retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def __retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Sam files converter"))
        self.label_2.setText(_translate("MainWindow", ".gtf file path: "))
        self.gtf_browse_btn.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "Gene ID :"))
        self.gene_load_btn.setText(_translate("MainWindow", "Load"))
        self.src_label.setText(_translate("MainWindow", "Source:"))
        self.sam_src_btn.setText(_translate("MainWindow", "Browse"))
        self.dest_label.setText(_translate("MainWindow", "Destination:"))
        self.sam_dest_btn.setText(_translate("MainWindow", "Browse"))
        self.proceed_btn.setText(_translate("MainWindow", "Proceed"))
        self.genes_clear_btn.setText(_translate("MainWindow", "Clear"))

    def __set_widgets_functions(self):
        self.gtf_browse_btn.clicked.connect(self.__browse_gtf)
        self.sam_src_btn.clicked.connect(self.__browse_sam_src)
        self.sam_dest_btn.clicked.connect(self.__browse_sam_dest)
        self.gene_load_btn.clicked.connect(self.__load_gene_id)
        self.gene_list.itemClicked.connect(self.__gene_selected_event)
        self.proceed_btn.clicked.connect(self.__proceed_btn)
        self.gene_id_line.textEdited.connect(self.__update_autocompletion)
        self.genes_clear_btn.clicked.connect(self.__clear_genes_list)

    def __browse_gtf(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, "Choose .gtf file", "C:/Users/user/Desktop",
                                                      ".gtf files (*.gtf)")
        self.gtf_thread = QThread()
        self.gtf_worker = GtfWorker(fname[0], self)
        self.gtf_worker.moveToThread(self.gtf_thread)
        self.gtf_thread.started.connect(self.gtf_worker.run)
        self.gtf_worker.finished.connect(self.gtf_thread.quit)
        self.gtf_worker.finished.connect(self.gtf_worker.deleteLater)
        self.gtf_thread.finished.connect(self.gtf_thread.deleteLater)
        self.gtf_thread.start()

    def __browse_sam_src(self):
        fname = QtWidgets.QFileDialog.getOpenFileNames(self, "Choose folder with .sam files",
                                                       "C:/Users/user/Desktop", ".sam files (*.sam)")
        files = fname[0]
        print(files)
        print(len(files))

        if len(files) != 0:
            text = ""
            for file in files:
                print(file)
                text += file.split("/")[-1] + ";"
            self.sam_src_filepath.setText(text)
            for file in files:
                self.sam_files.append(file)

    def __browse_sam_dest(self):
        fname = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose destination directory",
                                                           "C:/Users/user/Desktop")
        if fname != "":
            self.sam_dest_filepath.setText(fname)

    def __update_autocompletion(self):
        search = self.gene_id_line.text()
        self.update_gene_list(self.gene_dictionary.keys(), search)

    def __proceed_btn(self):
        if self.sam_src_filepath.text() != "" and self.sam_dest_filepath.text() != "" and len(self.genes_selected) > 0:
            self.sam_thread = QThread()
            self.sam_worker = SamWorker(self.sam_files, self)
            self.sam_worker.moveToThread(self.sam_thread)
            self.sam_thread.started.connect(self.sam_worker.run)
            self.sam_worker.finished.connect(self.sam_thread.quit)
            self.sam_worker.finished.connect(self.sam_worker.deleteLater)
            self.sam_thread.finished.connect(self.sam_thread.deleteLater)
            self.sam_thread.start()

    def set_status(self, status=""):
        self.status_label.setText("Status : " + status)

    def update_gene_list(self, gene_id_dict, phrase=""):
        if phrase == "":
            for gene_id in gene_id_dict:
                self.__update_list(gene_id)
        else:
            self.gene_list.clear()
            for gene_id in gene_id_dict:
                if str(gene_id).startswith(phrase):
                    self.__update_list(gene_id)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?',
                                     QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def __update_list(self, item):
        self.gene_list.addItem(str(item))

    def __show_not_loaded(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setText("Gene id wasn't selected. Please select gene id by double-clicking item on a list")
        msg_box.setWindowTitle("Gene id not selected")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def __gene_selected_event(self, item):
        self.gene_id_selected = item.text()
        self.current_gene_label.setText("Selected gene: " +
                                        str(self.gene_dictionary[self.gene_id_selected]).strip("{}"))

    def __load_gene_id(self):
        if self.gene_id_selected != "":
            self.genes_selected.append(self.gene_dictionary[self.gene_id_selected])
            self.loaded_genes.setText(self.loaded_genes.text() + ";" + self.gene_id_selected)
        else:
            self.__show_not_loaded()

    def __clear_genes_list(self):
        self.genes_selected = []
        self.loaded_genes.setText("Currently loaded genes :")
