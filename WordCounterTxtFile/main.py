import os
from algorithm import *
from fileHandling import *

class Main():
    def __init__(self,filePath=""):
        self.filePath = filePath
        self.file = ""

    def readFile(self):
        self.file = fileHandling(self.filePath).readFile()

    def countFile(self):
        wCount = Wcounter(self.file)
        print(wCount.count_words())


firstMain = Main("alice.txt")
firstMain.readFile()
firstMain.countFile()
