# Portfolio Chapter 8: N-grams
# File Name:    hw3_vtn180000_program_1.py
# Name:         Vincent Nguyen
# NetID:        VTN180000
# Course:       CS 4395.001
# Description: This program reads in a file. Then it creates bigrams and unigrams from the file read in.
#              After that, the program creates dictionary of both unigrams and bigrams and pickles both of them.

import sys
import nltk
import pickle
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

# Function to read file and create bigrams and unigrams
def file_in():

    # Open file and read it
    with open(sys.argv[1], mode='r') as language:
        line = language.read()

    # Close file
    language.close()

    # Tokenize the lines gotten from file
    token_contents = word_tokenize(line)

    # Create unigrams and bigrams
    uni = list(ngrams(token_contents, 1))
    bi = list(ngrams(token_contents, 2))

    # Create dictionary from unigrams and bigrams
    dict_uni = {unigrams: uni.count(unigrams) for unigrams in set(uni)}
    dict_bi = {bigrams: bi.count(bigrams) for bigrams in set(bi)}

    # Return bigrams and unigrams dictionary
    return dict_uni, dict_bi


# Function to pickle the unigrams and bigrams dictionary
def pickle_dict(uni_dict, bi_dict):
    # Pickle the English unigrams and english bigrams
    if sys.argv[1] == "LangId.train.English":
        pickle.dump(uni_dict, open('unigrams.English.p', 'wb'))
        pickle.dump(bi_dict, open('bigrams.English.p', 'wb'))

    # Pickle the French unigrams and french bigrams
    if sys.argv[1] == "LangId.train.French":
        pickle.dump(uni_dict, open('unigrams.French.p', 'wb'))
        pickle.dump(bi_dict, open('bigrams.French.p', 'wb'))

    # Pickle the Italian unigrams and italian bigrams
    if sys.argv[1] == "LangId.train.Italian":
        pickle.dump(uni_dict, open('unigrams.Italian.p'), 'wb')
        pickle.dump(bi_dict, open('bigrams.Italian.p'), 'wb')


# Main function
if __name__ == '__main__':
    # Call functions to read in file, create bigrams and unigrams and their dictionary, and pickle them
    dict_one, dict_two = file_in()
    pickle_dict(dict_one, dict_two)


