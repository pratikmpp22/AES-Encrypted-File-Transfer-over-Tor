import os
import sys
import subprocess
from PyQt5 import QtWidgets
from main_ui import Ui_MainWindow
import encrypt
import decrypt


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.browse_btn.clicked.connect(self.get_filepath)
        self.encrypt_btn.clicked.connect(self.encrypt_file)

        self.browse_btn_tab2.clicked.connect(self.get_filepath)
        self.decrypt_btn_tab2.clicked.connect(self.decrypt_file)

        self.send_btn.clicked.connect(self.send_file_on_tor)
        self.send_link_btn.clicked.connect(self.open_send_link_in_tor)

        self.receive_btn.clicked.connect(self.receive_files_on_tor)
        self.receive_link_btn.clicked.connect(self.open_receive_link_in_tor)

        self.show()
        
    def get_filepath(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'File', os.getenv('HOME'))
        if self.tabWidget.currentIndex() == 0:
            self.filepath_ledit.setText(filename)
        elif self.tabWidget.currentIndex() == 1:
            self.filepath_ledit_tab2.setText(filename)

    def encrypt_file(self):
        pub_key = self.pubkey_textedit.toPlainText().encode()
        result = encrypt.encrypt(pub_key, self.filepath_ledit.text())
        QtWidgets.QMessageBox.information(self, "Result", result)

    def decrypt_file(self):
        priv_key = self.privkey_textedit_tab2.toPlainText().encode()
        result = decrypt.decrypt(priv_key, self.filepath_ledit_tab2.text())
        QtWidgets.QMessageBox.information(self, "Result", result)

    def send_file_on_tor(self):
        onionshare_path = r"C:\Users\91845\OnionShare\onionshare-cli"

        # Browse for files to send
        filenames, _ = QtWidgets.QFileDialog.getOpenFileNames(self, 'Select Files to Send', os.getenv('HOME'))

        try:
            if filenames:
                # Launch OnionShare in a new Windows command prompt to send the specified files
                command = f"{onionshare_path} {' '.join(filenames)}"
                subprocess.call(f"start cmd /K {command}", shell=True)
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "No files selected.")
        except subprocess.CalledProcessError:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to open OnionShare.")

    def receive_files_on_tor(self):
        onionshare_path = r"C:\Users\91845\OnionShare\onionshare-cli"

        command = f"{onionshare_path} --receive"
        subprocess.call(f"start cmd /K {command}", shell=True)


    def open_send_link_in_tor(self):
        link, link_accepted = QtWidgets.QInputDialog.getText(self, "Send files on tor for a link", "Enter the OnionShare link:")
        if link_accepted:
            tor_browser_path = r"C:\Users\91845\Desktop\Tor Browser\Browser\firefox.exe"
            subprocess.call([tor_browser_path, link])

    def open_receive_link_in_tor(self):
        link, link_accepted = QtWidgets.QInputDialog.getText(self, "Receive files on tor for a link", "Enter the OnionShare link:")
        if link_accepted:
            tor_browser_path = r"C:\Users\91845\Desktop\Tor Browser\Browser\firefox.exe"
            subprocess.call([tor_browser_path, link])
      


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
