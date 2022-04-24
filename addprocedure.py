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


class Ui_Dialog_addprocedure(object):
    def setupUi(self, Dialog_addprocedure):
        cursor = connection.cursor()
        with connection.cursor() as cursor:
            countmed = "SELECT * FROM `medicine` "
            cursor.execute(countmed)
            countmed = cursor.fetchall()
            countequip = "SELECT * FROM `equipment` "
            cursor.execute(countequip)
            countequip = cursor.fetchall()
            countd = "SELECT * FROM `diet` "
            cursor.execute(countd)
            countd = cursor.fetchall()
        countmed = len(countmed)
        countequip = len(countequip)
        countd = len(countd)



        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME='procedure';"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)
        count = count + 2
        Dialog_addprocedure.setObjectName("Dialog_addprocedure")
        Dialog_addprocedure.resize(1141, 709)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_addprocedure)
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
        self.comboBox_equip = QtWidgets.QComboBox(Dialog_addprocedure)
        self.comboBox_equip.setGeometry(QtCore.QRect(260, 115, 50, 22))
        self.comboBox_equip.setObjectName("comboBox_equip")
        i = 0
        while i < countequip:
            self.comboBox_equip.addItem("")
            i = i + 1
        self.comboBox_med = QtWidgets.QComboBox(Dialog_addprocedure)
        self.comboBox_med.setGeometry(QtCore.QRect(220, 75, 50, 22))
        self.comboBox_med.setObjectName("comboBox_med")
        i = 0
        while i < countmed:
            self.comboBox_med.addItem("")
            i = i + 1
        self.comboBox_diet = QtWidgets.QComboBox(Dialog_addprocedure)
        self.comboBox_diet.setGeometry(QtCore.QRect(185, 155, 50, 22))
        self.comboBox_diet.setObjectName("comboBox_diet")
        i = 0
        while i < countd:
            self.comboBox_diet.addItem("")
            i = i + 1
        self.label = QtWidgets.QLabel(Dialog_addprocedure)
        self.label.setGeometry(QtCore.QRect(20, 70, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(Dialog_addprocedure)
        self.label2.setGeometry(QtCore.QRect(20, 110, 240, 31))
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(Dialog_addprocedure)
        self.label3.setGeometry(QtCore.QRect(20, 150, 180, 31))
        self.label3.setFont(font)
        self.label3.setObjectName("label3")


        self.retranslateUi(Dialog_addprocedure)
        QtCore.QMetaObject.connectSlotsByName(Dialog_addprocedure)

    def retranslateUi(self, Dialog_addprocedure):
        _translate = QtCore.QCoreApplication.translate
        Dialog_addprocedure.setWindowTitle(_translate("Dialog_addprocedure", "Добавить"))
        self.label.setText("Выберите лекарство:")
        self.label2.setText("Выберите оборудование:")
        self.label3.setText("Выберите диету:")

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            countmed = "SELECT * FROM `medicine` "
            cursor.execute(countmed)
            rcountmed = cursor.fetchall()
            countequip = "SELECT * FROM `equipment` "
            cursor.execute(countequip)
            rcountequip = cursor.fetchall()
            countd = "SELECT * FROM `diet` "
            cursor.execute(countd)
            rcountd = cursor.fetchall()
        countmed = len(rcountmed)
        countequip = len(rcountequip)
        countd = len(rcountd)

        idmed = []
        idd = []
        idequip = []

        for med in rcountmed:
            idmed.append(med["idmedicine"])

        i = 0
        while i < countmed:
            self.comboBox_med.setItemText(i, _translate("Dialog_addprocedure", str(idmed[i])))
            i += 1

        for d in rcountd:
            idd.append(d["iddiet"])

        i = 0
        while i < countd:
            self.comboBox_diet.setItemText(i, _translate("Dialog_addprocedure", str(idd[i])))
            i += 1

        for equip in rcountequip:
            idequip.append(equip["idequipment"])

        i = 0
        while i < countequip:
            self.comboBox_equip.setItemText(i, _translate("Dialog_addprocedure", str(idequip[i])))
            i += 1



        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM `procedure`;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)
        count = count + 1
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnHidden(0, True)
        item = self.tableWidget.horizontalHeaderItem(count - 1)
        item.setText(_translate("Dialog_addprocedure", "Добавить"))
        item = self.tableWidget.horizontalHeaderItem(count)
        item.setText(_translate("Dialog_addprocedure", "Вернуться назад"))

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
                    insert_query = "INSERT INTO `procedure` (" + inf_x + ") VALUES (" + inf + ");"
                    print(insert_query)
                    cursor.execute(insert_query)
                    connection.commit()

                cursor = connection.cursor()
                with connection.cursor() as cursor:
                    insert_query_id = "SELECT idprocedure FROM `procedure` ORDER BY idprocedure DESC LIMIT 1"
                    cursor.execute(insert_query_id)
                    id_procedure = cursor.fetchall()
                    id_pr=[]
                    for id in id_procedure:
                        id_pr.append(id["idprocedure"])
                    insert_query = "INSERT INTO `proced` (idprocedure, idmedicine, idequipment, iddiet) VALUES ('%s', '%s', '%s', '%s');" % (id_pr[0], self.comboBox_med.currentText(), self.comboBox_equip.currentText(), self.comboBox_diet.currentText())
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
    Dialog_addprocedure = QtWidgets.QDialog()
    ui = Ui_Dialog_addprocedure()
    ui.setupUi(Dialog_addprocedure)
    Dialog_addprocedure.show()
    sys.exit(app.exec_())
