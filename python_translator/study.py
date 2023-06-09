from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_studymode(object):
    def setupUi(self, studymode):
        studymode.setObjectName("studymode")
        studymode.resize(800, 600)
        studymode.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(parent=studymode)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 220, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.label.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setIndent(50)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(410, 220, 241, 61))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 180, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 300, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 0, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 300, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        studymode.setCentralWidget(self.centralwidget)

        self.retranslateUi(studymode)
        QtCore.QMetaObject.connectSlotsByName(studymode)

        self.label.setStyleSheet("color: black;")
        self.label_2.setStyleSheet("color: black;")
        self.label_3.setStyleSheet("color: black;")
        self.label_4.setStyleSheet("color: black;")
        self.pushButton.setStyleSheet("background-color: #2ecc71; color: white;")
        self.pushButton_2.setStyleSheet("background-color: #e74c3c; color: white;")

    def retranslateUi(self, studymode):
        _translate = QtCore.QCoreApplication.translate
        studymode.setWindowTitle(_translate("studymode", "studymode"))
        self.label.setText(_translate("studymode", "rep"))
        self.label_2.setText(_translate("studymode", "Word:"))
        self.label_3.setText(_translate("studymode", "Translate:"))
        self.pushButton.setText(_translate("studymode", "Refresh"))
        self.label_4.setText(_translate("studymode", "Study Mode"))
        self.pushButton_2.setText(_translate("studymode", "Check Translation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    studymode = QtWidgets.QMainWindow()
    ui = Ui_studymode()
    ui.setupUi(studymode)
    studymode.show()
    sys.exit(app.exec())
