import re
from collections import Counter

class Wcounter():
    def __init__(self, sentence):
        self.sentence = sentence
        #print("Wcounter: ",self.sentence)

    def count_words(self):
        self.sentence = self.sentence.lower()
        self.sentence = re.sub(r"[!&@$%^.:]","",self.sentence)
        self.sentence = self.sentence.replace("_"," ")
        self.sentence = self.sentence.replace(","," ").split()
        self.sentence = Wcounter(self.sentence).removeQutation()
        return Counter(self.sentence)

    def removeQutation(self):
        temp = []
        for char in self.sentence:
            if char.startswith('\'') or char.endswith('\''):
                char = re.sub(r"\'","",char)
                temp.append(char)
            else:
                temp.append(char)
        return temp
