# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class UserWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UserWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.file_path=""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(81, 111, 75, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(81, 149, 60, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(163, 111, 167, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(163, 149, 167, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 20, 201, 61))
        self.label_5.setMinimumSize(QtCore.QSize(201, 0))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 220, 291, 241))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 190, 72, 15))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(451, 111, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(551, 114, 171, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(440, 220, 291, 241))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(81, 491, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(181, 494, 171, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(451, 491, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(589, 491, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        """调用QFileSystemModel，获得可视化文件目录系统"""
        self.model = QFileSystemModel()
        current_path = os.getcwd()
        self.model.setRootPath(current_path)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(30, 220, 400, 300))
        self.treeView.setObjectName("treeView")
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.setRootPath(current_path))
        # self.treeView = QTreeView()
        self.treeView.setAnimated(False)
        self.treeView.setIndentation(20)
        self.treeView.setSortingEnabled(True)
        self.treeView.setWindowTitle("Dir View")
        self.treeView.resize(400, 260)
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.treeView)
        self.setLayout(windowLayout)
        self.treeView.doubleClicked.connect(self.show_path)

        self.pushButton.clicked.connect(self.touch_file)
        self.pushButton_3.clicked.connect(self.read_file)
        self.pushButton_4.clicked.connect(self.write_file)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.textEdit)
        MainWindow.setTabOrder(self.textEdit, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.textEdit_2)
        MainWindow.setTabOrder(self.textEdit_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_4)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "用户界面"))
        self.label.setText(_translate("MainWindow", "当前用户名"))
        self.label_3.setText(_translate("MainWindow", "用户等级"))
        self.label_5.setText(_translate("MainWindow", "用户面板"))
        self.label_2.setText(_translate("MainWindow", "文件目录："))
        self.pushButton.setText(_translate("MainWindow", "新建文件"))
        self.lineEdit_3.setText(_translate("MainWindow", "请输入文件名"))
        self.pushButton_2.setText(_translate("MainWindow", "选择文件"))
        self.pushButton_3.setText(_translate("MainWindow", "读取"))
        self.pushButton_4.setText(_translate("MainWindow", "写入"))

    def show_path(self, signal):
        """获得当前文件目录的文件"""
        file_path = self.treeView.model().filePath(signal)
        print(file_path)
        self.lineEdit_4.setPlaceholderText(file_path)
        print(self.lineEdit_4)
        self.file_path = file_path

    def getGrade(self):
        """./test/目录下有5个文件，分别对应4种权限"""
        current_path = os.getcwd().replace('\\','/')
        print (os.getcwd())
        str= current_path + "/test/"
        print(str)
        dict = {str+"admin.txt": "A", str+"A.txt": "A", str+"B.txt": str+"B", str+"C.txt": str+"C", str+"D.txt": "D"}
        print(dict)
        return dict

    def touch_file(self):
        urName = self.lineEdit.text()
        filename = self.lineEdit_3.text()
        cur_path = os.getcwd()
        new_path = os.path.join(cur_path + '/file/', urName)
        print(urName)
        if os.path.exists(new_path) == False:
            os.mkdir(new_path)
        os.chdir(new_path)
        fr = open(filename, 'w')
        key = (new_path + '/' + filename).replace('\\', '/')
        fr.close()
        os.chdir(cur_path)
        fa = open('./etc/ac.txt', 'r')
        a = fa.read()
        if a == '':
            dict = {}
        else:
            dict = eval(a)
        dict[key] = self.lineEdit_3.text()
        QMessageBox.information(self, "提示", "创建文件"+filename+"成功")
        fr = open('./etc/ac.txt', 'w')
        fr.write(str(dict))
        fr.close()
        fa.close()

    def read_file(self):
        log=""
        dict = self.getGrade()
        fgrade = str(dict[self.file_path])
        ugrade = self.lineEdit_2.text()
        if ugrade >= fgrade:
            print("用户"+ugrade + "正在读取文件权限为" + fgrade + "的文件")
            log=log+"用户"+ugrade + "正在读取文件权限为" + fgrade + "的文件\n"
            print(log)
            filename = self.file_path
            print(filename)
            fr = open(filename)
            lines = ''
            arrayofLines = fr.readlines()
            for line in arrayofLines:
                lines += line
            self.textEdit.setText(lines)
            print(' 读取成功\n')
            log=log+lines+"\n读取成功\n"
            self.textEdit_2.setPlaceholderText(log)
        else:
            QMessageBox.warning(self,
                                "警告",
                                "您的用户等级太高",
                                QMessageBox.Yes)
            self.lineEdit_4.setFocus()

    def write_file(self):
        log = ""
        dict = self.getGrade()
        fgrade = dict[self.file_path]
        ugrade = self.lineEdit_2.text()
        print("用户"+ugrade + "正在写入文件权限为" + fgrade + "的文件")
        log = log + "用户"+ugrade + "正在写入文件权限为" + fgrade + "的文件"
        if ugrade <= fgrade:
            filename = self.file_path
            str = self.textEdit.toPlainText()
            print(str)
            fo = open(filename, 'r+')
            fo.seek(0, 2)
            fo.write(str)
            log = log + " 写入成功\n"
            self.textEdit_2.setPlaceholderText(log)
        else:
            QMessageBox.warning(self,
                                "警告",
                                "您的用户等级太低",
                                QMessageBox.Yes)
            self.lineEdit_4.setFocus()



if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    userUI=UserWindow()
    userUI.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())