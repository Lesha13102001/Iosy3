import sys
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets
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


class Ui_Dialog_order(object):
    def setupUi(self, Dialog_order):
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME='order';"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)
        Dialog_order.setObjectName("Dialog_order")
        Dialog_order.resize(1141, 751)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_order)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 1141, 711))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(count)
        self.tableWidget.setRowCount(0)
        i = 0
        while i < count:
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            i = i + 1
        self.pushButton_back = QtWidgets.QPushButton(Dialog_order)
        self.pushButton_back.setGeometry(QtCore.QRect(1050, 10, 75, 23))
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_check = QtWidgets.QPushButton(Dialog_order)
        self.pushButton_check.setGeometry(QtCore.QRect(300, 10, 75, 23))
        self.pushButton_check.setObjectName("pushButton_check")
        self.pushButton_rev = QtWidgets.QPushButton(Dialog_order)
        self.pushButton_rev.setGeometry(QtCore.QRect(385, 10, 75, 23))
        self.pushButton_rev.setObjectName("pushButton_rev")
        self.lineEdit_year = QtWidgets.QLineEdit(Dialog_order)
        self.lineEdit_year.setGeometry(QtCore.QRect(210, 13, 50, 20))
        self.lineEdit_year.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_year.setMaxLength(4)
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.label = QtWidgets.QLabel(Dialog_order)
        self.label.setGeometry(QtCore.QRect(5, 5, 210, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(Dialog_order)
        self.label2.setGeometry(QtCore.QRect(265, 5, 30, 31))
        self.label2.setFont(font)
        self.label2.setObjectName("label")

        self.retranslateUi(Dialog_order)
        QtCore.QMetaObject.connectSlotsByName(Dialog_order)

    def retranslateUi(self, Dialog_order):
        _translate = QtCore.QCoreApplication.translate
        Dialog_order.setWindowTitle(_translate("Dialog_order", "Заказы"))
        self.pushButton_back.setText(_translate("Dialog_order", "Назад"))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.label.setText("Посмотреть заказы за")
        self.label2.setText("год")
        self.pushButton_check.setText(_translate("Dialog_order", "Применить"))
        self.pushButton_rev.setText(_translate("Dialog_order", "Отменить"))

        def add():
            global count
            global colums
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
                show_query = "SELECT * FROM `order` "
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
                    item.setText(_translate("Dialog_diet", l[i]))
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
                                    self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(str(row[l[k]])))
                                else:
                                    if typ[k] == "decimal(10,0)":
                                        self.tableWidget.setItem(tablerow, k,
                                                                 QtWidgets.QTableWidgetItem(str(row[l[k]])))
                                    else:
                                        self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(row[l[k]]))
                        k = k + 1
                    tablerow += 1

        add()


        def CheckYear():
            if (self.lineEdit_year.text() == ''):
                add = QMessageBox()
                add.setWindowTitle("Ошибка")
                add.setText("Введите год за который хотите посмотреть заказы")
                add.setStandardButtons(QMessageBox.Ok)
                add.exec_()
                return
            year=self.lineEdit_year.text()
            cursor = connection.cursor()
            with connection.cursor() as cursor:
                show_query = "SELECT * FROM `order` WHERE datest >= '"+str(year)+"-00-00' and datest <= '"+str(year)+"-12-31';"
                print(show_query)
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
                    item.setText(_translate("Dialog_diet", l[i]))
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
                                    self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(str(row[l[k]])))
                                else:
                                    if typ[k] == "decimal(10,0)":
                                        self.tableWidget.setItem(tablerow, k,
                                                                 QtWidgets.QTableWidgetItem(str(row[l[k]])))
                                    else:
                                        self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(row[l[k]]))
                        k = k + 1
                    tablerow += 1

        self.pushButton_check.clicked.connect(CheckYear)




        self.pushButton_rev.clicked.connect(add)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_order = QtWidgets.QDialog()
    ui = Ui_Dialog_order()
    ui.setupUi(Dialog_order)
    Dialog_order.show()
    sys.exit(app.exec_())
