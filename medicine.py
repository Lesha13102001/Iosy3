import sys
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QHBoxLayout, QMessageBox

import time
from datetime import date, datetime

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



def delmed():
    cursor = connection.cursor()
    with connection.cursor() as cursor:
        show_query = "SELECT * FROM `medicine` "
        cursor.execute(show_query)
        rows = cursor.fetchall()
        connection.commit()

    d = datetime.today()

    for row in rows:
        q = datetime.strptime(str(row["expired"]), "%Y-%m-%d") - d
        if q.days < 0:
            cursor = connection.cursor()
            with connection.cursor() as cursor:
                delete_query = "DELETE FROM `medicine` WHERE idmedicine = %s" % (row["idmedicine"])
                cursor.execute(delete_query)
                connection.commit()
            add = QMessageBox()
            add.setWindowTitle("Уведомление")
            add.setText("Лекарство " + str(row) + " вышло из срока годности, поэтому оно будет списано")
            add.setStandardButtons(QMessageBox.Ok)
            add.exec_()





class Ui_Dialog_medicine(object):
    def setupUi(self, Dialog_medicine):
        delmed()
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME='medicine';"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)
        count = count + 2
        Dialog_medicine.setObjectName("Dialog_medicine")
        Dialog_medicine.resize(1141, 751)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_medicine)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 1141, 711))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(count)
        self.tableWidget.setRowCount(0)
        i = 0
        while i < count:
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            i = i + 1

        self.pushButton_add_medicine = QtWidgets.QPushButton(Dialog_medicine)
        self.pushButton_add_medicine.setGeometry(QtCore.QRect(10, 10, 141, 23))
        self.pushButton_add_medicine.setObjectName("pushButton_add_medicine")
        self.pushButton_back = QtWidgets.QPushButton(Dialog_medicine)
        self.pushButton_back.setGeometry(QtCore.QRect(1050, 10, 75, 23))
        self.pushButton_back.setObjectName("pushButton_back")

        self.retranslateUi(Dialog_medicine)
        QtCore.QMetaObject.connectSlotsByName(Dialog_medicine)

    def retranslateUi(self, Dialog_medicine):
        _translate = QtCore.QCoreApplication.translate
        Dialog_medicine.setWindowTitle(_translate("Dialog_medicine", "Медикоменты"))
        self.pushButton_add_medicine.setText(_translate("Dialog_medicine", "Добавить лекарство"))
        self.pushButton_back.setText(_translate("Dialog_medicine", "Назад"))


        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM `medicine`;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)
        count = count + 1
        item = self.tableWidget.horizontalHeaderItem(count - 1)
        item.setText(_translate("Dialog_medicine", "Кнопка"))
        item = self.tableWidget.horizontalHeaderItem(count)
        item.setText(_translate("Dialog_medicine", "Удалить"))
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            show_query = "SELECT * FROM `medicine` "
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
                item.setText(_translate("Dialog_medicine", l[i]))
                i = i + 1

            for type in colums:
                typ.append(type["Type"])

            def Lets():
                numb_row = self.tableWidget.currentRow()
                i = 1

                cursor = connection.cursor()
                with connection.cursor() as cursor:
                    while i < wr:
                        update_query = "UPDATE `medicine` SET " + l[i] + "= '%s' WHERE idmedicine = '%s';" % (self.tableWidget.item(numb_row, i).text(), self.tableWidget.item(numb_row, 0).text())
                        cursor.execute(update_query)
                        i = i + 1
                    connection.commit()

            def Del():
                numb_row = self.tableWidget.currentRow()
                i = 1

                cursor = connection.cursor()
                with connection.cursor() as cursor:
                    delete_query = "DELETE FROM `medicine` WHERE idmedicine = %s" % (self.tableWidget.item(numb_row, 0).text())
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_medicine = QtWidgets.QDialog()
    ui = Ui_Dialog_medicine()
    ui.setupUi(Dialog_medicine)
    Dialog_medicine.show()
    sys.exit(app.exec_())
