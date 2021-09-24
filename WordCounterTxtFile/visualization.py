import matplotlib.pyplot as plt
# This module is to visualize the Data

# Gets a list of tuples
class visualizeData():
    def __init__(self,dataset):
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
        # Slice first 20 of dataset
        options = str(input("Do you like to see the results in percent? (Y/N): ")).upper()
        if options == "Y":
            # Percentage of Data
            percentageData = [(val/self.sumOfAllwords)*100 for val in self.numList]
            ax.plot(self.wordList[:30],percentageData[:30])
            ax.set_title("Most 30 frequent words")
            ax.set_ylabel("Percentage")
            ax.set_xlabel("Words")
            ax.tick_params(axis='both',labelsize=8)
            plt.show()
        elif options == "N":
            # Normal way
            ax.plot(self.wordList[:30],self.numList[:30])
            ax.set_title("Most 20 frequent words")
            ax.set_ylabel("Words")
            ax.set_xlabel("Frequence")
            # Schriftgröße der Achsen des Diagramms
            ax.tick_params(axis='both',labelsize=8)
            plt.show()
        else:
            print("Your input was invalid")

    def getArrays(self, listOfWords):
        for i in listOfWords:
            for j, k  in listOfWords:
                self.sumOfAllwords += int(k)
                self.wordList.append(j)
                self.numList.append(k)
            break


# checkList = [('der', 353), ('die', 345), ('und', 298), ('in', 261), ('=', 178), ('von', 172), ('werden', 146)]
# visualizeData(checkList)
# newTestData = [val*2 for val in range(0,20)]
# visualizeData(newTestData)
