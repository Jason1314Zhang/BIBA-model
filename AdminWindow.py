# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib
import os
from PyQt5.QtWidgets import *


class AdminWindow(QtWidgets.QMainWindow):
    def __init__(self):

        """它会查找所有的超类，以及超类的超类，直到找到所需的特性为止"""
        super(AdminWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.user = ''


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 158, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 300, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 442, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(351, 138, 45, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(351, 174, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 210, 60, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(418, 138, 162, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(418, 174, 162, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 450, 53, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(410, 450, 171, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 30, 201, 61))
        self.label_5.setMinimumSize(QtCore.QSize(201, 0))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(420, 210, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(350, 300, 261, 87))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.add_user)
        self.pushButton_2.clicked.connect(self.read_user)
        self.pushButton_3.clicked.connect(self.delete_user)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.textEdit)
        MainWindow.setTabOrder(self.textEdit, self.lineEdit_4)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "管理员界面"))
        self.pushButton.setText(_translate("MainWindow", "添加用户"))
        self.pushButton_2.setText(_translate("MainWindow", "查询用户"))
        self.pushButton_3.setText(_translate("MainWindow", "删除用户"))
        self.label.setText(_translate("MainWindow", "用户名"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.label_3.setText(_translate("MainWindow", "用户等级"))
        self.label_4.setText(_translate("MainWindow", "用户名 "))
        self.label_5.setText(_translate("MainWindow", "管理员面板"))
        self.comboBox.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox.setItemText(1, _translate("MainWindow", "B"))
        self.comboBox.setItemText(2, _translate("MainWindow", "C"))
        self.comboBox.setItemText(3, _translate("MainWindow", "D"))

    def add_user(self):
        """添加用户"""
        print("添加用户")
        user= self.lineEdit.text()
        print(self.lineEdit)
        passwd=self.lineEdit_2.text()
        md5=hashlib.md5()
        md5.update(passwd.encode("utf-8"))
        passwd=md5.hexdigest()
        group=self.comboBox.currentText()
        print(user)
        print(passwd)
        self.user=user
        """判断新加用户是否存在，如果不存在这个用户，则添加"""
        if self.not_exist():
            if (user == '') or (passwd == ''):
                QMessageBox.information(self, "警告", "账号和密码不能为空")
                self.lineEdit.setFocus()
            else:
                current_path=os.getcwd()
                filepath=current_path+"/etc/passwd.txt"
                fr=open(filepath,"r+")
                str=user+":"+passwd+":"+group+"\n"
                fr.seek(0,2)
                fr.write(str)
                fr.close()
                QMessageBox.information(self, "提示", "添加用户"+user+"成功")

        else:
            QMessageBox.warning(self, "警告", "账号已存在")
            self.lineEdit.setFocus()

    def read_user(self):
        """查阅系统中有多少用户"""
        current_path = os.getcwd()
        filepath = current_path + "/etc/passwd.txt"
        fr = open(filepath, "r+")
        """分别读出每一行用户信息"""
        userlines=fr.readlines()
        users=""
        for line in userlines:
            line=line.strip()
            """用：隔开用户密码和组，得到用户名"""
            arrays=line.split(":")
            users=users+arrays[0]+"    "
        self.textEdit.setPlaceholderText(users)
        print(self.textEdit)
        QMessageBox.information(self, "提示", "成功查找到用户")
    def delete_user(self):
        user=self.lineEdit_4.text()
        if user!="":
            current_path = os.getcwd()
            filepath = current_path + "/etc/passwd.txt"
            fr = open(filepath, "r+")
            with open(filepath, 'r', encoding="utf-8") as r:
                lines = r.readlines()
            with open(filepath, 'w', encoding="utf-8") as w:
                for line in lines:
                    line = line.strip()
                    listFromLine = line.split(':')
                    if user == listFromLine[0]:
                        print('删除用户' + user)
                        continue
                    if line == '\n':
                        line = ''
                    w.write(line)
                    QMessageBox.information(self, "提示", "成功删除账号"+user)
        else:
            QMessageBox.information(self, "提示", "无此用户，请输入正确的用户")
    """判断新加用户是否已经存在"""
    def not_exist(self):
        user=self.user
        flag = True
        current_path = os.getcwd()
        filename = current_path + '/etc/passwd.txt'
        fr = open(filename)
        arrayofLines = fr.readlines()
        for line in arrayofLines:
            line = line.strip()
            listFromLine = line.split(':')
            if user == listFromLine[0]:
                flag = False
        return flag


if __name__ == "__main__":
    import sys
    app= QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    adminUI=AdminWindow()
    adminUI.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

