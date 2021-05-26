from sys import argv

# Main Dialog
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from os import mkdir
from selenium import webdriver
from time import sleep

mainDlg_class = uic.loadUiType("ui/imgScrapper.ui")[0]

class imgScrapper(QMainWindow, mainDlg_class):
    def __init__(self):
        super(imgScrapper, self).__init__()
        self.setupUi(self)

        # Make directory to save result files
        try:
            mkdir('./images')
        except:
            pass

        self.loadState = 'loading..\n'

        self.searchBtn.clicked.connect(self.searchBtnFunction)

        # self.textEdit_jpgList # txt만들면서 만들어지는 목록들 보여주기 => 그냥 보기좋으라고 있는거

    def search_selenium(self, search_name, search_limit):
        try:
            search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"

            browser = webdriver.Chrome('./ui/chromedriver.exe')
            browser.get(search_url)

            # image_count = len(browser.find_elements_by_tag_name("img"))
            # print("로드된 이미지 개수 : ", image_count)

            browser.implicitly_wait(2)

            self.progressBar.setMaximum(search_limit-1)

            for i in range(search_limit):
                image = browser.find_elements_by_tag_name("img")[i]
                savename = search_name + '_' + str(i) + ".png"
                image.screenshot('./images/' + savename)

                self.progressBar.setValue(i)
                self.loadState = self.loadState + savename + '... saved!\n'
                self.textEdit_jpgList.setText(self.loadState)

            self.loadState = self.loadState + 'Load Complete!'
            self.loadState = ''
            browser.close()
            sleep(0.1)

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
