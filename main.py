import subprocess
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Sanat import Ui_Dialog
from AdVx import Ui_Admin
from Admin import Ui_Dialog_Admin
from Application import  Ui_Dialog_application
from People import Ui_Dialog_people
import People

app = QtWidgets.QApplication(sys.argv)


Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


def OpenOtherWindow():
    global Admin
    Admin = QtWidgets.QDialog()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Dialog.close()
    Admin.show()

    def GoToAdmin(Text):
        if (Text=="123"):
            global Dialog_Admin
            Dialog_Admin = QtWidgets.QDialog()
            ui = Ui_Dialog_Admin()
            ui.setupUi(Dialog_Admin)
            Admin.close()
            Dialog_Admin.show()

            def returnMain():
                Dialog_Admin.close()
                Dialog.show()


            def GoToApplication():
                global Dialog_application
                Dialog_application = QtWidgets.QDialog()
                ui = Ui_Dialog_application()
                ui.setupUi(Dialog_application)
                Dialog_Admin.close()
                Dialog_application.update()
                Dialog_application.show()


                def returnToAdmin():
                    Dialog_application.close()
                    Dialog_application.update()
                    Dialog_Admin.show()

                ui.pushButton_backtoadmin.clicked.connect(returnToAdmin)

            def GoToPeople():
                global Dialog_people
                Dialog_people = QtWidgets.QDialog()
                ui = Ui_Dialog_people()
                ui.setupUi(Dialog_people)
                Dialog_Admin.close()
                Dialog_people.show()

                def ret():
                    Dialog_people.close()
                    Dialog_Admin.show()

                ui.pushButton_backadmin.clicked.connect(ret)


            ui.pushButton_people.clicked.connect(GoToPeople)
            ui.pushButton_go_to_main.clicked.connect(returnMain)
            ui.pushButton_app.clicked.connect(GoToApplication)



        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Неверный пароль")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

    ui.pushButton_admin_go.clicked.connect(lambda: GoToAdmin(ui.lineEdit_admin.text()))




    def returnToMain():
        Admin.close()
        Dialog.show()


    ui.pushButton_admin_back.clicked.connect(returnToMain)





ui.pushButton_admin.clicked.connect(OpenOtherWindow)



sys.exit(app.exec_())