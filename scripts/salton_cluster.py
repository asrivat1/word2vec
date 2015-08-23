#!/usr/bin/pypy

# This file takes in a file containing high dimensional
# vectors as outputted by word2vec, a seed word, and a
# clustering threshold, and clusters the vectors according
# to Salton's method.

import utilities
import sys
from WordVectorDict import WordVectorDict

class Cluster:
    def __init__(self, vector, word):
        self.centroid = []
        for dim in vector:
            self.centroid.append(dim)

        self.size = 1.0
        self.words = [word]

    def addVector(self, vector, word):
        self.centroid = [self.size * dim for dim in self.centroid]
        self.centroid = [z[0] + z[1] for z in zip(self.centroid, vector)]
        self.centroid = [dim / self.size for dim in self.centroid]

        self.words.append(word)

    def getCentroid(self):
        return self.centroid

    def simToVec(self, vector):
        return utilities.cosineSim(vector, self.centroid)

    def getWords(self):
        return self.words

def readInput():
    if len(sys.argv) < 5:
        print "./salton_cluster.py <vector_file> <seed_word> <threshold> <output_file> [--verbose]"
        sys.exit()

    vecFileName = sys.argv[1]
    seed = sys.argv[2]
    threshold = float(sys.argv[3])
    clustFileName = sys.argv[4]

    return vecFileName, seed, threshold, clustFileName

def clusterWords(order, vectors, threshold):
    clusters = []
    for i in range(0, len(order)):
        word = order[i]
        wordVector = vectors.getVector(word)

        # compare to each centroid
        maxSim = float("-inf")
        maxCluster = None
        for cluster in clusters:
            sim = cluster.simToVec(wordVector)
            if sim > maxSim:
                maxCluster = cluster
                maxSim = sim

        # either add to closest or make new cluster
        if maxCluster is not None and maxSim > threshold:
            maxCluster.addVector(wordVector, word)
        else:
            newCluster = Cluster(wordVector, word)
            clusters.append(newCluster)

    return clusters

def main():
    vecFileName, seed, threshold, clustFileName = readInput()

    # read in data
    vectors = utilities.readVectors(vecFileName)

    # pre-order the data based on the seed
    seedSim = lambda word: utilities.cosineSim(vectors.getVector(word), vectors.getVector(seed))
    order = sorted(vectors.getVocab(), key = seedSim, reverse = True)

    # assign each word to a cluster
    clusters = clusterWords(order, vectors, threshold)

    # write results to file
    clustFile = open(clustFileName, 'w')
    for cluster in clusters:
        stringCentroid = [str(dim) for dim in cluster.getCentroid()]
        clustFile.write(" ".join(stringCentroid) + '\n')

        # print results to std out
        if "--verbose" in sys.argv:
            print cluster.getWords()

    clustFile.close()

if __name__ == "__main__":
    main()
