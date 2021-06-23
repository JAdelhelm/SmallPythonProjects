import re
from collections import Counter

def count_words(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r"[!&@$%^.:]","",sentence)
    sentence = sentence.replace("_"," ")
    sentence = sentence.replace(","," ").split()
    sentence = removeQutation(sentence)
    return Counter(sentence)

def removeQutation(sentence):
    temp = []
    for char in sentence:
        if char.startswith('\'') or char.endswith('\''):
            char = re.sub(r"\'","",char)
            temp.append(char)
        else:
            temp.append(char)
    return temp
