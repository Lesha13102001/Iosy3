import pymysql
from Config import host, user, password, db_name
from PyQt5 import QtCore, QtGui, QtWidgets

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



class Ui_Dialog_people(object):
    def setupUi(self, Dialog_people):
        Dialog_people.setObjectName("Dialog_people")
        Dialog_people.resize(1317, 823)
        self.pushButton_backadmin = QtWidgets.QPushButton(Dialog_people)
        self.pushButton_backadmin.setGeometry(QtCore.QRect(1110, 20, 191, 41))
        self.pushButton_backadmin.setObjectName("pushButton_backadmin")
        self.tableWidget_people = QtWidgets.QTableWidget(Dialog_people)
        self.tableWidget_people.setGeometry(QtCore.QRect(10, 80, 1291, 731))
        self.tableWidget_people.setObjectName("tableWidget_people")
        self.tableWidget_people.setColumnCount(9)
        self.tableWidget_people.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_people.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_people.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_people.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_people.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_people.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_people.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_people.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_people.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_people.setHorizontalHeaderItem(8, item)
        self.label = QtWidgets.QLabel(Dialog_people)
        self.label.setGeometry(QtCore.QRect(510, 20, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_people)
        QtCore.QMetaObject.connectSlotsByName(Dialog_people)

        self.loaddata()

    def retranslateUi(self, Dialog_people):
        _translate = QtCore.QCoreApplication.translate
        Dialog_people.setWindowTitle(_translate("Dialog_people", "Отдыхающие"))
        self.pushButton_backadmin.setText(_translate("Dialog_people", "Назад"))
        item = self.tableWidget_people.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_people", "Имя"))
        item = self.tableWidget_people.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_people", "Фамилия"))
        item = self.tableWidget_people.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_people", "Отчество"))
        item = self.tableWidget_people.horizontalHeaderItem(3)
        item.setText(_translate("Dialog_people", "Год рождения"))
        item = self.tableWidget_people.horizontalHeaderItem(4)
        item.setText(_translate("Dialog_people", "Номер телефона"))
        item = self.tableWidget_people.horizontalHeaderItem(5)
        item.setText(_translate("Dialog_people", "Дата заезда"))
        item = self.tableWidget_people.horizontalHeaderItem(6)
        item.setText(_translate("Dialog_people", "Дата отъезда"))
        item = self.tableWidget_people.horizontalHeaderItem(7)
        item.setText(_translate("Dialog_people", "Диагноз"))
        item = self.tableWidget_people.horizontalHeaderItem(8)
        item.setText(_translate("Dialog_people", "Оздоровительная программа"))
        self.label.setText(_translate("Dialog_people", "Отдыхающие"))

        self.tableWidget_people.setColumnWidth(0, 100)
        self.tableWidget_people.setColumnWidth(1, 100)
        self.tableWidget_people.setColumnWidth(2, 100)
        self.tableWidget_people.setColumnWidth(3, 120)
        self.tableWidget_people.setColumnWidth(4, 150)
        self.tableWidget_people.setColumnWidth(5, 80)
        self.tableWidget_people.setColumnWidth(6, 80)
        self.tableWidget_people.setColumnWidth(7, 250)
        self.tableWidget_people.setColumnWidth(8, 300)
        self.tableWidget_people.setColumnWidth(9, 300)
        self.tableWidget_people.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


    def loaddata(self):
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            show_query = "SELECT * FROM `users`"
            cursor.execute(show_query)
            rows=cursor.fetchall()
            connection.commit()
            print(rows)
            self.tableWidget_people.setRowCount(len(rows))
            tablerow = 0
            for row in rows:
                self.tableWidget_people.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row["name"]))
                self.tableWidget_people.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row["surname"]))
                self.tableWidget_people.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row["patronymic"]))
                self.tableWidget_people.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row["age"])))
                self.tableWidget_people.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row["telephone"]))
                self.tableWidget_people.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row["data_st"])))
                self.tableWidget_people.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row["data_end"])))
                self.tableWidget_people.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row["diagnoz"]))
                self.tableWidget_people.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row["programma"]))
                tablerow+=1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_people = QtWidgets.QDialog()
    ui = Ui_Dialog_people()
    ui.setupUi(Dialog_people)
    Dialog_people.show()
    sys.exit(app.exec_())
