import os
from algorithm import *
from fileHandling import *
from user import Username
from visualization import visualizeData
#from user import *
#from findArticles import *

class Main():
    def __init__(self,filePath=""):
        self.filePath = filePath
    # To safe usernames
        #Username().get_user()
    # To Read the File
        self.file = fileHandling(self.filePath).readFile()
    # To count the Words
        self.wCount = Wcounter(self.file)

    def countFile(self):
        listOfCountedWords = self.wCount.countWords()

        # Sort list after most called words
    def visualizeDataset(self):
        try:
            if len(self.wCount.words) == 0:
                raise Exception
            visual = visualizeData(self.wCount)
        except:
            print("No words are counted")
        # return listOfCountedWords,

    def findOperations(self):
        pass



firstMain = Main()
firstMain.countFile()
firstMain.visualizeDataset()
