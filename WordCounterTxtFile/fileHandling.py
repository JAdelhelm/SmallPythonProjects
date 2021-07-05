"""
Class to handle the file.
Next step is to implement options how to handle .txt files and strings """


class fileHandling():

    def __init__(self, filePath):
        self.filePath = filePath

    def readFile(self):
        try:
            if len(self.filePath) == 0:
                # optionsReadFile()
                self.filePath = str(input("Add filePath:\n"))
            contents = ""
            # encoding Problem
            with open(self.filePath,"r+", encoding="utf-8") as file_object:
                for line in file_object:
                    contents += line
            return contents
        except:
            print("FilePath is incorrect")




    def optionsReadFile(self):
        dicOptions = {
        1: "Add String",
        2: "Add FilePath"
        }
