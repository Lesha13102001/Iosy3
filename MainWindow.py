import sys
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QHBoxLayout, QMessageBox

from array import *
from datetime import datetime, date, timedelta

import pymysql
from Config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)
except Exception as ex:
    print("Connection refused...")
    print(ex)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(617, 547)
        self.order = QtWidgets.QPushButton(Dialog)
        self.order.setGeometry(QtCore.QRect(40, 40, 75, 23))
        self.order.setObjectName("order")
        self.diagnos = QtWidgets.QPushButton(Dialog)
        self.diagnos.setGeometry(QtCore.QRect(130, 40, 75, 23))
        self.diagnos.setObjectName("diagnos")
        self.diet = QtWidgets.QPushButton(Dialog)
        self.diet.setGeometry(QtCore.QRect(220, 40, 75, 23))
        self.diet.setObjectName("diet")
        self.client = QtWidgets.QPushButton(Dialog)
        self.client.setGeometry(QtCore.QRect(310, 40, 75, 23))
        self.client.setObjectName("client")
        self.discount = QtWidgets.QPushButton(Dialog)
        self.discount.setGeometry(QtCore.QRect(400, 40, 75, 23))
        self.discount.setObjectName("discount")
        self.equipment = QtWidgets.QPushButton(Dialog)
        self.equipment.setGeometry(QtCore.QRect(490, 40, 91, 23))
        self.equipment.setObjectName("equipment")
        self.room = QtWidgets.QPushButton(Dialog)
        self.room.setGeometry(QtCore.QRect(40, 80, 75, 23))
        self.room.setObjectName("room")
        self.medicine = QtWidgets.QPushButton(Dialog)
        self.medicine.setGeometry(QtCore.QRect(130, 80, 81, 23))
        self.medicine.setObjectName("medicine")
        self.procedure = QtWidgets.QPushButton(Dialog)
        self.procedure.setGeometry(QtCore.QRect(220, 80, 75, 23))
        self.procedure.setObjectName("procedure")
        self.worker = QtWidgets.QPushButton(Dialog)
        self.worker.setGeometry(QtCore.QRect(310, 80, 75, 23))
        self.worker.setObjectName("worker")
        self.new_order = QtWidgets.QPushButton(Dialog)
        self.new_order.setGeometry(QtCore.QRect(250, 400, 101, 23))
        self.new_order.setObjectName("new_order")
        self.order_rev = QtWidgets.QPushButton(Dialog)
        self.order_rev.setGeometry(QtCore.QRect(40, 150, 250, 23))
        self.order_rev.setObjectName("order_rev")
        self.client_rev = QtWidgets.QPushButton(Dialog)
        self.client_rev.setGeometry(QtCore.QRect(40, 180, 250, 23))
        self.client_rev.setObjectName("order_client_rev")
        self.client_worker = QtWidgets.QPushButton(Dialog)
        self.client_worker.setGeometry(QtCore.QRect(40, 210, 250, 23))
        self.client_worker.setObjectName("order_client_worker")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.order.setText(_translate("Dialog", "Заказы"))
        self.diagnos.setText(_translate("Dialog", "Диагнозы"))
        self.diet.setText(_translate("Dialog", "Диеты"))
        self.client.setText(_translate("Dialog", "Клиенты"))
        self.discount.setText(_translate("Dialog", "Скидки"))
        self.equipment.setText(_translate("Dialog", "Оборудование"))
        self.room.setText(_translate("Dialog", "Комнаты"))
        self.medicine.setText(_translate("Dialog", "Медикоменты"))
        self.procedure.setText(_translate("Dialog", "Процедуры"))
        self.worker.setText(_translate("Dialog", "Рабочие"))
        self.new_order.setText(_translate("Dialog", "Оформить заказ"))
        self.order_rev.setText("Кол-во заказов за определенный период")
        self.client_rev.setText("Клиенты и кол-во их заказов")
        self.client_worker.setText("Общий список клиентов и врачей")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
