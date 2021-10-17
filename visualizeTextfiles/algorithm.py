import re
import collections
import time
class algorithmWords():
    def __init__(self, sentence):
        self.sentence = sentence

    def countWords(self):
        try:
            start = time.perf_counter_ns()
            # Performance test
            #
            self.sentence = self.sentence.lower()
            self.sentence = re.sub(r"[!&@$%^.:]","",self.sentence)
            self.sentence = re.sub(r"[-,]"," ",self.sentence).split()
            self.sentence = algorithmWords(self.sentence).removeQutation()    
            dictWords = collections.Counter(self.sentence)
            #
            # Performance test
            # end = time.perf_counter_ns()
            # print(f"The function ran {end-start} nanoseconds")
            return dictWords
        except: return ""

    def removeQutation(self):
        temp = []
        for char in self.sentence:
            if char.startswith('\'') or char.endswith('\''):
                char = re.sub(r"\'","",char)
                temp.append(char)
            else:
                temp.append(char)
        return temp

# algoWords = algorithmWords("Das ist,ein-Testtext")
# print(algoWords.countWords())