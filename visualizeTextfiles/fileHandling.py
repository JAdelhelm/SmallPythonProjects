from pathlib import Path

class fileHandling():
    def __init__(self):
        pass

    def readFile(self):
        try:
            inputPath = str(input("Add filePath: "))
            filePath = Path(inputPath).resolve()
            content = open(filePath, "r").read()
            return content
        except:
            try:
                contentEngl = open(filePath, "r", encoding='utf-8').read()  
                return contentEngl
            except:
                print("FilePath is incorrect")

       

