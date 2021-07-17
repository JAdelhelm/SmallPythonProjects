import os
import matplotlib.pyplot as plt
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
        # Sort list after most called words
        fig, ax = plt.subplots()
        ax.plot(sorted(wCount.words[:50], key=wCount.words.count, reverse=False), linewidth=3)
        ax.set_title("Most 50 frequent words")
        plt.show()
        # return listOfCountedWords,

    def findOperations(self):
        pass



firstMain = Main()
print(firstMain.countFile())
