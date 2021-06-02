# ChromeDriver 90.0.4430.24
import sys
from sys import argv
from os.path import join, dirname, abspath

# Main Dialog
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from os import mkdir
from selenium import webdriver
from time import sleep

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', dirname(abspath(__file__)))
    return join(base_path, relative_path)
form = resource_path("imgScrapper.ui")
mainDlg_class = uic.loadUiType(form)[0]
# mainDlg_class = uic.loadUiType("ui/imgScrapper.ui")[0]

class imgScrapper(QMainWindow, mainDlg_class):
    def __init__(self):
        super(imgScrapper, self).__init__()
        self.setupUi(self)

        # Make directory to save result files
        try:
            mkdir('./images')
        except:
            pass

        icon = resource_path("sun.png")
        self.setWindowIcon(QIcon(icon))

        self.loadState = 'loading..\n'

        self.searchBtn.clicked.connect(self.searchBtnFunction)

        # self.textEdit_jpgList # txt만들면서 만들어지는 목록들 보여주기 => 그냥 보기좋으라고 있는거

    def search_selenium(self, search_name, search_limit):
        try:
            search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"

            if getattr(sys, 'frozen', False):
                chromedriver_path = join(sys._MEIPASS, "chromedriver.exe")
                browser = webdriver.Chrome(chromedriver_path)
            browser.get(search_url)

            # image_count = len(browser.find_elements_by_tag_name("img"))
            # print("로드된 이미지 개수 : ", image_count)

            browser.implicitly_wait(2)

            self.progressBar.setMaximum(search_limit-1)

            for i in range(search_limit):
                self.progressBar.setValue(i)

                image = browser.find_elements_by_tag_name("img")[i]
                savename = search_name + '_' + str(i) + ".png"
                image.screenshot('./images/' + savename)

                self.loadState = self.loadState + savename + '... saved!\n'
                self.textEdit_jpgList.setText(self.loadState)

            self.loadState = self.loadState + 'Load Complete!'
            self.loadState = ''
            sleep(0.1)
            browser.close()

            reply = QMessageBox.question(self, 'Message', 'Do you need more Data?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                pass
            else:
                sys.exit()

        except Exception as e:
            pass

    def searchBtnFunction(self):
        self.progressBar.setValue(0)

        self.keyword = str(self.textEdit_keyword.toPlainText())
        self.pieces = int(self.textEdit_pieces.toPlainText())

        # search_maybe(search_name, search_limit, search_path)
        self.search_selenium(self.keyword, self.pieces)

if __name__ == "__main__":
    app = QApplication(argv)
    win = imgScrapper()
    win.show()
    app.exec_()
