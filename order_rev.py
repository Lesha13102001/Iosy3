import sys
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QHBoxLayout, QMessageBox

import time
from datetime import date, datetime, timedelta

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


class Ui_Dialog_order_date(object):
    def setupUi(self, Dialog_order_date):
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME='order';"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)
        Dialog_order_date.setObjectName("Dialog_order_date")
        Dialog_order_date.resize(1141, 751)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_order_date)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 1141, 711))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(count)
        self.tableWidget.setRowCount(0)
        i = 0
        while i < count:
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            i = i + 1
        self.pushButton_back = QtWidgets.QPushButton(Dialog_order_date)
        self.pushButton_back.setGeometry(QtCore.QRect(1050, 10, 75, 23))
        self.pushButton_back.setObjectName("pushButton_back")
        self.label = QtWidgets.QLabel(Dialog_order_date)
        self.label.setGeometry(QtCore.QRect(20, 10, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dateEdit_st = QtWidgets.QDateEdit(Dialog_order_date)
        self.dateEdit_st.setGeometry(QtCore.QRect(195, 15, 90, 20))
        self.dateEdit_st.setObjectName("dateEdit_st")
        self.label2 = QtWidgets.QLabel(Dialog_order_date)
        self.label2.setGeometry(QtCore.QRect(290, 10, 30, 31))
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.dateEdit_end = QtWidgets.QDateEdit(Dialog_order_date)
        self.dateEdit_end.setGeometry(QtCore.QRect(320, 15, 90, 20))
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.pushButton_check = QtWidgets.QPushButton(Dialog_order_date)
        self.pushButton_check.setGeometry(QtCore.QRect(420, 10, 80, 25))
        self.pushButton_check.setObjectName("pushButton_check")
        self.label3 = QtWidgets.QLabel(Dialog_order_date)
        self.label3.setGeometry(QtCore.QRect(510, 10, 30, 31))
        self.label3.setFont(font)
        self.label3.setObjectName("label2")

        self.retranslateUi(Dialog_order_date)
        QtCore.QMetaObject.connectSlotsByName(Dialog_order_date)

    def retranslateUi(self, Dialog_order_date):
        _translate = QtCore.QCoreApplication.translate
        Dialog_order_date.setWindowTitle(_translate("Dialog_order_date", "Заказы"))
        self.pushButton_back.setText(_translate("Dialog_order_date", "Назад"))
        self.label.setText("Кол-во клиентов с")
        self.label2.setText("по")
        self.pushButton_check.setText(_translate("Dialog_client", "Применить"))
        self.dateEdit_st.setDisplayFormat(_translate("Dialog_Add_order", "yyyy-MM-dd"))
        self.dateEdit_end.setDisplayFormat(_translate("Dialog_Add_order", "yyyy-MM-dd"))
        d = date.today()
        self.dateEdit_st.setDate(d)
        self.dateEdit_end.setDate(d + timedelta(days=31))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        def add():
            cursor = connection.cursor()
            with connection.cursor() as cursor:
                count = "SHOW COLUMNS FROM `order`;"
                cursor.execute(count)
                colums = cursor.fetchall()
                connection.commit()
            count = len(colums)
            count = count + 1
            cursor = connection.cursor()
            with connection.cursor() as cursor:
                show_query = "SELECT * FROM `order` WHERE datest >= '" + str(
                    self.dateEdit_st.text()) + "' and dateend <= '" + str(self.dateEdit_end.text()) + "';"
                cursor.execute(show_query)
                rows = cursor.fetchall()
                connection.commit()
                self.tableWidget.setRowCount(len(rows))
                self.tableWidget.setColumnHidden(0, True)
                tablerow = 0
                wr = count - 1
                i = 0
                l = []
                r = []
                typ = []

                for ro in rows:
                    r.append(ro)

                for colum in colums:
                    l.append(colum["Field"])

                while i < len(colums):
                    item = self.tableWidget.horizontalHeaderItem(i)
                    item.setText(l[i])
                    i = i + 1

                for type in colums:
                    typ.append(type["Type"])

                for row in rows:
                    k = 0
                    while k < wr:
                        if k == 0:
                            self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(str(row[l[k]])))
                        else:
                            if typ[k] == "date":
                                self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(str(row[l[k]])))
                            else:
                                if typ[k] == "int" or typ[k] == "int unsigned":
                                    self.tableWidget.setItem(tablerow, k,
                                                             QtWidgets.QTableWidgetItem(str(row[l[k]])))
                                else:
                                    if typ[k] == "decimal(10,0)":
                                        self.tableWidget.setItem(tablerow, k,
                                                                 QtWidgets.QTableWidgetItem(str(row[l[k]])))
                                    else:
                                        self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(row[l[k]]))
                        k = k + 1
                    tablerow += 1

        self.pushButton_check.clicked.connect(add)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_order_date = QtWidgets.QDialog()
    ui = Ui_Dialog_order_date()
    ui.setupUi(Dialog_order_date)
    Dialog_order_date.show()
    sys.exit(app.exec_())
