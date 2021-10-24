from PyQt5.QtWidgets \
    import QMainWindow, \
    QApplication, \
    QMessageBox, \
    QWidget, \
    QPushButton, QGridLayout, QLabel, QLineEdit, QHBoxLayout, \
    QVBoxLayout, QPlainTextEdit

import sys
from PyQt5 import uic
from suiji import Ui_MainWindow
import random


class SuiJiChouYang(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stratButton.clicked.connect(self.start)
        self.ui.outButton.clicked.connect(self.out)

    def out(self):
        self.close()

    def start(self):
        all_num = self.ui.all_lineEdit.text()
        check_num = self.ui.check_lineEdit.text()
        print(all_num)
        print(check_num)
        info = self.ui.dataTextEdit.toPlainText()
        suiji = []
        if all_num == '':
            QMessageBox.about(self, "警告", "输入总人数")
        elif check_num == '':
            QMessageBox.about(self, "警告", "输入随机查询人数")
        elif int(check_num) > int(all_num):
            QMessageBox.about(self, "警告", "输入的随机数大于总人数")
        elif info == '':
            QMessageBox.about(self, "警告", "请输入要随机查询的人数")
        else:
            for line in info.splitlines():
                suiji.append(line)
            if len(suiji) >= int(all_num):
                QMessageBox.about(self, "警告", "请输入的总人数和具体总数据不对")

        QMessageBox.about(self, "输出结果", f"""抽到的结果如下：\n{random.sample(suiji, int(check_num))}""")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    suiji = SuiJiChouYang()
    suiji.show()
    app.exec_()
