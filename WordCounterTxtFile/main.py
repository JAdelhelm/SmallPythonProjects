import os
from algorithm import *
from fileHandling import *
from user import Username
from visualization import visualizeData
import time
#from user import *
#from findArticles import *

class Main():
    def __init__(self,filePath=""):
        self.filePath = filePath
        self.file = fileHandling(self.filePath).readFile()
    # Count words in Wcounter class
    # Returns a list with tuples
        self.wCount = Wcounter(self.file).countWords()
        # time.sleep(10)

    def visualizeDataset(self):
        try:
            if len(self.wCount) == 0:
                raise Exception
            visual = visualizeData(self.wCount)
        except:
            print("No words are counted")
        # return listOfCountedWords,

    def findOperations(self):
        pass



firstMain = Main()
firstMain.visualizeDataset()
