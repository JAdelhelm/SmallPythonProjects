"""Manages user interactions and parse them
to Model and View"""

from pathlib import Path
import re

from numpy import number

class Controller():
    def __init__(self):
        super().__init__()
        self.file = self.processedData()
        self.items = self.numberOfData()

    def numberOfData(self):
        try:
            numberToAnalyse = int(input("How many data do you want to visualize?\n"))
            return numberToAnalyse
        except:
            raise Exception("Your input was not a number")

    """Reads the file and parse it into a string instance"""
    def readData(self, filepath="alice.txt"):
        while len(filepath) == 0:
            filepath = str(input("Insert your filepath: \n"))
        try:
            return open(filepath).read()
        except UnicodeDecodeError:
            return open(filepath,encoding="utf8" ).read()
        else:
            print("Wrong filepath")

    """Process data, remove unnecessary characters and split words
    transform string into a list"""
    def processedData(self):
        content = self.readData()
        content = re.sub(r"[!&@$%^.:]","",content)
        content = re.sub(r"[-,\\]"," ",content).split()
        return content


        
