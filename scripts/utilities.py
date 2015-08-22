#!/usr/bin/env python

from WordVectorDict import WordVectorDict

def readVectors(vecFileName):
    infile = open(vecFileName)

    word_vec = WordVectorDict()

    for line in infile:
        arr = line.split()
        word = arr.pop(0)
        vec = [float(num) for num in arr]

        word_vec.addWord(word, vec)

    infile.close()
    return word_vec

def dot(vec1, vec2):
    return float(sum([z[0] * z[1] for z in zip(vec1, vec2)]))

def norm(vec):
    return float(sum([dim ** 2 for dim in vec]) ** 0.5)

def cosineSim(vec1, vec2):
    dotProd = dot(vec1, vec2)
    normProd = norm(vec1) * norm(vec2)

    return dotProd / normProd
