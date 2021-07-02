from wordCounter import *
from loadFile import *

class Main():
    def __init__(self):
        self.file = LoadFile().readFile()

    def countFile(self):
        wCount = Wcounter(self.file)
        print(wCount.count_words())


newMain = Main()
newMain.countFile()
