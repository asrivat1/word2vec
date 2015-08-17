# Usage
# ./run-word2vec.sh <corpus_file>

sed -e "s/’/'/g" -e "s/′/'/g" -e "s/''/ /g" < $1 | tr -c "A-Za-z'_ \n" " " > "$1-norm0"

time ./word2phrase -train "$1-norm0" -output "$1-norm0-phrase0" -threshold 200 -debug 2
time ./word2phrase -train "$1-norm0-phrase0" -output "$1-norm0-phrase1" -threshold 100 -debug 2

time ./word2vec -train "$1-norm0-phrase1" -output vectors-phrase.txt -cbow 1 -size 200 -window 10 -negative 25 -hs 0 -sample 1e-5 -threads 20 -binary 0 -iter 15
