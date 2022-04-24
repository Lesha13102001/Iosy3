from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(176, 114)
        self.label_admin = QtWidgets.QLabel(Admin)
        self.label_admin.setGeometry(QtCore.QRect(10, 0, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_admin.setFont(font)
        self.label_admin.setObjectName("label_admin")
        self.lineEdit_admin = QtWidgets.QLineEdit(Admin)
        self.lineEdit_admin.setGeometry(QtCore.QRect(10, 40, 151, 20))
        self.lineEdit_admin.setObjectName("lineEdit_admin")
        self.pushButton_admin_go = QtWidgets.QPushButton(Admin)
        self.pushButton_admin_go.setGeometry(QtCore.QRect(10, 80, 75, 23))
        self.pushButton_admin_go.setObjectName("pushButton_admin_go")
        self.pushButton_admin_back = QtWidgets.QPushButton(Admin)
        self.pushButton_admin_back.setGeometry(QtCore.QRect(90, 80, 75, 23))
        self.pushButton_admin_back.setObjectName("pushButton_admin_back")

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Вход"))
        self.label_admin.setText(_translate("Admin", "Введите пароль:"))
        self.pushButton_admin_go.setText(_translate("Admin", "Вход"))
        self.pushButton_admin_back.setText(_translate("Admin", "Назад"))
