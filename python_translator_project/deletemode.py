from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Deletemode(object):
    def setupUi(self, Deletemode):
        Deletemode.setObjectName("Deletemode")
        Deletemode.resize(800, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.All, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.All, QtGui.QPalette.ColorRole.WindowText, brush)
        Deletemode.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(parent=Deletemode)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 40, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #FFFFFF;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 110, 411, 421))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(450, 140, 81, 31))
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 120, 291, 16))
        self.label_2.setStyleSheet("color: #FFFFFF;")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 180, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: #2ecc71;")
        Deletemode.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Deletemode)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Deletemode.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Deletemode)
        self.statusbar.setObjectName("statusbar")
        Deletemode.setStatusBar(self.statusbar)

        self.retranslateUi(Deletemode)
        QtCore.QMetaObject.connectSlotsByName(Deletemode)

    def retranslateUi(self, Deletemode):
        _translate = QtCore.QCoreApplication.translate
        Deletemode.setWindowTitle(_translate("Deletemode", "DeleteMode"))
        self.label.setText(_translate("Deletemode", "Delete Mode"))
        self.label_2.setText(_translate("Deletemode", "Select the number of the pair you want to delete"))
        self.pushButton.setText(_translate("Deletemode", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Deletemode = QtWidgets.QMainWindow()
    ui = Ui_Deletemode()
    ui.setupUi(Deletemode)
    Deletemode.show()
    sys.exit(app.exec())