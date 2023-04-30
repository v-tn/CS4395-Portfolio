# Portfolio Chapter 8: N-grams
# File Name:    hw3_vtn180000_program_2.py
# Name:         Vincent Nguyen
# NetID:        VTN180000
# Course:       CS 4395.001
# Description: This program unpickles the bigrams and unigrams dictionary. Then, it calculates probability
#              for each of the languages.

import sys
import nltk
import pickle
import math
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

# Main function
if __name__ == '__main__':
    # Unpickle the English unigram and bigrams dictionary
    uni_english = pickle.load(open('unigrams.English.p', 'rb'))
    bi_english = pickle.load(open('bigrams.English.p', 'rb'))

    # Unpickle the French unigram and bigrams dictionary
    uni_french = pickle.load(open('unigrams.French.p', 'rb'))
    bi_french = pickle.load(open('bigrams.French.p', 'rb'))

    # Unpickle the Italian unigram and bigrams dictionary
    uni_italian = pickle.load(open('unigrams.Italian.p', 'rb'))
    bi_italian = pickle.load(open('bigrams.Italian.p', 'rb'))

