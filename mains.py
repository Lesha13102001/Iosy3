import subprocess
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from datetime import date, timedelta
from MainWindow import Ui_Dialog
from client import Ui_Dialog_client
from newcolum import Ui_Dialog_addcolum
from columdel import Ui_Dialog_deletecolum
from addclient import Ui_Dialog_add_client
from worker import Ui_Dialog_worker
from addworker import Ui_Dialog_addworker
from diagnos import Ui_Dialog_diagnoz
from adddiagnos import Ui_Dialog_adddiagnos
from room import Ui_Dialog_livingroom
from addroom import Ui_Dialog_addroom
from discount import Ui_Dialog_discount
from adddiscount import Ui_Dialog_adddiscount
from procedure import Ui_Dialog_procedure
from addprocedure import Ui_Dialog_addprocedure
from medicine import Ui_Dialog_medicine
from addmedicine import Ui_Dialog_addmedicine
from equipment import Ui_Dialog_equipment
from addequipment import Ui_Dialog_addequipment
from diet import Ui_Dialog_diet
from adddiet import Ui_Dialog_adddiet
from order import Ui_Dialog_order
from addordering import Ui_Dialog_Add_order
from order_rev import Ui_Dialog_order_date
from client_rev import Ui_Dialog_client_order
from client_worker import Ui_Dialog_client_worker

import People
from datetime import date, datetime

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

app = QtWidgets.QApplication(sys.argv)


Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

def OpenOtherWindow():
    global Dialog_client
    Dialog_client = QtWidgets.QDialog()
    ui = Ui_Dialog_client()
    ui.setupUi(Dialog_client)
    Dialog.close()
    Dialog_client.show()

    def NewColum():
        global Dialog_addcolum
        Dialog_addcolum = QtWidgets.QDialog()
        ui = Ui_Dialog_addcolum()
        ui.setupUi(Dialog_addcolum)
        Dialog_client.close()
        Dialog_addcolum.show()

        def AddColum():
            cursor = connection.cursor()
            with connection.cursor() as cursor:
                query = "ALTER TABLE `client` ADD COLUMN `"+ui.lineEdit.text()+"` "+ui.comboBox.currentText()
                print(query)
                cursor.execute(query)
                connection.commit()
            Dialog_addcolum.close()
            Dialog.show()

        ui.pushButton_addcolum.clicked.connect(AddColum)



        def returnToMain():
            Dialog_addcolum.close()
            Dialog.show()

        ui.pushButton.clicked.connect(returnToMain)

    ui.pushButton_add.clicked.connect(NewColum)


    def DeleteColum():
        global Dialog_deletecolum
        Dialog_deletecolum = QtWidgets.QDialog()
        ui = Ui_Dialog_deletecolum()
        ui.setupUi(Dialog_deletecolum)
        Dialog_deletecolum.show()
        Dialog_client.close()

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM client;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()

        i=1
        columsname=[]
        while i<len(colums):
            ui.comboBox_name.addItem("")
            i+=1

        for colum in colums:
            columsname.append(colum["Field"])

        i=1
        k=0
        while i<len(colums):
            ui.comboBox_name.setItemText(k,columsname[i])
            k+=1
            i+=1


        def DeleteColum():
            cursor = connection.cursor()
            with connection.cursor() as cursor:
                query = "ALTER TABLE `client` DROP COLUMN `"+ui.comboBox_name.currentText()+"` "
                cursor.execute(query)
                connection.commit()
            Dialog_deletecolum.close()
            Dialog.show()

        ui.pushButton_deletecolum.clicked.connect(DeleteColum)



        def returnToMain():
            Dialog_deletecolum.close()
            Dialog.show()



        ui.pushButton_back2.clicked.connect(returnToMain)



    ui.pushButton_delete.clicked.connect(DeleteColum)


    def NewClient():
        global Dialog_add_client
        Dialog_add_client = QtWidgets.QDialog()
        ui = Ui_Dialog_add_client()
        ui.setupUi(Dialog_add_client)
        Dialog_add_client.show()
        Dialog_client.close()



        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM client;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)


        def returnToMain():
            Dialog_add_client.close()
            Dialog.show()


        def returnToMain2():
            if ui.err==0:
                Dialog_add_client.close()
                Dialog.show()

        ui.tableWidget.cellWidget(0, count).clicked.connect(returnToMain2)

        ui.tableWidget.cellWidget(0, count+1).clicked.connect(returnToMain)




    ui.pushButton_add_client.clicked.connect(NewClient)


    def returnToMain():
        Dialog_client.close()
        Dialog.show()


    ui.pushButton_back.clicked.connect(returnToMain)




ui.client.clicked.connect(OpenOtherWindow)


def OpenWindowWorker():
    global Dialog_worker
    Dialog_worker = QtWidgets.QDialog()
    ui = Ui_Dialog_worker()
    ui.setupUi(Dialog_worker)
    Dialog_worker.show()
    Dialog.close()



    def AddWorker():
        global Dialog_addworker
        Dialog_addworker = QtWidgets.QDialog()
        ui = Ui_Dialog_addworker()
        ui.setupUi(Dialog_addworker)
        Dialog_addworker.show()
        Dialog_worker.close()

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM `worker`;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)

        def returnToMain():
            Dialog_addworker.close()
            Dialog.show()

        def returnToMain2():
            if ui.err==0:
                Dialog_addworker.close()
                Dialog.show()

        ui.tableWidget.cellWidget(0, count).clicked.connect(returnToMain2)

        ui.tableWidget.cellWidget(0, count + 1).clicked.connect(returnToMain)


    ui.pushButton_add_worker.clicked.connect(AddWorker)

    def returnToMain():
        Dialog_worker.close()
        Dialog.show()


    ui.pushButton_back.clicked.connect(returnToMain)


ui.worker.clicked.connect(OpenWindowWorker)



def OpenWindowDiagnos():
    global Dialog_diagnoz
    Dialog_diagnoz = QtWidgets.QDialog()
    ui = Ui_Dialog_diagnoz()
    ui.setupUi(Dialog_diagnoz)
    Dialog_diagnoz.show()
    Dialog.close()


    def AddDiagnoz():
        global Dialog_addworker
        Dialog_adddiagnos = QtWidgets.QDialog()
        ui = Ui_Dialog_adddiagnos()
        ui.setupUi(Dialog_adddiagnos)
        Dialog_adddiagnos.show()
        Dialog_diagnoz.close()

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM `diagnos`;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)

        def returnToMain():
            Dialog_adddiagnos.close()
            Dialog.show()

        def returnToMain2():
            if ui.err==0:
                Dialog_adddiagnos.close()
                Dialog.show()

        ui.tableWidget.cellWidget(0, count).clicked.connect(returnToMain2)

        ui.tableWidget.cellWidget(0, count + 1).clicked.connect(returnToMain)


    ui.pushButton_add_diagnoz.clicked.connect(AddDiagnoz)



    def returnToMain():
        Dialog_diagnoz.close()
        Dialog.show()


    ui.pushButton_back.clicked.connect(returnToMain)


ui.diagnos.clicked.connect(OpenWindowDiagnos)


def OpenWindowRoom():
    global Dialog_livingroom
    Dialog_livingroom = QtWidgets.QDialog()
    ui = Ui_Dialog_livingroom()
    ui.setupUi(Dialog_livingroom)
    Dialog_livingroom.show()
    Dialog.close()

    def AddRoom():
        global Dialog_addworker
        Dialog_addroom = QtWidgets.QDialog()
        ui = Ui_Dialog_addroom()
        ui.setupUi(Dialog_addroom)
        Dialog_addroom.show()
        Dialog_livingroom.close()

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM `livingroom`;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)

        def returnToMain():
            Dialog_addroom.close()
            Dialog.show()

        def returnToMain2():
            if ui.err==0:
                Dialog_addroom.close()
                Dialog.show()

        ui.tableWidget.cellWidget(0, count).clicked.connect(returnToMain2)

        ui.tableWidget.cellWidget(0, count + 1).clicked.connect(returnToMain)


    ui.pushButton_add_room.clicked.connect(AddRoom)


    def returnToMain():
        Dialog_livingroom.close()
        Dialog.show()


    ui.pushButton_back.clicked.connect(returnToMain)


ui.room.clicked.connect(OpenWindowRoom)


def OpenWindowDiscount():
    global Dialog_discount
    Dialog_discount = QtWidgets.QDialog()
    ui = Ui_Dialog_discount()
    ui.setupUi(Dialog_discount)
    Dialog_discount.show()
    Dialog.close()



    def AddDiscount():
        global Dialog_adddiscount
        Dialog_adddiscount = QtWidgets.QDialog()
        ui = Ui_Dialog_adddiscount()
        ui.setupUi(Dialog_adddiscount)
        Dialog_adddiscount.show()
        Dialog_discount.close()

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM `discount`;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)

        def returnToMain():
            Dialog_adddiscount.close()
            Dialog.show()

        def returnToMain2():
            if ui.err==0:
                Dialog_adddiscount.close()
                Dialog.show()

        ui.tableWidget.cellWidget(0, count).clicked.connect(returnToMain2)

        ui.tableWidget.cellWidget(0, count + 1).clicked.connect(returnToMain)


    ui.pushButton_add_discount.clicked.connect(AddDiscount)


    def returnToMain():
        Dialog_discount.close()
        Dialog.show()


    ui.pushButton_back.clicked.connect(returnToMain)


ui.discount.clicked.connect(OpenWindowDiscount)


def OpenWindowProcedure():
    global Dialog_procedure
    Dialog_procedure = QtWidgets.QDialog()
    ui = Ui_Dialog_procedure()
    ui.setupUi(Dialog_procedure)
    Dialog_procedure.show()
    Dialog.close()


    def AddProcedure():
        global Dialog_addprocedure
        Dialog_addprocedure = QtWidgets.QDialog()
        ui = Ui_Dialog_addprocedure()
        ui.setupUi(Dialog_addprocedure)
        Dialog_addprocedure.show()
        Dialog_procedure.close()

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM `procedure`;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)

        def returnToMain():
            Dialog_addprocedure.close()
            Dialog.show()

        def returnToMain2():
            if ui.err==0:
                Dialog_addprocedure.close()
                Dialog.show()

        ui.tableWidget.cellWidget(0, count).clicked.connect(returnToMain2)

        ui.tableWidget.cellWidget(0, count + 1).clicked.connect(returnToMain)


    ui.pushButton_add_procedure.clicked.connect(AddProcedure)



    def returnToMain():
        Dialog_procedure.close()
        Dialog.show()


    ui.pushButton_back.clicked.connect(returnToMain)

ui.procedure.clicked.connect(OpenWindowProcedure)



def OpenWindowMedicine():
    global Dialog_medicine
    Dialog_medicine = QtWidgets.QDialog()
    ui = Ui_Dialog_medicine()
    ui.setupUi(Dialog_medicine)
    Dialog_medicine.show()
    Dialog.close()


    def AddMedicine():
        global Dialog_addmedicine
        Dialog_addmedicine = QtWidgets.QDialog()
        ui = Ui_Dialog_addmedicine()
        ui.setupUi(Dialog_addmedicine)
        Dialog_addmedicine.show()
        Dialog_medicine.close()

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM `medicine`;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)

        def returnToMain():
            Dialog_addmedicine.close()
            Dialog.show()

        def returnToMain2():
            if ui.err==0:
                Dialog_addmedicine.close()
                Dialog.show()

        ui.tableWidget.cellWidget(0, count).clicked.connect(returnToMain2)

        ui.tableWidget.cellWidget(0, count + 1).clicked.connect(returnToMain)


    ui.pushButton_add_medicine.clicked.connect(AddMedicine)


    def returnToMain():
        Dialog_medicine.close()
        Dialog.show()


    ui.pushButton_back.clicked.connect(returnToMain)

ui.medicine.clicked.connect(OpenWindowMedicine)



def OpenWindowEquipment():
    global Dialog_equipment
    Dialog_equipment = QtWidgets.QDialog()
    ui = Ui_Dialog_equipment()
    ui.setupUi(Dialog_equipment)
    Dialog_equipment.show()
    Dialog.close()


    def AddEquipment():
        global Dialog_addequipment
        Dialog_addequipment = QtWidgets.QDialog()
        ui = Ui_Dialog_addequipment()
        ui.setupUi(Dialog_addequipment)
        Dialog_addequipment.show()
        Dialog_equipment.close()

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM `equipment`;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)

        def returnToMain():
            Dialog_addequipment.close()
            Dialog.show()

        def returnToMain2():
            if ui.err==0:
                Dialog_addequipment.close()
                Dialog.show()

        ui.tableWidget.cellWidget(0, count).clicked.connect(returnToMain2)

        ui.tableWidget.cellWidget(0, count + 1).clicked.connect(returnToMain)


    ui.pushButton_add_equipment.clicked.connect(AddEquipment)


    def returnToMain():
        Dialog_equipment.close()
        Dialog.show()


    ui.pushButton_back.clicked.connect(returnToMain)


ui.equipment.clicked.connect(OpenWindowEquipment)


def OpenWindowDiet():
    global Dialog_diet
    Dialog_diet = QtWidgets.QDialog()
    ui = Ui_Dialog_diet()
    ui.setupUi(Dialog_diet)
    Dialog_diet.show()
    Dialog.close()



    def AddDiet():
        global Dialog_adddiet
        Dialog_adddiet = QtWidgets.QDialog()
        ui = Ui_Dialog_adddiet()
        ui.setupUi(Dialog_adddiet)
        Dialog_adddiet.show()
        Dialog_diet.close()

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            count = "SHOW COLUMNS FROM `diet`;"
            cursor.execute(count)
            colums = cursor.fetchall()
            connection.commit()
        count = len(colums)

        def returnToMain():
            Dialog_adddiet.close()
            Dialog.show()

        def returnToMain2():
            if ui.err==0:
                Dialog_adddiet.close()
                Dialog.show()

        ui.tableWidget.cellWidget(0, count).clicked.connect(returnToMain2)

        ui.tableWidget.cellWidget(0, count + 1).clicked.connect(returnToMain)


    ui.pushButton_add_diet.clicked.connect(AddDiet)



    def returnToMain():
        Dialog_diet.close()
        Dialog.show()


    ui.pushButton_back.clicked.connect(returnToMain)


ui.diet.clicked.connect(OpenWindowDiet)


def OpenWindowAddOrder():
    global Dialog_Add_order
    Dialog_Add_order = QtWidgets.QDialog()
    ui = Ui_Dialog_Add_order()
    ui.setupUi(Dialog_Add_order)
    Dialog_Add_order.show()
    Dialog.close()

    def AddOr():
        if datetime.strptime(str(ui.dateEdit_st.text()), "%Y-%m-%d") < datetime.today()-timedelta(days=1):
            add = QMessageBox()
            add.setWindowTitle("Ошибка")
            add.setText("Дата приезда не может быть позже текущей даты")
            add.setStandardButtons(QMessageBox.Ok)
            add.exec_()
            return
        else:
            if datetime.strptime(str(ui.dateEdit_end.text()), "%Y-%m-%d") < datetime.strptime(str(ui.dateEdit_st.text()), "%Y-%m-%d"):
                add = QMessageBox()
                add.setWindowTitle("Ошибка")
                add.setText("Дата отъезда не может быть раньше даты приезда")
                add.setStandardButtons(QMessageBox.Ok)
                add.exec_()
                return
            else:
                q=datetime.strptime(str(ui.dateEdit_end.text()), "%Y-%m-%d")-datetime.strptime(str(ui.dateEdit_st.text()), "%Y-%m-%d")
                if q.days<5:
                    add = QMessageBox()
                    add.setWindowTitle("Ошибка")
                    add.setText("Длительность путевки должна быть не меньше 5 дней")
                    add.setStandardButtons(QMessageBox.Ok)
                    add.exec_()
                    return

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            show_query = "SELECT * FROM `order` "
            cursor.execute(show_query)
            orders = cursor.fetchall()
            connection.commit()

        for order in orders:
            print(ui.comboBox_client.currentText())
            if str(ui.comboBox_client.currentText()) == str(order["idclient"]):
                print("idCl=BdCl")
                if datetime.strptime(str(ui.dateEdit_st.text()), "%Y-%m-%d") < datetime.strptime(str(order["datest"]),"%Y-%m-%d") and datetime.strptime(str(ui.dateEdit_end.text()), "%Y-%m-%d") < datetime.strptime(str(order["datest"]), "%Y-%m-%d"):
                    print("continue1")
                    continue
                else:
                    if datetime.strptime(str(ui.dateEdit_st.text()), "%Y-%m-%d") > datetime.strptime(str(order["dateend"]), "%Y-%m-%d"):
                        print("continue2")
                        continue
                    else:
                        add = QMessageBox()
                        add.setWindowTitle("Ошибка")
                        add.setText("Интервал дат оформляемого заказа не может совподать с интервалами дат его предыдующих заказов")
                        add.setStandardButtons(QMessageBox.Ok)
                        add.exec_()
                        return

        disc=0
        for order in orders:
            if str(ui.comboBox_discount.currentText()) == str(order["iddiscount"]):
                disc=disc+1

        print(disc)

        if disc>0:
            cursor = connection.cursor()
            with connection.cursor() as cursor:
                show_query = "SELECT * FROM `discount` "
                cursor.execute(show_query)
                discounts = cursor.fetchall()
                connection.commit()

            for discount in discounts:
                if str(ui.comboBox_discount.currentText()) == str(discount["iddiscount"]):
                    if int(str(discount["percent"])) + 5 < 36:
                        cursor = connection.cursor()
                        with connection.cursor() as cursor:
                            update_query = "UPDATE `discount` SET percent = '%s' WHERE iddiscount= '%s';" % (str(int(str(discount["percent"])) + 5), ui.comboBox_discount.currentText())
                            cursor.execute(update_query)
                            connection.commit()

        cursor = connection.cursor()
        with connection.cursor() as cursor:
            insert_query = "INSERT INTO `order` (idclient, datest, dateend, iddiagnos, idlivingroom, idworker, idprocedure, iddiscount) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (
            ui.comboBox_client.currentText(), str(ui.dateEdit_st.text()), str(ui.dateEdit_end.text()),
            ui.comboBox_diagnos.currentText(), ui.comboBox_room.currentText(), ui.comboBox_worker.currentText(),
            ui.comboBox_procedure.currentText(), ui.comboBox_discount.currentText())
            print(insert_query)
            cursor.execute(insert_query)
            connection.commit()
        Dialog_Add_order.close()
        Dialog.show()

    ui.pushButton_add_order.clicked.connect(AddOr)

    def returnToMain():
        Dialog_Add_order.close()
        Dialog.show()


    ui.pushButton_back.clicked.connect(returnToMain)

ui.new_order.clicked.connect(OpenWindowAddOrder)


def OpenWindowOrder():
    global Dialog_order
    Dialog_order = QtWidgets.QDialog()
    ui = Ui_Dialog_order()
    ui.setupUi(Dialog_order)
    Dialog_order.show()
    Dialog.close()



    def returnToMain():
        Dialog_order.close()
        Dialog.show()


    ui.pushButton_back.clicked.connect(returnToMain)


ui.order.clicked.connect(OpenWindowOrder)

def OpenWindowOrderRev():
    global Dialog_order_date
    Dialog_order_date = QtWidgets.QDialog()
    ui = Ui_Dialog_order_date()
    ui.setupUi(Dialog_order_date)
    Dialog_order_date.show()
    Dialog.close()


    def returnToMain():
        Dialog_order_date.close()
        Dialog.show()


    ui.pushButton_back.clicked.connect(returnToMain)



ui.order_rev.clicked.connect(OpenWindowOrderRev)



def OpenWindowClientRev():
    global Dialog_client_order
    Dialog_client_order = QtWidgets.QDialog()
    ui = Ui_Dialog_client_order()
    ui.setupUi(Dialog_client_order)
    Dialog_client_order.show()
    Dialog.close()


    def returnToMain():
        Dialog_client_order.close()
        Dialog.show()


    ui.pushButton_back.clicked.connect(returnToMain)


ui.client_rev.clicked.connect(OpenWindowClientRev)


def OpenWindowClientWorker():
    global Dialog_client_worker
    Dialog_client_worker = QtWidgets.QDialog()
    ui = Ui_Dialog_client_worker()
    ui.setupUi(Dialog_client_worker)
    Dialog_client_worker.show()
    Dialog.close()

    def returnToMain():
        Dialog_client_worker.close()
        Dialog.show()


    ui.pushButton_back.clicked.connect(returnToMain)


ui.client_worker.clicked.connect(OpenWindowClientWorker)


sys.exit(app.exec_())