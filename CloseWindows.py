from PyQt5 import uic, QtWidgets
import sys

class CloseWin():
    def __init__(self):
        super(CloseWin, self).__init__()
        self.ui = uic.loadUi("closewindows.ui")
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    closewin = CloseWin()
    closewin.ui.show()
    app.exec_()