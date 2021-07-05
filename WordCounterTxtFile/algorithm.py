import re
from collections import Counter
import itertools

class Wcounter():
    def __init__(self, sentence):
        self.sentence = sentence
        #print("Wcounter: ",self.sentence)

    def countWords(self):
        try:
            self.sentence = self.sentence.lower()
            self.sentence = re.sub(r"[!&@$%^.:]","",self.sentence)
            self.sentence = self.sentence.replace("_"," ")
            self.sentence = self.sentence.replace(","," ").split()
            self.sentence = Wcounter(self.sentence).removeQutation()
            dictWords = dict(Counter(self.sentence))
            dictWords = dict(itertools.islice(dictWords.items(),50))
            dictWords = sorted(dictWords.items(), key=lambda x: x[1], reverse=True)
            return dictWords
        except:
            return ""


    def removeQutation(self):
        temp = []
        for char in self.sentence:
            if char.startswith('\'') or char.endswith('\''):
                char = re.sub(r"\'","",char)
                temp.append(char)
            else:
                temp.append(char)
        return temp
