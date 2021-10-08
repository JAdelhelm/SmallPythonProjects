import re
from collections import Counter
import itertools

class algorithmWords():
    def __init__(self, sentence):
        self.sentence = sentence

    def countWords(self, numberWords):
        try:
            self.numberWords = numberWords
            self.sentence = self.sentence.lower()
            self.sentence = re.sub(r"[!&@$%^.:]","",self.sentence)
            self.sentence = self.sentence.replace("_"," ")
            self.sentence = self.sentence.replace(","," ").split()
            self.sentence = algorithmWords(self.sentence).removeQutation()
            allWords = len(self.sentence)
            print("\nSum of Words: ",allWords,"\n")
            print(f"Showing first sorted {self.numberWords} words:\n")
            dictWords = dict(Counter(self.sentence))
            dictWords = sorted(dictWords.items(), key=lambda x: x[1], reverse=True)
            print(dictWords[:self.numberWords])
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