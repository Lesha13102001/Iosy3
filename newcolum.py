from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_addcolum(object):
    def setupUi(self, Dialog_addcolum):
        Dialog_addcolum.setObjectName("Dialog_addcolum")
        Dialog_addcolum.resize(400, 234)
        self.label_type = QtWidgets.QLabel(Dialog_addcolum)
        self.label_type.setGeometry(QtCore.QRect(20, 40, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_type.setFont(font)
        self.label_type.setObjectName("label_type")
        self.comboBox = QtWidgets.QComboBox(Dialog_addcolum)
        self.comboBox.setGeometry(QtCore.QRect(250, 40, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_name = QtWidgets.QLabel(Dialog_addcolum)
        self.label_name.setGeometry(QtCore.QRect(40, 110, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.lineEdit = QtWidgets.QLineEdit(Dialog_addcolum)
        self.lineEdit.setGeometry(QtCore.QRect(230, 119, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_addcolum = QtWidgets.QPushButton(Dialog_addcolum)
        self.pushButton_addcolum.setGeometry(QtCore.QRect(70, 170, 121, 31))
        self.pushButton_addcolum.setObjectName("pushButton_addcolum")
        self.pushButton = QtWidgets.QPushButton(Dialog_addcolum)
        self.pushButton.setGeometry(QtCore.QRect(270, 170, 75, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog_addcolum)
        QtCore.QMetaObject.connectSlotsByName(Dialog_addcolum)

    def retranslateUi(self, Dialog_addcolum):
        _translate = QtCore.QCoreApplication.translate
        Dialog_addcolum.setWindowTitle(_translate("Dialog_addcolum", "Новый столбец"))
        self.label_type.setText(_translate("Dialog_addcolum", "Выберите тип данных:"))
        self.comboBox.setItemText(0, _translate("Dialog_addcolum", "INT"))
        self.comboBox.setItemText(1, _translate("Dialog_addcolum", "VARCHAR(100)"))
        self.comboBox.setItemText(2, _translate("Dialog_addcolum", "DECIMAL"))
        self.comboBox.setItemText(3, _translate("Dialog_addcolum", "DATE"))
        self.label_name.setText(_translate("Dialog_addcolum", "Название столбца:"))
        self.pushButton_addcolum.setText(_translate("Dialog_addcolum", "Добавить"))
        self.pushButton.setText(_translate("Dialog_addcolum", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_addcolum = QtWidgets.QDialog()
    ui = Ui_Dialog_addcolum()
    ui.setupUi(Dialog_addcolum)
    Dialog_addcolum.show()
    sys.exit(app.exec_())
