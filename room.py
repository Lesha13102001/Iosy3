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


class Ui_Dialog_livingroom(object):
    def setupUi(self, Dialog_livingroom):
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME='livingroom';"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)
        count = count + 2

        Dialog_livingroom.setObjectName("Dialog_livingroom")
        Dialog_livingroom.resize(1141, 751)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_livingroom)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 1141, 711))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(count)
        self.tableWidget.setRowCount(0)

        i = 0
        while i < count:
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            i = i + 1

        self.pushButton_add_room = QtWidgets.QPushButton(Dialog_livingroom)
        self.pushButton_add_room.setGeometry(QtCore.QRect(10, 10, 141, 23))
        self.pushButton_add_room.setObjectName("pushButton_add_room")
        self.pushButton_back = QtWidgets.QPushButton(Dialog_livingroom)
        self.pushButton_back.setGeometry(QtCore.QRect(1050, 10, 75, 23))
        self.pushButton_back.setObjectName("pushButton_back")
        self.label = QtWidgets.QLabel(Dialog_livingroom)
        self.label.setGeometry(QtCore.QRect(180, 5, 210, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(Dialog_livingroom)
        self.label2.setGeometry(QtCore.QRect(360, 5, 30, 31))
        self.label2.setFont(font)
        self.label2.setObjectName("label2")

        self.retranslateUi(Dialog_livingroom)
        QtCore.QMetaObject.connectSlotsByName(Dialog_livingroom)

    def retranslateUi(self, Dialog_livingroom):
        _translate = QtCore.QCoreApplication.translate
        Dialog_livingroom.setWindowTitle(_translate("Dialog_livingroom", "Комнаты проживания"))
        self.pushButton_add_room.setText(_translate("Dialog_livingroom", "Добавить комнату"))
        self.pushButton_back.setText(_translate("Dialog_livingroom", "Назад"))
        self.label.setText("Общее кол-во комнат: ")

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM livingroom;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)
        count = count + 1
        item = self.tableWidget.horizontalHeaderItem(count - 1)
        item.setText(_translate("Dialog_livingroom", "Кнопка"))
        item = self.tableWidget.horizontalHeaderItem(count)
        item.setText(_translate("Dialog_livingroom", "Удалить"))
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            show_query = "SELECT * FROM `livingroom` "
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
                item.setText(_translate("Dialog_livingroom", l[i]))
                i = i + 1

            for type in colums:
                typ.append(type["Type"])

            def Lets():
                numb_row = self.tableWidget.currentRow()
                i = 1

                cursor = connection.cursor()
                with connection.cursor() as cursor:
                    while i < wr:
                        update_query = "UPDATE `livingroom` SET " + l[i] + "= '%s' WHERE idlivingroom = '%s';" % (
                        self.tableWidget.item(numb_row, i).text(), self.tableWidget.item(numb_row, 0).text())
                        cursor.execute(update_query)
                        i = i + 1
                    connection.commit()

            def Del():
                numb_row = self.tableWidget.currentRow()
                i = 1

                cursor = connection.cursor()
                with connection.cursor() as cursor:
                    while i < wr:
                        delete_query = "DELETE FROM `livingroom` WHERE idlivingroom = %s" % (
                            self.tableWidget.item(numb_row, 0).text())
                        cursor.execute(delete_query)
                        i = i + 1
                    connection.commit()
                button_deactivate = button_del + str(numb_row)
                buttondel[button_deactivate].setEnabled(False)
                self.tableWidget.setRowHidden(numb_row, True)
                roomkol()

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

        def roomkol():
            cursor = connection.cursor()
            with connection.cursor() as cursor:
                show_query = "SELECT COUNT(*) as count FROM `livingroom` ;"
                cursor.execute(show_query)
                count = cursor.fetchall()
                connection.commit()
            self.label2.setText(str(count[0]["count"]))

        roomkol()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_livingroom = QtWidgets.QDialog()
    ui = Ui_Dialog_livingroom()
    ui.setupUi(Dialog_livingroom)
    Dialog_livingroom.show()
    sys.exit(app.exec_())
