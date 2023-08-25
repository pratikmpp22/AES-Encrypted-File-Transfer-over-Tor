from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReceiveFilesWindow(object):
    def setupUi(self, ReceiveFilesWindow):
        ReceiveFilesWindow.setObjectName("ReceiveFilesWindow")
        ReceiveFilesWindow.resize(400, 300)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReceiveFilesWindow = QtWidgets.QMainWindow()
    ui = Ui_ReceiveFilesWindow()
    ui.setupUi(ReceiveFilesWindow)
    ReceiveFilesWindow.show()
    sys.exit(app.exec_())
