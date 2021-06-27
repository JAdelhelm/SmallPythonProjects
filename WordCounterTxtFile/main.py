from wordCounter import *
from file import *

class Main():
    def __init__(self):
        self.filePath = File().filePath

    def countFile(self):
        wCount = Wcounter(self.filePath)
        print(wCount.count_words())

newMain = Main()

newMain.countFile()
