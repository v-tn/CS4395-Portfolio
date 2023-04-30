# Class-Portfolio
Portfolio for CS 4395 for Vincent Nguyen

# Overview of NLP
This is a pdf document that shows an overview of NLP. You can see the [pdf document here](Overview_Of_NLP.pdf).

# Program 1
Program 1 is a program that reads a csv file comtaining employees id, first name, last name, middle initial, and phone number and processes it. The program should fix any mistake in the data and display the results. You can see program 1 [here](hw1_vtn180000.py). To run it, you need a csv file name "data.csv" inside a folder named data. Furthermore, you need to make sure the file path is in sysarg. There are some strengths for text processing in Python. The first is that it is easy to edit lines. You can split the lines up after reading in lines from the file. Also, you can lower case and capitalize letters in lines. 

I realized I learned a lot after writing program 1. Before, I never had experience with writing Python. Now, I know how to read a file in Python. Furthermore, I now know how to edit letters and lines in Python.

# Program 2
Program 2 reads the file contents and tokenizes the file contents. The program outputs unique lemmas, calculates lexical diversity, count nouns in the file, and does other things as well. The program is also a word guessing game. You can see program 2 [here](hw2_vtn180000.py).

# WordNet
This is a pdf document that shows an overview of WordNet, SentiWordNet, Morphy, and Collocation. You can see the [pdf document here](wordnet.pdf).

# N-Gram Language Model Program and Report
There are two programs for the N-Gram. [This](hw3_vtn180000_program_1.py) is the first program. The first program reads in a csv file and then tokenizes the text. After that, the program creates a bigram and unigram list. Lastly, the program creates two dictionary from the two lists and then pickles them. The [second program](hw3_vtn180000_program_2.py) reads in the pickles from the first program and unpickles them. The [N-Gram report](vtn180000.N-Grams.pdf) is a pdf document that talks about N-Grams, describing what they are and how are they important. 

# Web Crawler Program
This program utilizes the web crawler to search for the wikipedia page on ice hockey. Then it uses the web scraping function to download all the urls on the ice hockey wikipedia page into several text files. Lastly, the program cleans up the text files using the tokenizer and finds the top 10 terms to put them in a dictionary. You can see the program [here](vtn180000-hwch12.py)

# Text Classification 1 Report
This is a pdf document that shows how I utilized Naïve Bayes, Logistic Regression, and Neural Networks algorithms for text classification. I used the algorithms to train and test from a [dataset](cleaned_review.csv). You can see the [pdf document here](vtn180000-text_classification_hw_-1.pdf)

# ACL Paper Summary Report
This is a pdf document that summarizes "Contextual Representation Learning beyond Masked Language Modeling" which is an ACL paper that was published in 2022. You can see the report [here](VTN180000-ACL Paper Summary-1.pdf).

# Text Classification 2 Report
This is a pdf document that shows how I utilized the sequential model, RNN, and embeddings for text classification from a [dataset](cleaned_review.csv). You can see the [pdf document here](vtn180000-text_classification_2_hw.pdf).

# Chatbot Program and Report 
This program utilizes the OpenAI API to use as a chatbot to respond to the user. The program uses the web scrape to scrape two web pages, one about basketball and the other about ice hockey. Then the program cleans up the text files and sends it to the chatbot when the user asks about the origin of basketball or ice hockey. The program also utilizes NER (named entity recognition) to keep track of the user name. You can see the program [here](chatbot.py). The chatbot report is a report over the chatbot program. The report gives an overview of the program and also talks about its strengths and weaknesses. You can see the report [here](Chatbot Report.pdf).
