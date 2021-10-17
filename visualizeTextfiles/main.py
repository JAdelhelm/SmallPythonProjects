from matplotlib.pyplot import install_repl_displayhook
from algorithm import *
from fileHandling import *
from visualization import visualizeData
import collections

class Main():
    def __init__(self):
        pass

    def readFile(self):
        txtFile = fileHandling().readFile()
        wordData = algorithmWords(txtFile).countWords()
        return wordData


visMain = Main()
data = visMain.readFile()
# print(type(data))
while True:
    try:
        inputOpt = int(input("How many words do you like to visualize?\n"))
        numWords = int(inputOpt); break       
    except:
        if inputOpt == "exit()" or inputOpt == "": break
        print("Wrong Input, write exit() to escape")
visualizeData(data, inputOpt)

# Test
# testObject = collections.Counter(["Hi","Hi","Hi","WOW","wow","ohh","YES"])
# newVisuaization = visualizeData(testObject, 10)