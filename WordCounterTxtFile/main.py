from wCounter import *
from fileHandling import *

class Main():
    def __init__(self, filePath="alice.txt"):
        self.filePath = filePath
        self.file = fileHandling.readFile()

    def countFile(self):
        wCount = Wcounter(self.file)
        print(wCount.count_words())


newMain = Main()
newMain.countFile()
