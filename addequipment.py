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


class Ui_Dialog_addequipment(object):
    def setupUi(self, Dialog_addequipment):
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME='equipment';"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)
        count = count + 2
        Dialog_addequipment.setObjectName("Dialog_addequipment")
        Dialog_addequipment.resize(1141, 709)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_addequipment)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1141, 711))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(count)
        self.tableWidget.setRowCount(0)
        i = 0
        while i < count:
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            i = i + 1

        self.err = 0
        self.retranslateUi(Dialog_addequipment)
        QtCore.QMetaObject.connectSlotsByName(Dialog_addequipment)

    def retranslateUi(self, Dialog_addequipment):
        _translate = QtCore.QCoreApplication.translate
        Dialog_addequipment.setWindowTitle(_translate("Dialog_addequipment", "Добавить"))

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM `equipment`;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)
        count = count + 1
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnHidden(0, True)
        item = self.tableWidget.horizontalHeaderItem(count - 1)
        item.setText(_translate("Dialog_addequipment", "Добавить"))
        item = self.tableWidget.horizontalHeaderItem(count)
        item.setText(_translate("Dialog_addequipment", "Вернуться назад"))

        def Lets():
            try:
                i = 0
                inf = []
                while i < wr - 1:
                    inf.append(self.tableWidget.item(0, i + 1).text())
                    i = i + 1
                i = 1
                inf = str(inf)
                leng = len(inf)
                inf = inf[1:leng - 1]
                cursor = connection.cursor()
                with connection.cursor() as cursor:
                    insert_query = "INSERT INTO `equipment` (" + inf_x + ") VALUES (" + inf + ");"
                    print(insert_query)
                    cursor.execute(insert_query)
                    connection.commit()
                self.err = 0
            except Exception as diet:
                self.err = 1
                if str(diet) == "'NoneType' object has no attribute 'text'":
                    add = QMessageBox()
                    add.setWindowTitle("Ошибка")
                    add.setText("Поле пустое")
                    add.setStandardButtons(QMessageBox.Ok)
                    add.exec_()
                    return
                else:
                    add = QMessageBox()
                    add.setWindowTitle("Ошибка из MySQL: ")
                    add.setText(str(diet))
                    add.setStandardButtons(QMessageBox.Ok)
                    add.exec_()
                    return

        button_add = QtWidgets.QPushButton()
        button_back = QtWidgets.QPushButton()
        button_add.setText("Добавить")
        button_back.setText("Назад")
        self.tableWidget.setCellWidget(0, count - 1, button_add)
        button_add.clicked.connect(Lets)
        self.tableWidget.setCellWidget(0, count, button_back)

        wr = count - 1
        i = 0
        l = []

        for colum in colums:
            l.append(colum["Field"])

        while i < len(colums):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("Dialog_adddiet", l[i]))
            i = i + 1

        inf_x = l
        del inf_x[0]
        inf_x = str(inf_x)
        leng = len(inf_x)
        inf_x = inf_x[1:leng - 1]
        inf_x = inf_x.replace("'", "")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_addequipment = QtWidgets.QDialog()
    ui = Ui_Dialog_addequipment()
    ui.setupUi(Dialog_addequipment)
    Dialog_addequipment.show()
    sys.exit(app.exec_())
