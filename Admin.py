from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Admin(object):
    def setupUi(self, Dialog_Admin):
        Dialog_Admin.setObjectName("Dialog_Admin")
        Dialog_Admin.resize(298, 135)
        self.pushButton_go_to_main = QtWidgets.QPushButton(Dialog_Admin)
        self.pushButton_go_to_main.setGeometry(QtCore.QRect(50, 90, 201, 31))
        self.pushButton_go_to_main.setObjectName("pushButton_go_to_main")
        self.pushButton_app = QtWidgets.QPushButton(Dialog_Admin)
        self.pushButton_app.setGeometry(QtCore.QRect(20, 20, 251, 23))
        self.pushButton_app.setObjectName("pushButton_app")
        self.pushButton_people = QtWidgets.QPushButton(Dialog_Admin)
        self.pushButton_people.setGeometry(QtCore.QRect(20, 50, 251, 23))
        self.pushButton_people.setObjectName("pushButton_people")

        self.retranslateUi(Dialog_Admin)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Admin)

    def retranslateUi(self, Dialog_Admin):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Admin.setWindowTitle(_translate("Dialog_Admin", "Администратор"))
        self.pushButton_go_to_main.setText(_translate("Dialog_Admin", "Выйти из режима Администратор"))
        self.pushButton_app.setText(_translate("Dialog_Admin", "Заявки"))
        self.pushButton_people.setText(_translate("Dialog_Admin", "Информация о отдыхающих"))


