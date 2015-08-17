#!/usr/bin/env python

import sys

def main():
    if len(sys.argv) < 4:
        print "./split_file.py <input_file> <vector_file> <label_file>"

    infile = open(sys.argv[1])
    vectorfile = open(sys.argv[2], 'w')
    labelfile = open(sys.argv[3], 'w')

    for line in infile:
        arr = line.split()
	word = arr.pop(0)

	labelfile.write(word + '\n')
	vectorfile.write(' '.join(arr) + '\n')

    infile.close()
    vectorfile.close()
    labelfile.close()

if __name__ == "__main__":
    main()
