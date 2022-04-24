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


class Ui_Dialog_client_order(object):
    def setupUi(self, Dialog_client_order):
        Dialog_client_order.setObjectName("Dialog_client_order")
        Dialog_client_order.resize(1141, 751)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_client_order)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 1141, 711))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_back = QtWidgets.QPushButton(Dialog_client_order)
        self.pushButton_back.setGeometry(QtCore.QRect(1050, 10, 75, 23))
        self.pushButton_back.setObjectName("pushButton_back")

        self.retranslateUi(Dialog_client_order)
        QtCore.QMetaObject.connectSlotsByName(Dialog_client_order)

    def retranslateUi(self, Dialog_client_order):
        _translate = QtCore.QCoreApplication.translate
        Dialog_client_order.setWindowTitle(_translate("Dialog_client_order", "Клиенты и кол-во их заказов"))
        self.pushButton_back.setText(_translate("Dialog_client_order", "Назад"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_diet", "Клиент"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_diet", "Кол-во заказов"))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            show_query = "SELECT * FROM `client` "
            cursor.execute(show_query)
            rows = cursor.fetchall()
            connection.commit()
        self.tableWidget.setRowCount(len(rows))

        tablerow = 0
        wr = len(rows)
        i = 0
        r = []

        for ro in rows:
            r.append(ro)

        k=0
        while i<wr:
            try:
                self.tableWidget.setItem(i, k, QtWidgets.QTableWidgetItem(str(r[i]["idclient"])))
                cursor = connection.cursor()
                with connection.cursor() as cursor:
                    show_query = "SELECT COUNT(*) as count FROM `order` WHERE idclient='%s'; " % (str(r[i]["idclient"]))
                    cursor.execute(show_query)
                    count = cursor.fetchall()
                    connection.commit()
                self.tableWidget.setItem(i, k+1, QtWidgets.QTableWidgetItem(str(count[0]["count"])))
                i = i + 1
            except Exception as ex:
                print(ex)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_client_order = QtWidgets.QDialog()
    ui = Ui_Dialog_client_order()
    ui.setupUi(Dialog_client_order)
    Dialog_client_order.show()
    sys.exit(app.exec_())
