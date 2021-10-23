from PyQt5.QtWidgets \
    import QMainWindow, \
    QApplication, \
    QMessageBox, \
    QWidget, \
    QPushButton, QGridLayout
import sys


class Windows2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("窗口2")
        self.centerWidget = QWidget()
        self.setCentralWidget(self.centerWidget)

        button = QPushButton("按钮2")
        grid = QGridLayout(self.centerWidget)
        grid.addWidget(button)

        button.clicked.connect(self.close_self)
    def close_self(self):
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("窗口1")
        self.centerWidget = QWidget()
        self.setCentralWidget(self.centerWidget)

        button = QPushButton("按钮1")

        grid = QGridLayout(self.centerWidget)
        grid.addWidget(button)

        button.clicked.connect(self.open_new_window)

    def open_new_window(self):
        # 实例化另外一个窗口
        self.window2 = Windows2()
        # 显示窗口
        self.window2.show()
        # 关闭自己
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()
