class fileHandling():
    def __init__(self, filePath):
        self.filePath = filePath

    def readFile(self):
        try:
            with open(self.filePath) as file_object:
                contents = file_object.read()
            return contents
        except:
            print("Filepath does not exist")
