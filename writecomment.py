# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'writecomment.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class rres:
    def __init__(self):
        self.s1 = ""
        self.s2 = ""
    def set(self, st1, st2):
        self.s1 = st1
        self.s2 = st2

cur1 = rres()

class Ui_com(object):
    def setupUi(self, com):
        self.window = com
        com.setObjectName("com")
        com.resize(1000, 600)
        com.setMinimumSize(QtCore.QSize(1000, 600))
        com.setMaximumSize(QtCore.QSize(1000, 600))
        self.WriteLabel = QtWidgets.QLabel(com)
        self.WriteLabel.setGeometry(QtCore.QRect(430, 40, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.WriteLabel.setFont(font)
        self.WriteLabel.setObjectName("WriteLabel")
        self.CommentEdit = QtWidgets.QLineEdit(com)
        self.CommentEdit.setGeometry(QtCore.QRect(240, 140, 541, 321))
        self.CommentEdit.setObjectName("CommentEdit")
        self.SubmitComment = QtWidgets.QPushButton(com)
        self.SubmitComment.setGeometry(QtCore.QRect(480, 500, 93, 28))
        self.SubmitComment.setObjectName("SubmitComment")
        self.ACTIDLabel = QtWidgets.QLabel(com)
        self.ACTIDLabel.setGeometry(QtCore.QRect(750, 20, 151, 31))
        self.ACTIDLabel.setObjectName("ACTIDLabel")
        self.ACTIDEdit = QtWidgets.QLineEdit(com)
        self.ACTIDEdit.setGeometry(QtCore.QRect(680, 60, 261, 51))
        self.ACTIDEdit.setObjectName("ACTIDEdit")

        self.retranslateUi(com)
        QtCore.QMetaObject.connectSlotsByName(com)

        self.SubmitComment.clicked.connect(self.submit)

    def retranslateUi(self, com):
        _translate = QtCore.QCoreApplication.translate
        com.setWindowTitle(_translate("com", "Form"))
        self.WriteLabel.setText(_translate("com", "写评论"))
        self.SubmitComment.setText(_translate("com", "提交"))
        self.ACTIDLabel.setText(_translate("com", "评论活动的ID"))

    def submit(self):
        
        cur1.set(self.ACTIDEdit.text(), self.CommentEdit.text())
        self.window.close()
        

