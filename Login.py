# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from AdminWindow import *
from UserWindow import *
from PyQt5.QtWidgets import *


class LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 363)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 190, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 190, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(228, 100, 171, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(228, 128, 171, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 100, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 128, 71, 20))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.check_user_and_passwd)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BIBA模型登录"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))
        self.lineEdit.setText(_translate("MainWindow", "请输入账号"))
        self.lineEdit_2.setText(_translate("MainWindow", "请输入密码"))
        self.label.setText(_translate("MainWindow", "账号"))
        self.label_2.setText(_translate("MainWindow", "密码"))

    def check_user_and_passwd(self):
        user=self.lineEdit.text()
        passwd=self.lineEdit_2.text()
        md5=hashlib.md5()
        md5.update(passwd.encode("utf-8"))
        passwd=md5.hexdigest()
        if (user == '') or (passwd == ''):
            QMessageBox.warning(self, "警告", "账号和密码不能为空", QMessageBox.Yes)
            self.lineEdit.setFocus()
        print(user, passwd)
        fr = open('./etc/passwd.txt')
        arrayofLines = fr.readlines()
        numberofLines = len(arrayofLines)
        for line in arrayofLines:
            line = line.strip()
            listFromLine = line.split(':')
            name = listFromLine[0]
            if name == user:
                numberofLines = -1
                truepasswd = listFromLine[1]
                if truepasswd == passwd:
                    group = listFromLine[2]
                    print("\n登录成功!\n")
                    if name == 'admin':
                        print('admin登录')
                        adminUI.show()
                        MainWindow.close()
                    else:
                        urName = user
                        print("\n用户登录")
                        userUI.show()
                        MainWindow.close()
                        userUI.lineEdit.setText(urName)
                        userUI.lineEdit_2.setText(group)
                else:
                    QMessageBox.warning(self,
                                        "警告",
                                        "密码错误！",
                                        QMessageBox.Yes)
                    self.lineEdit.setFocus()
        fr.close()
        return 0




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginWindow()
    adminUI = AdminWindow()
    userUI = UserWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())