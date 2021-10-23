from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
from ui_check import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # 创建对象
        self.ui.setupUi(self)  # 初始化界面
        self.ui.button.clicked.connect(self.handleCalc)  # 绑定函数监听事件

    def handleCalc(self):
        info = self.ui.textEdit.toPlainText()
        max_num = ""
        min_num = ""
        for line in info.splitlines():  # 按照 行 进行切割
            if not line.strip():  # 按照空格进行切割  或者按照 .strip("*") 这样切割为多份
                continue
            parts = line.split(" ")
            parts = [p for p in parts if p]
            name, salary, age = parts
            if int(salary) >= 20000:
                max_num += name + "\n"
            else:
                min_num += name + "\n"
        QMessageBox.about(self, "统计结果",
                          f"""20000以上有：\n{max_num}\n20000以下有：\n{min_num}\n""")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
