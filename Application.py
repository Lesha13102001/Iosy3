import sys
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets

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

class Ui_Dialog_application(object):
    def setupUi(self, Dialog_application):
        Dialog_application.setObjectName("Dialog_application")
        Dialog_application.resize(1317, 823)
        self.pushButton_backtoadmin = QtWidgets.QPushButton(Dialog_application)
        self.pushButton_backtoadmin.setGeometry(QtCore.QRect(1110, 20, 191, 41))
        self.pushButton_backtoadmin.setObjectName("pushButton_backtoadmin")
        self.tableWidget = QtWidgets.QTableWidget(Dialog_application)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 1291, 731))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.label = QtWidgets.QLabel(Dialog_application)
        self.label.setGeometry(QtCore.QRect(450, 20, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_application)
        QtCore.QMetaObject.connectSlotsByName(Dialog_application)

        self.loaddata()



    def retranslateUi(self, Dialog_application):
        _translate = QtCore.QCoreApplication.translate
        Dialog_application.setWindowTitle(_translate("Dialog_application", "Заявки"))
        self.pushButton_backtoadmin.setText(_translate("Dialog_application", "Назад"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_application", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_application", "Имя"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_application", "Фамилия"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog_application", "Отчество"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog_application", "Год рождения"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog_application", "Номер телефона"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog_application", "Дата заезда"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog_application", "Дата отъезда"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog_application", "Диагноз"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Dialog_application", "Оздоровительная программа"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Dialog_application", "Кнопка"))
        self.label.setText(_translate("Dialog_application", "Заявки в санаторий"))

        self.tableWidget.setColumnWidth(0, 1)
        self.tableWidget.setColumnWidth(1, 80)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 120)
        self.tableWidget.setColumnWidth(4, 85)
        self.tableWidget.setColumnWidth(6, 80)
        self.tableWidget.setColumnWidth(7, 80)
        self.tableWidget.setColumnWidth(8, 210)
        self.tableWidget.setColumnWidth(9, 270)


    def loaddata(self):
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            show_query = "SELECT * FROM `usr_app` "
            cursor.execute(show_query)
            rows=cursor.fetchall()
            connection.commit()
            self.tableWidget.setRowCount(len(rows))
            tablerow = 0
            button_name="button"
            button={}
            def Lets():
                numb_row=self.tableWidget.currentRow()
                ID=self.tableWidget.item(numb_row,0)
                Name=self.tableWidget.item(numb_row,1)
                Surname = self.tableWidget.item(numb_row, 2)
                Patronymic = self.tableWidget.item(numb_row, 3)
                Age = self.tableWidget.item(numb_row, 4)
                Tel = self.tableWidget.item(numb_row, 5)
                Date_st = self.tableWidget.item(numb_row, 6)
                Date_end = self.tableWidget.item(numb_row, 7)
                Diagn = self.tableWidget.item(numb_row, 8)
                Prog = self.tableWidget.item(numb_row, 9)

                cursor = connection.cursor()
                with connection.cursor() as cursor:
                    insert_query = "INSERT INTO `users` (name, surname, patronymic, age, telephone, data_st, data_end, diagnoz, programma) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (Name.text(), Surname.text(), Patronymic.text(), Age.text(), Tel.text(), Date_st.text(), Date_end.text(), Diagn.text(), Prog.text())
                    delete_query = "DELETE FROM `usr_app` WHERE idusr = %s" % (ID.text())
                    cursor.execute(insert_query)
                    cursor.execute(delete_query)
                    connection.commit()
                button_deactivate=button_name+str(numb_row)
                button[button_deactivate].setEnabled(False)
                self.tableWidget.setRowHidden(numb_row, True)

            for row in rows:
                button_name2=button_name+str(tablerow)
                button[button_name2] = QtWidgets.QPushButton()
                button[button_name2].setText("Принять")
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row["idusr"])))
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row["name"]))
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row["surname"]))
                self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row["patronymic"]))
                self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row["age"])))
                self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row["telephone"]))
                self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row["data_st"])))
                self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row["data_end"])))
                self.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row["diagnoz"]))
                self.tableWidget.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(row["programma"]))
                self.tableWidget.setCellWidget(tablerow, 10, button[button_name2])
                button[button_name2].clicked.connect(Lets)
                tablerow+=1

            self.tableWidget.setColumnHidden(0, True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_application = QtWidgets.QDialog()
    ui = Ui_Dialog_application()
    ui.setupUi(Dialog_application)
    Dialog_application.show()
    sys.exit(app.exec_())
