# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import segno

class Ui_qr_generator(object):
    def setupUi(self, qr_generator):
        qr_generator.setObjectName("qr_generator")
        qr_generator.resize(331, 172)
        qr_generator.setIconSize(QtCore.QSize(24, 24))
        qr_generator.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(qr_generator)
        self.centralwidget.setObjectName("centralwidget")
        icon = QtGui.QIcon("Screenshot 2024-01-12 183253.jpg")
        qr_generator.setWindowIcon(icon)


        self.url = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(10, 10, 311, 31))
        self.url.setObjectName("url")

        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(254, 50, 61, 31))
        self.browse.setObjectName("browse")
        self.browse.clicked.connect(self.browse_folder)  # Connect browse button to the browse_folder method

        self.location = QtWidgets.QTextBrowser(self.centralwidget)
        self.location.setGeometry(QtCore.QRect(10, 50, 231, 31))
        self.location.setObjectName("location")

        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(10, 90, 311, 41))
        self.run.setObjectName("run")
        self.run.clicked.connect(self.run_program)

        qr_generator.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(qr_generator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 21))
        self.menubar.setObjectName("menubar")
        qr_generator.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(qr_generator)
        self.statusbar.setObjectName("statusbar")
        qr_generator.setStatusBar(self.statusbar)

        self.retranslateUi(qr_generator)
        QtCore.QMetaObject.connectSlotsByName(qr_generator)

    def retranslateUi(self, qr_generator):
        _translate = QtCore.QCoreApplication.translate
        qr_generator.setWindowTitle(_translate("qr_generator", "QR Generator"))
        self.browse.setText(_translate("qr_generator", "Browse"))
        self.run.setText(_translate("qr_generator", "Run"))
        self.url.setPlaceholderText(_translate("QR Generator", "Enter your text"))
        self.location.setPlaceholderText(_translate("QR Generator", "the image will be saved in this location"))

    def browse_folder(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Directory")
        if folder_path:
            self.location.setPlainText(folder_path)
    
    def run_program(self):
        self.qr_maker(self.url.toPlainText())

    def qr_maker(self, url):
        qr = segno.make(url, micro=False, error="h")
        qr.save(f"{self.location.toPlainText()}/QR.png", scale=10, dark="black", light="white")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qr_generator = QtWidgets.QMainWindow()
    ui = Ui_qr_generator()
    ui.setupUi(qr_generator)
    qr_generator.show()
    sys.exit(app.exec_())
