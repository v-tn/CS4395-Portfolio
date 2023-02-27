# Portfolio Assignment 2: Word Guessing
# File Name:    hw2_vtn180000.py
# Name:         Vincent Nguyen
# NetID:        VTN180000
# Course:       CS 4395.001
# Description: This program reads the file contents and tokenizes the file contents. It calculates lexical diversity,
#              number of nouns, number of tokens, and unique lemmas and outputs it to the user. This program also has
#              a word guessing game, where the user guess the letters to find out the word.

import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Function to open and read file
def file_read():

    contents = ''

    # Open file and read contents of file
    with open(sys.argv[1], mode="r") as file:
        contents = file.read()

    # Close file
    file.close()
    return contents


# Function to tokenize the file contents
def tokenize_word(lines):

    list_nouns = []
    counter_nouns = 0
    counter_tokens = 0

    # Tokenize the file
    token_one = word_tokenize(lines)

    # Print out lexical diversity in two decimal places
    # lexical diversity = unique tokens / total tokens
    print("Lexical Diversity: ", round(len(set(token_one)) / len(token_one), 2))

    # Find tokens that are not stopwords, are in the alphabet, and length greater than 5
    token_one = [tokens for tokens in token_one if tokens.isalpha() and len(tokens) > 5 and tokens not in
                 stopwords.words('english')]

    # Get number of tokens
    counter_tokens = len(token_one)

    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    count_lemmas = [lemmatizer.lemmatize(tokens) for tokens in token_one]

    # Get unique lemmas from the lemmatize tokens
    unique = set(count_lemmas)

    # POS Tag the unique lemmas
    tagging = nltk.pos_tag(unique)

    # Print 20 unique lemmas
    print("Unique Lemmas Tagged: ")
    for num in range(20):
        print(tagging[num])

    # Get a copy of tokens
    copy_tokens = token_one

    # Count number of nouns and make a list of words that are nouns
    for token_one, nouns in tagging:
        if nouns == 'NN' or nouns == 'NNS' or nouns == 'NNPS' or nouns == 'NNP':
            counter_nouns = counter_nouns + 1
            list_nouns.append(token_one)

    # Output number of tokens and nouns to screen
    print("Number of tokens: ", counter_tokens)
    print("Number of nouns: ", counter_nouns)

    # Return tokens and list of nouns
    return copy_tokens, list_nouns


# Main function
if __name__ == '__main__':

    nouns_list = []

    # Check if user input file name n sysarg
    if len(sys.argv) == 1:
        print('Please input correct file name in system arg')
        quit()

    # Get file contents
    content = file_read()

    # Tokenize the file contents and get list of nouns and tokens
    contents_tokenize, nouns_list = tokenize_word(content)




