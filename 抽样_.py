from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
import random, csv, sys
from datetime import datetime


class Stats(QMainWindow):
    bool_start = False
    list_samples = []

    def __init__(self):
        # 把csv内容读入 对象属性
        rows = []
        with open('./学生名单.csv', encoding='GBK') as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)

        self.rows = rows[1:]

        # 从文件中加载UI定义
        super().__init__()
        self.ui = uic.loadUi("Unit7.ui")
        self.ui.pB_Start.clicked.connect(self.pB_Start)
        self.ui.pB_Save.clicked.connect(self.pB_Save)
        self.ui.pB_Show.clicked.connect(self.pB_Show)
        self.ui.pB_Quit.clicked.connect(self.pB_Quit)
        rownum = len(self.rows)
        self.ui.lE_Total.setText(str(rownum))
        self.ui.lE_Sample.setText(str(int(rownum / 3)))

    # 抽样
    def pB_Start(self):
        num = int(self.ui.lE_Sample.text())

        self.sample = random.sample(self.rows, num)

        showText = ''
        for row in self.sample:
            showText += f'{"    ".join(row)}\n'

        self.ui.Browser.setPlainText(showText)

    # 保存抽样数据
    def pB_Save(self):
        # 将本次抽样追加记录“学生名单.csv”的新列，抽中的名单标记“抽中”，没有抽中的不标记
        prefix = datetime.now().strftime('%Y%m%d%H%M%S')
        with open(f'sample{prefix}.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.sample)

        QMessageBox.about(self.ui,
                          f'成功',
                          f'已经保存到 sample{prefix}.csv'
                          )

    # 显示全班名单
    def pB_Show(self):
        showText = ''
        for row in self.rows:
            showText += f'{"    ".join(row)}\n'

        self.ui.Browser.setPlainText(showText)

    def pB_Quit(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Stats()
    window.ui.show()
    sys.exit(app.exec_())
