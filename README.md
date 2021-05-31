# SUN 1.0v (Google Image Scrapper)
# Using ChromeDriver version 90.0.4430.24

This tool scrap google search engine images by using keyword.
SUN will help you gather images for DL Data set easily.

HOW TO USE 
First set Keyword. (e.g. hammer, 망치...) 
Second set pieces (the number of images to download).
Finally Press Search Button.

SUN will download images as .png extension.
And save file name code is made similarly under this line
# save(./images/'keyword'_'i'.png)

※ SUN is made with selenium library. 
So you must have 'chromedriver.exe' precisely matching with your chrome version in ui folder (Please check source code).

# pyinstaller --noconsole --add-binary "chromedriver.exe";"." --add-binary "imgScrapper.ui";"." --onefile "SUN(GoogleImageScrapper).py"
