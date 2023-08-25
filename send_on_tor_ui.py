from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SendFilesWindow(object):
    def setupUi(self, SendFilesWindow):
        SendFilesWindow.setObjectName("SendFilesWindow")
        SendFilesWindow.resize(400, 300)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SendFilesWindow = QtWidgets.QMainWindow()
    ui = Ui_SendFilesWindow()
    ui.setupUi(SendFilesWindow)
    SendFilesWindow.show()
    sys.exit(app.exec_())
