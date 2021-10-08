from algorithm import *
from fileHandling import *
from visualization import visualizeData

class Main():
    def __init__(self):
        while True:
            try:
                inputOpt = input("How many words do you like to visualize?\n")
                self.numWords = int(inputOpt); break       
            except:
                if inputOpt == "exit()" or inputOpt == "": break
                print("Wrong Input, write exit() to escape")

    def readFile(self):
        txtFile = fileHandling().readFile()
        wordData = algorithmWords(txtFile).countWords(self.numWords)
        return wordData

    def visualizeDataset(self, data):
        try:
            if len(data) == 0:
                raise Exception
            visual = visualizeData(data, self.numWords)
        except:
            print("No words are counted")


visMain = Main()
data = visMain.readFile()
visMain.visualizeDataset(data)