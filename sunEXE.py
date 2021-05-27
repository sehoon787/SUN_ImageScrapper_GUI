from os import system

# pyinstaller --noconsole --onefile --icon=../icons/sun.ico "sunEXE.py"

try:
    system('start dist\\SUN(GoogleImageScrapper)\\SUN(GoogleImageScrapper).exe')
except:
    pass
