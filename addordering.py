import sys
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date, timedelta
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QHBoxLayout, QMessageBox

import time

from array import *

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


class Ui_Dialog_Add_order(object):
    def setupUi(self, Dialog_Add_order):
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            countcl = "SELECT * FROM `client` "
            cursor.execute(countcl)
            countcl = cursor.fetchall()
            countd = "SELECT * FROM `diagnos` "
            cursor.execute(countd)
            countd = cursor.fetchall()
            countr = "SELECT * FROM `livingroom` "
            cursor.execute(countr)
            countr = cursor.fetchall()
            countdisc = "SELECT * FROM `discount` "
            cursor.execute(countdisc)
            countdisc = cursor.fetchall()
            countpr = "SELECT * FROM `procedure` "
            cursor.execute(countpr)
            countpr = cursor.fetchall()
            countw = "SELECT * FROM `worker` "
            cursor.execute(countw)
            countw = cursor.fetchall()
            connection.commit()
        countcl = len(countcl)
        countd = len(countd)
        countr = len(countr)
        countdisc = len(countdisc)
        countpr = len(countpr)
        countw = len(countw)

        Dialog_Add_order.setObjectName("Dialog_Add_order")
        Dialog_Add_order.resize(630, 567)
        self.label = QtWidgets.QLabel(Dialog_Add_order)
        self.label.setGeometry(QtCore.QRect(200, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_Add_order)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_client = QtWidgets.QComboBox(Dialog_Add_order)
        self.comboBox_client.setGeometry(QtCore.QRect(160, 70, 131, 31))
        self.comboBox_client.setObjectName("comboBox_client")
        self.dateEdit_st = QtWidgets.QDateEdit(Dialog_Add_order)
        self.dateEdit_st.setGeometry(QtCore.QRect(160, 120, 131, 31))
        i = 0
        while i < countcl:
            self.comboBox_client.addItem("")
            i = i + 1
        self.dateEdit_st.setObjectName("dateEdit_st")
        self.label_3 = QtWidgets.QLabel(Dialog_Add_order)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog_Add_order)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.dateEdit_end = QtWidgets.QDateEdit(Dialog_Add_order)
        self.dateEdit_end.setGeometry(QtCore.QRect(160, 170, 131, 31))
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.label_5 = QtWidgets.QLabel(Dialog_Add_order)
        self.label_5.setGeometry(QtCore.QRect(60, 220, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog_Add_order)
        self.label_6.setGeometry(QtCore.QRect(60, 270, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog_Add_order)
        self.label_7.setGeometry(QtCore.QRect(70, 320, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog_Add_order)
        self.label_8.setGeometry(QtCore.QRect(40, 370, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog_Add_order)
        self.label_9.setGeometry(QtCore.QRect(40, 420, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_add_order = QtWidgets.QPushButton(Dialog_Add_order)
        self.pushButton_add_order.setGeometry(QtCore.QRect(140, 500, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_add_order.setFont(font)
        self.pushButton_add_order.setObjectName("pushButton_add_order")
        self.comboBox_diagnos = QtWidgets.QComboBox(Dialog_Add_order)
        self.comboBox_diagnos.setGeometry(QtCore.QRect(160, 230, 131, 31))
        self.comboBox_diagnos.setObjectName("comboBox_diagnos")
        i = 0
        while i < countd:
            self.comboBox_diagnos.addItem("")
            i = i + 1
        self.comboBox_room = QtWidgets.QComboBox(Dialog_Add_order)
        self.comboBox_room.setGeometry(QtCore.QRect(160, 280, 131, 31))
        self.comboBox_room.setObjectName("comboBox_room")
        i = 0
        while i < countr:
            self.comboBox_room.addItem("")
            i = i + 1
        self.comboBox_discount = QtWidgets.QComboBox(Dialog_Add_order)
        self.comboBox_discount.setGeometry(QtCore.QRect(160, 330, 131, 31))
        self.comboBox_discount.setObjectName("comboBox_discount")
        i = 0
        while i < countdisc:
            self.comboBox_discount.addItem("")
            i = i + 1
        self.comboBox_procedure = QtWidgets.QComboBox(Dialog_Add_order)
        self.comboBox_procedure.setGeometry(QtCore.QRect(160, 380, 131, 31))
        self.comboBox_procedure.setObjectName("comboBox_procedure")
        i = 0
        while i < countpr:
            self.comboBox_procedure.addItem("")
            i = i + 1
        self.comboBox_worker = QtWidgets.QComboBox(Dialog_Add_order)
        self.comboBox_worker.setGeometry(QtCore.QRect(160, 430, 131, 31))
        self.comboBox_worker.setObjectName("comboBox_worker")
        i = 0
        while i < countw:
            self.comboBox_worker.addItem("")
            i = i + 1
        self.pushButton_back = QtWidgets.QPushButton(Dialog_Add_order)
        self.pushButton_back.setGeometry(QtCore.QRect(330, 500, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")

        self.retranslateUi(Dialog_Add_order)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Add_order)

    def retranslateUi(self, Dialog_Add_order):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Add_order.setWindowTitle(_translate("Dialog_Add_order", "Оформление заказа"))
        self.label.setText(_translate("Dialog_Add_order", "Оформление заказа"))
        self.label_2.setText(_translate("Dialog_Add_order", "Клиент:"))
        self.dateEdit_st.setDisplayFormat(_translate("Dialog_Add_order", "yyyy-MM-dd"))
        self.label_3.setText(_translate("Dialog_Add_order", "Дата приезда:"))
        self.label_4.setText(_translate("Dialog_Add_order", "Дата отъезда:"))
        self.dateEdit_end.setDisplayFormat(_translate("Dialog_Add_order", "yyyy-MM-dd"))
        self.label_5.setText(_translate("Dialog_Add_order", "Диагноз:"))
        self.label_6.setText(_translate("Dialog_Add_order", "Комната:"))
        self.label_7.setText(_translate("Dialog_Add_order", "Скидка:"))
        self.label_8.setText(_translate("Dialog_Add_order", "Процедура:"))
        self.label_9.setText(_translate("Dialog_Add_order", "Сутрудник:"))
        self.pushButton_add_order.setText(_translate("Dialog_Add_order", "Добавить"))
        self.pushButton_back.setText(_translate("Dialog_Add_order", "Назад"))
        d = date.today()
        self.dateEdit_st.setDate(d)
        self.dateEdit_end.setDate(d + timedelta(days=5))

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            countcl = "SELECT * FROM `client` "
            cursor.execute(countcl)
            rcountcl = cursor.fetchall()
            countd = "SELECT * FROM `diagnos` "
            cursor.execute(countd)
            rcountd = cursor.fetchall()
            countr = "SELECT * FROM `livingroom` "
            cursor.execute(countr)
            rcountr = cursor.fetchall()
            countdisc = "SELECT * FROM `discount` "
            cursor.execute(countdisc)
            rcountdisc = cursor.fetchall()
            countpr = "SELECT * FROM `procedure` "
            cursor.execute(countpr)
            rcountpr = cursor.fetchall()
            countw = "SELECT * FROM `worker` "
            cursor.execute(countw)
            rcountw = cursor.fetchall()
            connection.commit()
        countcl = len(rcountcl)
        countd = len(rcountd)
        countr = len(rcountr)
        countdisc = len(rcountdisc)
        countpr = len(rcountpr)
        countw = len(rcountw)

        idcl = []
        idd = []
        idr = []
        iddisc = []
        idpr = []
        idw = []

        for cl in rcountcl:
            idcl.append(cl["idclient"])

        i = 0
        while i < countcl:
            self.comboBox_client.setItemText(i, _translate("Dialog_Order_add", str(idcl[i])))
            i += 1

        for d in rcountd:
            idd.append(d["iddiagnos"])

        i = 0
        while i < countd:
            self.comboBox_diagnos.setItemText(i, _translate("Dialog_Order_add", str(idd[i])))
            i += 1

        for r in rcountr:
            idr.append(r["idlivingroom"])

        i = 0
        while i < countr:
            self.comboBox_room.setItemText(i, _translate("Dialog_Order_add", str(idr[i])))
            i += 1

        for disc in rcountdisc:
            iddisc.append(disc["iddiscount"])

        i = 0
        while i < countdisc:
            self.comboBox_discount.setItemText(i, _translate("Dialog_Order_add", str(iddisc[i])))
            i += 1

        for pr in rcountpr:
            idpr.append(pr["idprocedure"])

        i = 0
        while i < countpr:
            self.comboBox_procedure.setItemText(i, _translate("Dialog_Order_add", str(idpr[i])))
            i += 1

        for w in rcountw:
            idw.append(w["idworker"])

        i = 0
        while i < countw:
            self.comboBox_worker.setItemText(i, _translate("Dialog_Order_add", str(idw[i])))
            i += 1





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Add_order = QtWidgets.QDialog()
    ui = Ui_Dialog_Add_order()
    ui.setupUi(Dialog_Add_order)
    Dialog_Add_order.show()
    sys.exit(app.exec_())
