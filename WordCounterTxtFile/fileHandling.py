class fileHandling():

"""
Class to handle the file to read.
Next step is to implement options to handle .txt files """

dicOptions = {
1: "Add String",
2: "Add FilePath"
}

    def __init__(self, filePath):
        self.filePath = filePath

    def readFile(self):
        if len(self.filePath) == 0:
            optionsReadFile()
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

    def optionsReadFile(self):
        pass
