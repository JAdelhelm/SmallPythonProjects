import matplotlib.pyplot as plt
# Creates an object to visualize the data
class visualizeData():
    def __init__(self,dataset, words):
        self.words = words
        print("Different words: ",len(dataset))
        self.dataset = dataset
        self.sumOfAllwords = 0
        self.wordList = []
        self.numList = []
        self.getArrays(self.dataset)
        print("Sum of all words: ", self.sumOfAllwords)
        self.plot_set()

    def plot_set(self):
        fig, ax = plt.subplots()
        options = str(input("Do you like to see the results in percent? (Y/N): ")).upper()
        if options == "Y":
            percentageData = [(val/self.sumOfAllwords)*100 for val in self.numList]
            ax.plot(self.wordList[:self.words],percentageData[:self.words])
            ax.set_title(f"Most {self.words} frequent words")
            ax.set_ylabel("Percentage")
            ax.set_xlabel("Words")
            ax.tick_params(axis='both',labelsize=8)
            plt.show()
        elif options == "N":
            ax.plot(self.wordList[:self.words],self.numList[:self.words])
            ax.set_title(f"Most {self.words} frequent words")
            ax.set_ylabel("Words")
            ax.set_xlabel("Frequence")
            ax.tick_params(axis='both',labelsize=8)
            plt.show()
        else:
            print("No option was chosen")

    def getArrays(self, listOfWords):
        for i in listOfWords:
            for j, k  in listOfWords:
                self.sumOfAllwords += int(k)
                self.wordList.append(j)
                self.numList.append(k)
            break
