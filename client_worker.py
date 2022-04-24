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


class Ui_Dialog_client_worker(object):
    def setupUi(self, Dialog_client_worker):
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME='client';"
            cursor.execute(count)
            columscl = cursor.fetchall()
            count = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME='worker';"
            cursor.execute(count)
            columsw = cursor.fetchall()
            connection.commit()
        countcl = len(columscl)
        countw = len(columsw)
        global allx
        allx=countcl+countw


        Dialog_client_worker.setObjectName("Dialog_client_worker")
        Dialog_client_worker.resize(1141, 751)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_client_worker)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 1141, 711))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(countw+countcl)
        self.tableWidget.setRowCount(0)
        i = 0
        while i < countw+countcl:
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            i = i + 1
        self.pushButton_back = QtWidgets.QPushButton(Dialog_client_worker)
        self.pushButton_back.setGeometry(QtCore.QRect(1050, 10, 75, 23))
        self.pushButton_back.setObjectName("pushButton_back")

        self.retranslateUi(Dialog_client_worker)
        QtCore.QMetaObject.connectSlotsByName(Dialog_client_worker)

    def retranslateUi(self, Dialog_client_worker):
        _translate = QtCore.QCoreApplication.translate
        Dialog_client_worker.setWindowTitle(_translate("Dialog_client_worker", "Общий список клиентов и врачей"))
        self.pushButton_back.setText(_translate("Dialog_client_worker", "Назад"))

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM client;"
            cursor.execute(count)
            columscl = cursor.fetchall()
            connection.commit()
        countcl = len(columscl)

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM `worker`;"
            cursor.execute(count)
            columsw = cursor.fetchall()
            connection.commit()
        countw = len(columsw)

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            show_query = "SELECT * FROM `client` LEFT JOIN `worker` ON idclient=idworker"+" UNION "+" SELECT * FROM `client` RIGHT JOIN `worker` ON idclient=idworker"
            cursor.execute(show_query)
            rows = cursor.fetchall()
            connection.commit()
            self.tableWidget.setRowCount(len(rows))
            tablerow = 0
            wr = countcl+countw
            i = 0
            cl = []
            w = []
            r = []
            typcl = []
            typw = []

            for ro in rows:
                r.append(ro)



            for cle in columscl:
                cl.append(cle["Field"])

            for wo in columsw:
                w.append(wo["Field"])

            for typecl in columscl:
                typcl.append(typecl["Type"])

            for typew in columsw:
                typw.append(typew["Type"])


            cl=cl+w
            print(cl)
            typ = typcl+typw


            while i < countcl:
                item = self.tableWidget.horizontalHeaderItem(i)
                item.setText(_translate("Dialog_diet", cl[i]))
                i = i + 1

            i=countcl
            l=0
            while i < countcl+countw:
                item = self.tableWidget.horizontalHeaderItem(i)
                item.setText(_translate("Dialog_diet", w[l]))
                i = i + 1
                l=l+1


            try:
                for row in rows:
                    k = 0
                    while k < wr:
                        if str(row[cl[k]])=="None":
                            self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(""))
                        else:
                            if k == 0:
                                self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(str(row[cl[k]])))
                            else:
                                if typ[k] == "date":
                                    self.tableWidget.setItem(tablerow, k, QtWidgets.QTableWidgetItem(str(row[cl[k]])))
                                else:
                                    if typ[k] == "int" or typ[k] == "int unsigned":
                                        self.tableWidget.setItem(tablerow, k,
                                                                 QtWidgets.QTableWidgetItem(str(row[cl[k]])))
                                    else:
                                        if typ[k] == "decimal(10,0)":
                                            self.tableWidget.setItem(tablerow, k,
                                                                     QtWidgets.QTableWidgetItem(str(row[cl[k]])))
                                        else:
                                            self.tableWidget.setItem(tablerow, k,QtWidgets.QTableWidgetItem(row[cl[k]]))
                        k = k + 1
                    tablerow += 1
            except Exception as ex:
                print(ex)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_client_worker = QtWidgets.QDialog()
    ui = Ui_Dialog_client_worker()
    ui.setupUi(Dialog_client_worker)
    Dialog_client_worker.show()
    sys.exit(app.exec_())
