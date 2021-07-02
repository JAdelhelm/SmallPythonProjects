class fileHandling():

    def __init__(self, filePath):
        self.filePath = filePath

    def readFile(self):
        if len(self.filePath) == 0:
            self.filePath = str(input("Add filePath:\n"))
        try:
            contents = ""
            # encoding Problem
            with open(self.filePath,"r+", encoding="utf-8") as file_object:
                for line in file_object:
                    contents += line
            return contents
        except:
            print("FilePath is incorrect")
