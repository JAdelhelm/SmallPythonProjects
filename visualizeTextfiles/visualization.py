import collections
import matplotlib.pyplot as plt
import collections

# Creates an object to visualize the data
class visualizeData():
    def __init__(self,dataset, numWords):
        self.dataset = dataset
        self.numWords = numWords
        self.sumOfAllWords = sum(self.dataset.values())
        print(f"Sum of all words: ",self.sumOfAllWords)
        self.wordList = []
        self.numList = []
        countMostCommon = collections.Counter(self.dataset)
        self.dataset = countMostCommon.most_common(numWords)
        self.getArrays(self.dataset)  
        self.plot_set()

    def plot_set(self):
        print(f"First {self.numWords} sorted Words: {self.dataset}")
        fig, ax = plt.subplots()
        options = str(input("Do you like to see the results in percent? (Y/N): ")).upper()
        if options == "Y":
            percentageData = [(val/self.sumOfAllWords)*100 for val in self.numList]
            ax.plot(self.wordList[: self.numWords],percentageData[:self.numWords])
            ax.set_title(f"Most {self.numWords} frequent words")
            ax.set_ylabel("Percentage")
            ax.set_xlabel("Words")
            ax.tick_params(axis='both',labelsize=8)
            plt.show()
        elif options == "N":
            ax.plot(self.wordList[:self.numWords],self.numList[:self.numWords])
            ax.set_title(f"Most {self.numWords} frequent words")
            ax.set_ylabel("Words")
            ax.set_xlabel("Frequence")
            ax.tick_params(axis='both',labelsize=8)
            plt.show()
        else:
            print("No option was chosen")

    def getArrays(self, listOfWords):
        for i in listOfWords:
            for j, k  in listOfWords:
                self.wordList.append(j)
                self.numList.append(k)
            break


            # print("\nSum of Words: ",allWords,"\n")
            # print(f"Showing first {self.numberWords} sorted words:\n{dictWords.most_common(self.numberWords)}\n")