#!/usr/bin/pypy

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

def readClusters(clustFileName):
    infile = open(clustFileName)

    clusters = []

    for line in infile:
        arr = line.split()
        vec = [float(num) for num in arr]

        clusters.append(vec)

    infile.close()
    return clusters

def wordClusterVectors(vectors, clusters):
    word2clust = WordVectorDict()

    for word in vectors.getVocab():
        vec = []
        for cluster in clusters:
            sim = cosineSim(vectors.getVector(word), cluster)
            vec.append(sim)

        word2clust.addWord(word, vec)

    return word2clust

def dot(vec1, vec2):
    return float(sum([z[0] * z[1] for z in zip(vec1, vec2)]))

def norm(vec):
    return float(sum([dim ** 2 for dim in vec]) ** 0.5)

def cosineSim(vec1, vec2):
    dotProd = dot(vec1, vec2)
    normProd = norm(vec1) * norm(vec2)

    return dotProd / normProd
