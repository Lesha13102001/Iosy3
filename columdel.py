from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_deletecolum(object):
    def setupUi(self, Dialog_deletecolum):
        Dialog_deletecolum.setObjectName("Dialog_deletecolum")
        Dialog_deletecolum.resize(400, 186)
        self.label = QtWidgets.QLabel(Dialog_deletecolum)
        self.label.setGeometry(QtCore.QRect(10, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_name = QtWidgets.QComboBox(Dialog_deletecolum)
        self.comboBox_name.setGeometry(QtCore.QRect(200, 50, 191, 31))
        self.comboBox_name.setObjectName("comboBox_name")
        self.pushButton_deletecolum = QtWidgets.QPushButton(Dialog_deletecolum)
        self.pushButton_deletecolum.setGeometry(QtCore.QRect(30, 130, 141, 41))
        self.pushButton_deletecolum.setObjectName("pushButton_deletecolum")
        self.pushButton_back2 = QtWidgets.QPushButton(Dialog_deletecolum)
        self.pushButton_back2.setGeometry(QtCore.QRect(260, 130, 71, 41))
        self.pushButton_back2.setObjectName("pushButton_back2")

        self.retranslateUi(Dialog_deletecolum)
        QtCore.QMetaObject.connectSlotsByName(Dialog_deletecolum)

    def retranslateUi(self, Dialog_deletecolum):
        _translate = QtCore.QCoreApplication.translate
        Dialog_deletecolum.setWindowTitle(_translate("Dialog_deletecolum", "Удалить"))
        self.label.setText(_translate("Dialog_deletecolum", "Выберите столбец:"))
        self.pushButton_deletecolum.setText(_translate("Dialog_deletecolum", "Удалить"))
        self.pushButton_back2.setText(_translate("Dialog_deletecolum", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_deletecolum = QtWidgets.QDialog()
    ui = Ui_Dialog_deletecolum()
    ui.setupUi(Dialog_deletecolum)
    Dialog_deletecolum.show()
    sys.exit(app.exec_())
