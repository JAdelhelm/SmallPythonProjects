"""Manages user interactions and parse them
to Model and View"""

import re

class Controller():
    def __init__(self,filepath="alice.txt"):
        super().__init__()
        self.filepath = filepath
        self.file = self.processedData()
        self.n = 0

    """Reads the file and parse it into a string instance"""
    def readData(self,filepath):
        while len(filepath) == 0:
            filepath = str(input("Insert your filepath: \n"))
        try:
            return open(filepath).read()
        except UnicodeDecodeError:
            return open(filepath,encoding="utf8" ).read()
        else:
            print("Wrong filepath")

    """Process data, remove unnecessary characters and split words
    transform string into a list
    --> Takes input file from readData"""
    def processedData(self,inputData=""):
        content = re.sub(r"[!&@$%^.:]","",inputData)
        content = re.sub(r"[-,\\]"," ",inputData).split()
        return content




        
