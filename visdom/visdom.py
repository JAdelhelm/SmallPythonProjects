import re
from pathlib import Path
import collections
import matplotlib.pyplot as plt
from vis import visualizeData

class visdom():
    def __init__(self):
        pass
    def readTxt(self):
        try:
            inputPath = str(input("Add filepath: "))
            filePath = Path(inputPath).resolve()
            content = open(filePath, "r").read()
            return content
        except:
            try:
                contentEngl = open(filePath, "r", encoding='utf-8').read()  
                return contentEngl
            except:
                print("FilePath is incorrect")
                raise NameError
    def prepare(self, content):
        try:
            content = content.lower()
            content = re.sub(r"[!&@$%^.:]","",content)
            content = re.sub(r"[-,\\]"," ",content).split()
            dictWords = collections.Counter(content)
            return dictWords
        except: return ""

visObject = visdom()
content = visObject.readTxt()
content = visObject.prepare(content)
# Visualize
newVisualization = visualizeData(dataset=content,numWords=5)

    