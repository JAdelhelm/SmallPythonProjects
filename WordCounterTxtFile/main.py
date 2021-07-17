import os
from algorithm import *
from fileHandling import *
from user import *
#from findArticles import *

class Main():
    def __init__(self,filePath=""):
        self.filePath = filePath
        # Gives back NoneType
        user().greet_user()
        self.file = fileHandling(self.filePath).readFile()

    def countFile(self):
        wCount = Wcounter(self.file)
        listOfCountedWords = wCount.countWords()
        return listOfCountedWords


    def findOperations(self):
        pass



firstMain = Main()
print(firstMain.countFile())
