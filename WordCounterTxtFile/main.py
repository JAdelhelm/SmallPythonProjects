import os
import matplotlib.pyplot as plt
from algorithm import *
from fileHandling import *
from user import Username
#from user import *
#from findArticles import *

class Main():
    def __init__(self,filePath=""):
        self.filePath = filePath
        #Username().get_user()

        self.file = fileHandling(self.filePath).readFile()

    def countFile(self):
        wCount = Wcounter(self.file)
        listOfCountedWords = wCount.countWords()
        # Sort list after most called words
        fig, ax = plt.subplots()
        # Ein- und Ausgabewerte übergeben
        # print(sorted(wCount.words[:50], key=wCount.words.count, reverse=False))
        ax.plot(sorted(wCount.words[:50], key=wCount.words.count, reverse=False), linewidth=3)
        ax.set_title("Most 50 frequent words")
        ax.set_ylabel("Words")
        ax.set_xlabel("Frequence")
        # Schriftgröße der Achsen des Diagramms
        ax.tick_params(axis='both',labelsize=8)
        plt.show()
        # return listOfCountedWords,

    def findOperations(self):
        pass



firstMain = Main()
firstMain.countFile()
