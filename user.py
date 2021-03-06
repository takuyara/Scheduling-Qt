# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
import sys

user_signal = 'abc'
class Ui_user(object):
    def setupUi(self, user):
        user.setObjectName("user")
        user.resize(1000, 600)
        user.setMinimumSize(QtCore.QSize(1000, 600))
        user.setMaximumSize(QtCore.QSize(1000, 600))
        self.UserMessage = QtWidgets.QLabel(user)
        self.UserMessage.setGeometry(QtCore.QRect(350, 40, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.UserMessage.setFont(font)
        self.UserMessage.setObjectName("UserMessage")
        self.IDLabel = QtWidgets.QLabel(user)
        self.IDLabel.setGeometry(QtCore.QRect(210, 150, 72, 15))
        self.IDLabel.setObjectName("IDLabel")
        self.NameEdit = QtWidgets.QLineEdit(user)
        self.NameEdit.setGeometry(QtCore.QRect(290, 210, 271, 41))
        self.NameEdit.setObjectName("NameEdit")
        self.NameLabel = QtWidgets.QLabel(user)
        self.NameLabel.setGeometry(QtCore.QRect(200, 220, 72, 15))
        self.NameLabel.setObjectName("NameLabel")
        self.PasswordEdit = QtWidgets.QLineEdit(user)
        self.PasswordEdit.setGeometry(QtCore.QRect(290, 420, 271, 41))
        self.PasswordEdit.setObjectName("PasswordEdit")
        self.GenderLabel = QtWidgets.QLabel(user)
        self.GenderLabel.setGeometry(QtCore.QRect(190, 290, 72, 15))
        self.GenderLabel.setObjectName("GenderLabel")
        self.GenderEdit = QtWidgets.QComboBox(user)
        self.GenderEdit.setGeometry(QtCore.QRect(290, 280, 101, 41))
        self.GenderEdit.setObjectName("GenderEdit")
        self.GenderEdit.addItem("")
        self.GenderEdit.addItem("")
        self.GradeLabel = QtWidgets.QLabel(user)
        self.GradeLabel.setGeometry(QtCore.QRect(190, 360, 72, 15))
        self.GradeLabel.setObjectName("GradeLabel")
        self.GradeEdit = QtWidgets.QComboBox(user)
        self.GradeEdit.setGeometry(QtCore.QRect(290, 350, 171, 41))
        self.GradeEdit.setObjectName("GradeEdit")
        self.GradeEdit.addItem("")
        self.GradeEdit.addItem("")
        self.GradeEdit.addItem("")
        self.GradeEdit.addItem("")
        self.PasswordLabel = QtWidgets.QLabel(user)
        self.PasswordLabel.setGeometry(QtCore.QRect(180, 430, 72, 15))
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.UserTypeLabel = QtWidgets.QLabel(user)
        self.UserTypeLabel.setGeometry(QtCore.QRect(180, 500, 72, 15))
        self.UserTypeLabel.setObjectName("UserTypeLabel")
        self.UserTypeEdit = QtWidgets.QComboBox(user)
        self.UserTypeEdit.setGeometry(QtCore.QRect(290, 490, 171, 41))
        self.UserTypeEdit.setObjectName("UserTypeEdit")
        self.UserTypeEdit.addItem("")
        self.UserTypeEdit.addItem("")
        self.NameTip = QtWidgets.QLabel(user)
        self.NameTip.setGeometry(QtCore.QRect(600, 220, 211, 16))
        self.NameTip.setObjectName("NameTip")
        self.PasswordTip = QtWidgets.QLabel(user)
        self.PasswordTip.setGeometry(QtCore.QRect(600, 430, 171, 16))
        self.PasswordTip.setObjectName("PasswordTip")
        self.IDMessage = QtWidgets.QTextBrowser(user)
        self.IDMessage.setGeometry(QtCore.QRect(290, 140, 271, 41))
        self.IDMessage.setObjectName("IDMessage")

        self.retranslateUi(user)
        QtCore.QMetaObject.connectSlotsByName(user)

        _translate = QtCore.QCoreApplication.translate
        self.IDMessage.setText(_translate("user", user_signal))

    def retranslateUi(self, user):
        _translate = QtCore.QCoreApplication.translate
        user.setWindowTitle(_translate("user", "Form"))
        self.UserMessage.setText(_translate("user", "????????????"))
        self.IDLabel.setText(_translate("user", "ID"))
        self.NameLabel.setText(_translate("user", "Name"))
        self.GenderLabel.setText(_translate("user", "Gender"))
        self.GenderEdit.setItemText(0, _translate("user", "male"))
        self.GenderEdit.setItemText(1, _translate("user", "female"))
        self.GradeLabel.setText(_translate("user", "Grade"))
        self.GradeEdit.setItemText(0, _translate("user", "ONE"))
        self.GradeEdit.setItemText(1, _translate("user", "TWO"))
        self.GradeEdit.setItemText(2, _translate("user", "THREE"))
        self.GradeEdit.setItemText(3, _translate("user", "FOUR"))
        self.PasswordLabel.setText(_translate("user", "Password"))
        self.UserTypeLabel.setText(_translate("user", "User Type"))
        self.UserTypeEdit.setItemText(0, _translate("user", "??????"))
        self.UserTypeEdit.setItemText(1, _translate("user", "??????"))
        self.NameTip.setText(_translate("user", "?????????0~12"))
        self.PasswordTip.setText(_translate("user", "?????????0~12"))

if __name__ == "__main__":
     app = QApplication(sys.argv)
     form = QtWidgets.QWidget()
     window = Ui_user()
     window.setupUi(form)
     form.show()
     sys.exit(app.exec_())