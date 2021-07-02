class LoadFile():
    def __init__(self, filePath="Add FilePath"):
        self.filePath = str(input("Add filePath:"))

    def readFile(self):
        # if len(self.filePath) == 0:
        #     self.filePath = "alice.txt"
        try:
            with open(self.filePath) as file_object:
                contents = file_object.read()
            return contents
        except:
            print("Filepath does not exist")
