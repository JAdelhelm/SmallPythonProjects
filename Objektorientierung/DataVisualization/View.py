"""Is used to visualize graphs"""
from Model import *
from Controller import *
import matplotlib.pyplot as plt
import pandas as pd
import time, functools
class View(Model, Controller):
    def __init__(self, filep="",nData=0):
        super().__init__()
        # Initialize different objects
        self.initialiseObjects(filePath=filep,nData=nData)
        

    def graphVisualize(self):
        plt.plot(self.getItems(self.items)[0], self.getItems(self.items)[1])
        plt.xlabel("Words")
        plt.ylabel("Number")
        plt.title("Visualization of data by Jörg Adelhelm")
        plt.show()

    def pieVisualize(self):
        start = time.perf_counter()

        if self.items > 3: explodePie = [0.2]+[0.2]+[0.2]+ [0 for val in range(3,self.items)]
        else: explodePie = [0 for val in range(0,self.items)]
        plt.pie(self.getItems(self.items)[1],labels=self.getItems(self.items)[0], shadow=True, startangle=90, explode=explodePie)
        plt.xlabel(f"\nExploded items contain {self.percentOfData} % of all data")
        
        print(f"It took {round(time.perf_counter()-start,2)} seconds to visualize the file")
        plt.show()
       

    def getItems(self, items):
        itemsOfData = self.processedFile.most_common(items)
        listWords = []
        listNums = []
        for word, num in itemsOfData:
            listWords.append(word)
            listNums.append(num)
        return tuple(listWords), tuple(listNums)

    def numberOfData(self,n):
        try:
            if n != 0: return n
            numberToAnalyse = int(input("How many data do you want to visualize?\n"))
            return numberToAnalyse
        except:
            raise Exception("Your input was not a number")

    def initialiseObjects(self,filePath,nData=0):
        readData = self.readData(filePath)
        processedData = self.processedData(readData)
        self.processedFile = collections.Counter(processedData)

        self.items = self.numberOfData(nData)
        self.sumOfItems = sum(self.getItems(self.items)[1])
        self.sumOfAllItems = sum(self.processedFile.values())
        self.percentOfData = round((self.sumOfItems/self.sumOfAllItems)*100,2)



if __name__ == "__main__":
    v = View("alice.txt",10)
    # v.graphVisualize()  
    v.pieVisualize()
    