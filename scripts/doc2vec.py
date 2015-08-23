#!/usr/bin/pypy

import sys
import utilities

# This file will compute a vector representation
# of each document, based on the words in that document.

def readInput():
    if len(sys.argv) < 4:
        print "./doc2vec.py <cluster_file> <vector_file> <doc_file> <output_file>"
        sys.exit()

    clustFileName = sys.argv[1]
    vecFileName = sys.argv[2]
    docFileName = sys.argv[3]
    outFileName = sys.argv[4]

    return clustFileName, vecFileName, docFileName, outFileName

def vectorizeDocs(docFileName, word2clust, numclusters):
    infile = open(docFileName)
    documents = []
    vocab = set(word2clust.getVocab())

    i = 0
    for line in infile:
        i += 1
        if i % 1000 == 0:
            print i

        arr = line.split()
        arr.pop(0) # discard the topic name

        # compute total similarity document to each cluster
        docvec = [0.0] * numclusters
        for word in arr:
            if word in vocab:
                clusterSims = word2clust.getVector(word)
                for i in range(0, numclusters):
                    docvec[i] += clusterSims[i]

        documents.append(docvec)

    infile.close()
    return documents

def writeDocVecs(documents, outFileName):
    outfile = open(outFileName, 'w')

    for doc in documents:
        stringDoc = [str(dim) for dim in doc]
        outfile.write(' '.join(stringDoc) + '\n')

    outfile.close()

def main():
    # read input
    clustFileName, vecFileName, docFileName, outFileName = readInput()

    # read in the vector file
    vectors = utilities.readVectors(vecFileName)

    # read in cluster file
    clusters = utilities.readClusters(clustFileName)

    # compute the similarity of each word to each cluster
    word2clust = utilities.wordClusterVectors(vectors, clusters)

    # for each doc, compute the vector
    documents = vectorizeDocs(docFileName, word2clust, len(clusters))

    # write the doc vectors to file
    writeDocVecs(documents, outFileName)

if __name__ == "__main__":
    main()
