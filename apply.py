# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apply.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import psycopg2
import datetime

nowtime = datetime.datetime.now()

apply_signal = 'abc'
class Ui_apply(object):
    def setupUi(self, apply):
        apply.setObjectName("apply")
        apply.resize(1000, 600)
        apply.setMinimumSize(QtCore.QSize(1000, 600))
        apply.setMaximumSize(QtCore.QSize(1000, 600))
        self.MainLabel = QtWidgets.QLabel(apply)
        self.MainLabel.setGeometry(QtCore.QRect(400, 20, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.MainLabel.setFont(font)
        self.MainLabel.setObjectName("MainLabel")
        self.NameLabel = QtWidgets.QLabel(apply)
        self.NameLabel.setGeometry(QtCore.QRect(150, 110, 72, 15))
        self.NameLabel.setObjectName("NameLabel")
        self.NameEdit = QtWidgets.QLineEdit(apply)
        self.NameEdit.setGeometry(QtCore.QRect(250, 100, 441, 41))
        self.NameEdit.setObjectName("NameEdit")
        self.NameTip = QtWidgets.QLabel(apply)
        self.NameTip.setGeometry(QtCore.QRect(720, 110, 101, 16))
        self.NameTip.setObjectName("NameTip")
        self.PlaceLabel = QtWidgets.QLabel(apply)
        self.PlaceLabel.setGeometry(QtCore.QRect(150, 180, 72, 15))
        self.PlaceLabel.setObjectName("PlaceLabel")
        self.StartDate = QtWidgets.QDateTimeEdit(apply)
        self.StartDate.setGeometry(QtCore.QRect(250, 230, 181, 21))
        self.StartDate.setObjectName("StartDate")
        self.StartDate.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.StartLabel = QtWidgets.QLabel(apply)
        self.StartLabel.setGeometry(QtCore.QRect(150, 230, 72, 15))
        self.StartLabel.setObjectName("StartLabel")
        self.EndDate = QtWidgets.QDateTimeEdit(apply)
        self.EndDate.setGeometry(QtCore.QRect(250, 280, 194, 22))
        self.EndDate.setObjectName("EndDate")
        self.EndDate.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.EndLabel = QtWidgets.QLabel(apply)
        self.EndLabel.setGeometry(QtCore.QRect(150, 280, 72, 15))
        self.EndLabel.setObjectName("EndLabel")
        self.CapacityLabel = QtWidgets.QLabel(apply)
        self.CapacityLabel.setGeometry(QtCore.QRect(150, 340, 72, 15))
        self.CapacityLabel.setObjectName("CapacityLabel")
        self.CapacityEdit = QtWidgets.QLineEdit(apply)
        self.CapacityEdit.setGeometry(QtCore.QRect(250, 330, 191, 41))
        self.CapacityEdit.setObjectName("CapacityEdit")
        self.ApplyButton = QtWidgets.QPushButton(apply)
        self.ApplyButton.setGeometry(QtCore.QRect(410, 480, 151, 51))
        self.ApplyButton.setObjectName("ApplyButton")
        self.PlaceComboBox = QtWidgets.QComboBox(apply)
        self.PlaceComboBox.setGeometry(QtCore.QRect(250, 170, 441, 41))
        self.PlaceComboBox.setObjectName("PlaceComboBox")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.CapacityTip = QtWidgets.QLabel(apply)
        self.CapacityTip.setGeometry(QtCore.QRect(480, 340, 231, 16))
        self.CapacityTip.setObjectName("CapacityTip")
        self.StudentLabel = QtWidgets.QLabel(apply)
        self.StudentLabel.setGeometry(QtCore.QRect(150, 400, 72, 15))
        self.StudentLabel.setObjectName("StudentLabel")
        self.StudentMessage = QtWidgets.QTextBrowser(apply)
        self.StudentMessage.setGeometry(QtCore.QRect(250, 390, 341, 41))
        self.StudentMessage.setObjectName("StudentMessage")
        self.Feedback = QtWidgets.QTextBrowser(apply)
        self.Feedback.setGeometry(QtCore.QRect(720, 230, 256, 192))
        self.Feedback.setObjectName("Feedback")

        self.retranslateUi(apply)
        QtCore.QMetaObject.connectSlotsByName(apply)

        _translate = QtCore.QCoreApplication.translate
        self.StudentMessage.setText(_translate("user", apply_signal))

        # ????????????????????????????????????
        self.NameEdit.setClearButtonEnabled(True)

        # ???????????????????????????????????????display??????
        self.ApplyButton.clicked.connect(self.ApplyNew)

    def ApplyNew(self):
        newname = self.NameEdit.text()
        newplace = self.PlaceComboBox.currentText()
        newcapacity = self.CapacityEdit.text()
        newstudent = self.StudentMessage.toPlainText()
        newstarttime = self.StartDate.dateTime()
        newendtime = self.EndDate.dateTime()
        numbers = int(newcapacity)

        if newname == "" or newcapacity == "":
            self.Feedback.setText("??????????????????????????????????????????")
            return

        elif len(newname) >= 19:
            self.Feedback.setText("???????????????????????????????????????????????????")
            return

        elif newstarttime <= nowtime or newstarttime >= newendtime:
            print(newstarttime, newendtime)
            self.Feedback.setText("???????????????????????????????????????")
            return

        try:
            conn = psycopg2.connect(
                user='postgres',
                password='patrick+',
                host='127.0.0.1',
                database='postgres',
                port=5432
            )
            cursor = conn.cursor()
            query1 = "SELECT ROO_ID, ROO_CAPACITY FROM ROOM"
            cursor.execute(query1)
            for row in cursor:
                if row[0] == newplace:
                    print(row[0], row[1])
                    if row[1] < numbers:
                        print("yy")
                        # ??????text Browser????????????setText()????????????????????????
                        self.Feedback.setText("???????????????????????????????????????????????????")
                        return

            query2 = "SELECT ACT_STARTTIME, ACT_ENDTIME, ROO_ID, STU_ID FROM ACTIVITY"
            cursor.execute(query2)
            for row in cursor:
                if row[2] == newplace or row[3] ==newstudent :
                    if row[0] <= newstarttime <= row[1] or row[0] <= newendtime <= row[1]:
                        # ??????text Browser????????????setText()????????????????????????
                        self.Feedback.setText("???????????????????????????????????????")
                        return

            tempstart = self.StartDate.dateTime().toString("yyyy-MM-dd HH:mm:ss")
            tempend = self.EndDate.dateTime().toString("yyyy-MM-dd HH:mm:ss")
            query3 = "INSERT INTO ACTIVITY (ACT_NAME, STU_ID, ACT_STARTTIME, ACT_ENDTIME, ROO_ID, ACT_CAPACITY, CURRENTNUM) VALUES (%s, %s, %s, %s, %s, %s, 0)"
            cursor.execute(query3, (newname, newstudent, tempstart, tempend, newplace, numbers))
            conn.commit()
            self.Feedback.setText("???????????????")
            return
        except psycopg2.Error as err:
            print(err)
        else:
            conn.close()


    def retranslateUi(self, apply):
        _translate = QtCore.QCoreApplication.translate
        apply.setWindowTitle(_translate("apply", "????????????"))
        self.MainLabel.setText(_translate("apply", "????????????"))
        self.NameLabel.setText(_translate("apply", "????????????"))
        self.NameTip.setText(_translate("apply", "?????????0~18"))
        self.PlaceLabel.setText(_translate("apply", "????????????"))
        self.StartLabel.setText(_translate("apply", "????????????"))
        self.EndLabel.setText(_translate("apply", "????????????"))
        self.CapacityLabel.setText(_translate("apply", "????????????"))
        self.ApplyButton.setText(_translate("apply", "??????"))
        self.PlaceComboBox.setItemText(0, _translate("apply", "101"))
        self.PlaceComboBox.setItemText(1, _translate("apply", "202"))
        self.PlaceComboBox.setItemText(2, _translate("apply", "3103"))
        self.PlaceComboBox.setItemText(3, _translate("apply", "4404"))
        self.PlaceComboBox.setItemText(4, _translate("apply", "5105"))
        self.PlaceComboBox.setItemText(5, _translate("apply", "6A013"))
        self.CapacityTip.setText(_translate("apply", "????????????????????????????????????"))
        self.StudentLabel.setText(_translate("apply", "?????????"))

if __name__ == "__main__":
     app = QApplication(sys.argv)
     form = QtWidgets.QWidget()
     window = Ui_apply()
     window.setupUi(form)
     form.show()
     sys.exit(app.exec_())