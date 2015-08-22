#!/usr/bin/env python

# stores the vector corresponding
# to a given word
class WordVectorDict:
    def __init__(self):
        self.size = 0
        self.word2index = {}
        self.vectors = []

    def addWord(self, word, vector):
        self.word2index[word] = self.size
        self.size += 1
        self.vectors.append(vector)

    def getVector(self, word):
        if word in self.word2index:
            return self.vectors[self.word2index[word]]
        else:
            return None

    def getVocab(self):
        return self.word2index.keys()
