import sys
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets

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


class Ui_Dialog_worker(object):
    def setupUi(self, Dialog_worker):
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME='worker';"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)
        count = count + 2

        Dialog_worker.setObjectName("Dialog_worker")
        Dialog_worker.resize(1141, 751)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_worker)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 1141, 711))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(count)
        self.tableWidget.setRowCount(0)
        i = 0
        while i < count:
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            i = i + 1

        self.pushButton_add_worker = QtWidgets.QPushButton(Dialog_worker)
        self.pushButton_add_worker.setGeometry(QtCore.QRect(10, 10, 141, 23))
        self.pushButton_add_worker.setObjectName("pushButton_add_worker")
        self.pushButton_back = QtWidgets.QPushButton(Dialog_worker)
        self.pushButton_back.setGeometry(QtCore.QRect(1050, 10, 75, 23))
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_rev = QtWidgets.QPushButton(Dialog_worker)
        self.pushButton_rev.setGeometry(QtCore.QRect(180, 10, 250, 23))
        self.pushButton_rev.setObjectName("pushButton_rev")

        self.retranslateUi(Dialog_worker)
        QtCore.QMetaObject.connectSlotsByName(Dialog_worker)

    def retranslateUi(self, Dialog_worker):
        _translate = QtCore.QCoreApplication.translate
        Dialog_worker.setWindowTitle(_translate("Dialog_worker", "Сотрудники"))
        self.pushButton_add_worker.setText(_translate("Dialog_worker", "Добавить сотрудника"))
        self.pushButton_back.setText(_translate("Dialog_worker", "Назад"))
        self.pushButton_rev.setText(_translate("Dialog_worker", "Вывести в алфавитном порядке (по имени)"))

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM worker;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)
        count = count + 1
        item = self.tableWidget.horizontalHeaderItem(count - 1)
        item.setText(_translate("Dialog_worker", "Кнопка"))
        item = self.tableWidget.horizontalHeaderItem(count)
        item.setText(_translate("Dialog_worker", "Удалить"))
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            show_query = "SELECT * FROM `worker`"
            cursor.execute(show_query)
            rows = cursor.fetchall()
            connection.commit()
            self.tableWidget.setRowCount(len(rows))
            self.tableWidget.setColumnHidden(0, True)
            tablerow = 0
            button_name = "button"
            button = {}
            button_del = "buttondel"
            buttondel = {}
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
                item.setText(_translate("Dialog_worker", l[i]))
                i = i + 1

            for type in colums:
                typ.append(type["Type"])

            def Lets():
                numb_row = self.tableWidget.currentRow()
                i = 1

                cursor = connection.cursor()
                with connection.cursor() as cursor:
                    while i < wr:
                        update_query = "UPDATE `worker` SET " + l[i] + "= '%s' WHERE idworker = '%s';" % (self.tableWidget.item(numb_row, i).text(), self.tableWidget.item(numb_row, 0).text())
                        print(update_query)
                        cursor.execute(update_query)
                        i = i + 1
                    connection.commit()

            def Del():
                numb_row = self.tableWidget.currentRow()
                i = 1

                cursor = connection.cursor()
                with connection.cursor() as cursor:
                    delete_query = "DELETE FROM `worker` WHERE idworker = %s" % (self.tableWidget.item(numb_row, 0).text())
                    print(delete_query)
                    cursor.execute(delete_query)
                    connection.commit()
                button_deactivate = button_del + str(numb_row)
                buttondel[button_deactivate].setEnabled(False)
                self.tableWidget.setRowHidden(numb_row, True)


            for row in rows:
                k = 0
                button_name2 = button_name + str(tablerow)
                button[button_name2] = QtWidgets.QPushButton()
                button[button_name2].setText("Изменить")

                button_del2 = button_del + str(tablerow)
                buttondel[button_del2] = QtWidgets.QPushButton()
                buttondel[button_del2].setText("Удалить")
                while k < wr:
                    if k == 0:
                        self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(str(row[l[k]])))
                    else:
                        if typ[k] == "date":
                            self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(str(row[l[k]])))
                        else:
                            if typ[k] == "int":
                                self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(str(row[l[k]])))
                            else:
                                if typ[k] == "decimal(10,0)":
                                    self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(str(row[l[k]])))
                                else:
                                    self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(row[l[k]]))
                    k = k + 1
                self.tableWidget.setCellWidget(tablerow, k, button[button_name2])
                button[button_name2].clicked.connect(Lets)
                self.tableWidget.setCellWidget(tablerow, k + 1, buttondel[button_del2])
                buttondel[button_del2].clicked.connect(Del)
                tablerow += 1

        def alf():
            cursor = connection.cursor()
            with connection.cursor() as cursor:
                show_query = "SELECT * FROM `worker` ORDER BY namew"
                cursor.execute(show_query)
                rows = cursor.fetchall()
                connection.commit()
                self.tableWidget.setRowCount(len(rows))
                self.tableWidget.setColumnHidden(0, True)
                tablerow = 0
                button_name = "button"
                button = {}
                button_del = "buttondel"
                buttondel = {}
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
                    item.setText(_translate("Dialog_worker", l[i]))
                    i = i + 1

                for type in colums:
                    typ.append(type["Type"])

                def Lets():
                    numb_row = self.tableWidget.currentRow()
                    i = 1

                    cursor = connection.cursor()
                    with connection.cursor() as cursor:
                        while i < wr:
                            update_query = "UPDATE `worker` SET " + l[i] + "= '%s' WHERE idworker = '%s';" % (
                            self.tableWidget.item(numb_row, i).text(), self.tableWidget.item(numb_row, 0).text())
                            print(update_query)
                            cursor.execute(update_query)
                            i = i + 1
                        connection.commit()

                def Del():
                    numb_row = self.tableWidget.currentRow()
                    i = 1

                    cursor = connection.cursor()
                    with connection.cursor() as cursor:
                        delete_query = "DELETE FROM `worker` WHERE idworker = %s" % (
                            self.tableWidget.item(numb_row, 0).text())
                        print(delete_query)
                        cursor.execute(delete_query)
                        connection.commit()
                    button_deactivate = button_del + str(numb_row)
                    buttondel[button_deactivate].setEnabled(False)
                    self.tableWidget.setRowHidden(numb_row, True)

                for row in rows:
                    k = 0
                    button_name2 = button_name + str(tablerow)
                    button[button_name2] = QtWidgets.QPushButton()
                    button[button_name2].setText("Изменить")

                    button_del2 = button_del + str(tablerow)
                    buttondel[button_del2] = QtWidgets.QPushButton()
                    buttondel[button_del2].setText("Удалить")
                    while k < wr:
                        if k == 0:
                            self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(str(row[l[k]])))
                        else:
                            if typ[k] == "date":
                                self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(str(row[l[k]])))
                            else:
                                if typ[k] == "int":
                                    self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(str(row[l[k]])))
                                else:
                                    if typ[k] == "decimal(10,0)":
                                        self.tableWidget.setItem(tablerow, k,
                                                                 QtWidgets.QTableWidgetItem(str(row[l[k]])))
                                    else:
                                        self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(row[l[k]]))
                        k = k + 1
                    self.tableWidget.setCellWidget(tablerow, k, button[button_name2])
                    button[button_name2].clicked.connect(Lets)
                    self.tableWidget.setCellWidget(tablerow, k + 1, buttondel[button_del2])
                    buttondel[button_del2].clicked.connect(Del)
                    tablerow += 1

        self.pushButton_rev.clicked.connect(alf)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_worker = QtWidgets.QDialog()
    ui = Ui_Dialog_worker()
    ui.setupUi(Dialog_worker)
    Dialog_worker.show()
    sys.exit(app.exec_())
