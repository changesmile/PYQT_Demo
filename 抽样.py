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
        if all_num == '':
            QMessageBox.about(self, "警告", "输入总人数")
        elif check_num == '':
            QMessageBox.about(self, "警告", "输入随机查询人数")
        elif int(check_num) > int(all_num):
            QMessageBox.about(self, "警告", "输入的随机数大于总人数")
        elif info == '':
            QMessageBox.about(self, "警告", "请输入要随机查询的人数")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    suiji = SuiJiChouYang()
    suiji.show()
    app.exec_()
