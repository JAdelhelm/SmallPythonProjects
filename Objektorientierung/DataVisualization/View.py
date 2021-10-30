"""Is used to visualize graphs"""
from Model import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
class View(Model):
    def __init__(self):
        super().__init__()
        self.sumOfItems = sum(self.getItems(self.items)[1])
        self.sumOfAllItems = sum(self.processedFile.values())
        self.percentOfData = round((self.sumOfItems/self.sumOfAllItems)*100,2)

    def graphVisualize(self):
        plt.plot(self.getItems(self.items)[0], self.getItems(self.items)[1])
        plt.xlabel("Words")
        plt.ylabel("Number")
        plt.title("Visualization of data by Jörg Adelhelm")
        plt.show()

    def pieVisualize(self):
        if self.items > 3: explodePie = [0.2]+[0.2]+[0.2]+ [0 for val in range(3,self.items)]
        else: explodePie = [0 for val in range(0,self.items)]
        plt.pie(self.getItems(self.items)[1],labels=self.getItems(self.items)[0], shadow=True, startangle=90, explode=explodePie)
        plt.xlabel(f"\nExploded items take {self.percentOfData} % of all data")
        plt.show()

    def getItems(self, items):
        itemsOfData = self.processedFile.most_common(items)
        listWords = []
        listNums = []
        for word, num in itemsOfData:
            listWords.append(word)
            listNums.append(num)
        return tuple(listWords), tuple(listNums)

v = View()
# v.graphVisualize()
v.pieVisualize()
