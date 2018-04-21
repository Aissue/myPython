# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstone.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import itchat
import time
import threading

myUserName = ""
reMsg = ""
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(363, 241)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 80, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 80, 75, 23))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 271, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 191, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 281, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(280, 210, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 190, 161, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close)
        self.pushButton.clicked.connect(self.test)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "微信自动回复设置器"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "关闭"))
        self.label.setText(_translate("Form", "自动回复内容:"))
        self.label_2.setText(_translate("Form", "使用方法："))
        self.label_3.setText(_translate("Form", "1、设置自动回复内容，点击确定"))
        self.label_4.setText(_translate("Form", "2、用微信扫描弹出的二维码，点击登录，设置成功"))
        self.label_5.setText(_translate("Form", "by Aissue"))
        self.label_6.setText(_translate("Form", "3、关闭按钮结束自动回复"))

    @itchat.msg_register(['Map', 'Card', 'Note', 'Sharing', 'Picture', 'Text'])
    def text_reply(msg):
        global myUserName
        # 当消息不是由自己发出的时候
        if not msg['FromUserName'] == myUserName:
            # 回复给好友
            return u'%s' % (reMsg)

    def test(self):
        msg = self.lineEdit.text()
        t = threading.Thread(target=task,args=(msg,))
        t.setDaemon(True)
        t.start()

def task(msg):
    global reMsg
    global myUserName
    reMsg = msg
    print("设定回复语：%s" % reMsg)
    itchat.load_login_status
    itchat.auto_login()
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


