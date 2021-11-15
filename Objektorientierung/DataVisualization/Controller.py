"""Manages user interactions and parse them
to Model and View"""

import re
from typing import List, Dict
import sys



class Controller():
    def __init__(self,filepath="alice.txt"):
        super().__init__()
        self.filepath = filepath
        self.file: List[str] = self.processedData()

    """Reads the file and parse it into a string instance
    Annotation str that says that a str of data will be returned"""
    def readData(self,filepath) -> str:
        while len(filepath) == 0:
            filepath: str = str(input("Insert your filepath: \n"))
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
        content: List[str] = re.sub(r"[!&@$%^.:]","",inputData)
        content: List[str] = re.sub(r"[-,\\]"," ",inputData).split()
        return content




        
