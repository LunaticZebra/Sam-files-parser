import threading

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit, QListWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, \
    QMenuBar, QStatusBar, QListWidgetItem
from GtfReader import GtfReader

class UiMainWindow(QMainWindow):

    def __init__(self):
        super(UiMainWindow, self).__init__()
        self.gene_id_selected = ""

    def setup_ui(self):
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
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gene_list = QListWidget(self.centralwidget)
        self.gene_list.setObjectName("gene_list")
        self.verticalLayout_2.addWidget(self.gene_list)
        self.gtf_load_btn = QPushButton(self.centralwidget)
        self.gtf_load_btn.setMaximumSize(QtCore.QSize(64, 16777215))
        self.gtf_load_btn.setObjectName("gtf_load_btn")
        self.verticalLayout_2.addWidget(self.gtf_load_btn)
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
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
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
        self.setWindowTitle(_translate("MainWindow", "MyApp"))
        self.label_2.setText(_translate("MainWindow", ".gtf file path: "))
        self.gtf_browse_btn.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "Gene ID :"))
        self.gtf_load_btn.setText(_translate("MainWindow", "Load"))
        self.src_label.setText(_translate("MainWindow", "Source:"))
        self.sam_src_btn.setText(_translate("MainWindow", "Browse"))
        self.dest_label.setText(_translate("MainWindow", "Destination:"))
        self.sam_dest_btn.setText(_translate("MainWindow", "Browse"))
        self.pushButton_6.setText(_translate("MainWindow", "Proceed"))


    def add_gtf_reader(self, gtf_reader : GtfReader):
        self.gtf_reader = gtf_reader

    def __set_widgets_functions(self):
        self.gtf_browse_btn.clicked.connect(self.__browse_gtf)
        self.sam_src_btn.clicked.connect(self.__browse_sam_src)
        self.sam_dest_btn.clicked.connect(self.__browse_sam_dest)
        self.gtf_load_btn.clicked.connect(self.__load_gene_id)
        self.gene_list.itemActivated.connect(self.__gene_selected_event)

    def __browse_gtf(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, "Choose .gtf file", "C:/Users/user/Desktop", ".gtf files (*.gtf)")
        if fname[0] != "":
            self.gtf_filepath.setText(fname[0])
            self.gtf_filename = str(self.gtf_filepath.text())
            self.gtf_reader.set_filepath(fname[0])
            self.gene_dictionary = self.gtf_reader.create_dict()
            self.__update_gene_list(self.gene_dictionary.keys())

    def __update_gene_list(self, gene_ids):
        for gene_id in gene_ids:
            self.update_list(gene_id)

    def __browse_sam_src(self):
        fname = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose .sam file", "C:/Users/user/Desktop")
        self.sam_src_filepath.setText(fname[0])

    def __load_gene_id(self):
        print("Clicked")
        if self.gene_id_selected != "":
            self.gene_selected = self.gene_dictionary[self.gene_id_selected]
            print(self.gene_selected)
        #dodaj pokazywanie sie obecnie zaladowanego genu
        #dodaj popup ze nie wybrano gene_id

    def __gene_selected_event(self, item):
        self.gene_id_selected = item.text()
        print(item.text())

    def __browse_sam_dest(self):
        fname = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose destination directory", "C:/Users/user/Desktop")
        self.sam_dest_filepath.setText(fname)
        print(self.sam_dest_filepath.text())

    def update_list(self, item):
        self.gene_list.addItem(str(item))



