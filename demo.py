# encoding: utf-8

# ***网络测试程序V0.1***
# 1.采用ping原理进行网络测试
# 2.分离UI主线程和工作线程
# ***********************
# V0.2
# 更新网络成功或失败按钮颜色的变化


import os
import sys
import time

global ip

from ui_net import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class WorkThread(QtCore.QThread):
    sinOut = pyqtSignal(int)

    def __int__(self):
        super(WorkThread, self).__init__()

    def run(self):
        global ip
        exit_code = os.system(u'ping %s' % ip)
        if exit_code:
            # raise Exception('connect failed.')
            self.sinOut.emit(0)  # 反馈信号出去
        else:
            self.sinOut.emit(1)  # 反馈信号出去


# 
class mywindow(QtWidgets.QWidget, Ui_MainWindow):
    trigger = QtCore.pyqtSignal()

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        # 连接 QPushButton 的点击信号到槽 BigWork()
        self.pushButton.clicked.connect(self.net_work)

        # # 延时为了看启动界面
        # time.sleep(1)

    def net_work(self):
        # print("开始多线程")

        self.wt = WorkThread()
        global ip
        ip = self.lineEdit.text()
        print(ip)
        # 开始执行run()函数里的内容
        self.wt.start()

        # # 收到信号
        self.wt.sinOut.connect(self.net_back)  # 将信号连接至net_back函数

    def net_back(self, net_bool):
        if net_bool == 1:
            self.pushButton.setText(u"成功")
            # button1.setStyleSheet("background-color: red");
            # button2.setStyleSheet("background-color:#ff0000;");
            # button3.setStyleSheet("background-color:rgb(255,0,0)");
            self.pushButton.setStyleSheet("background-color: green")

        else:
            self.pushButton.setText(u"失败")
            self.pushButton.setStyleSheet("background-color: red")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # 启动界面
    splash = QtWidgets.QSplashScreen(QPixmap("D://D.png"))
    splash.show()
    splash.showMessage(u"正在加载软件", alignment=QtCore.Qt.AlignHCenter)

    app.processEvents()  # 防止卡死
    print("app.processEvents()")
    myshow = mywindow()
    print("app.processEvents()")
    myshow.show()
    print("app.processEvents()")

    # 关闭启动界面
    splash.finish(myshow)

    sys.exit(app.exec_())