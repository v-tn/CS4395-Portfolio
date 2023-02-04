# Portfolio Assignment 1: Text Processing
# File Name:    hw1_vtn180000.py
# Name:         Vincent Nguyen
# NetID:        VTN180000
# Course:       CS 4395.001
# Description:  This program reads employees data from a file and processes the data. The program will
#               fix any mistake the data has. In the end, the program will display the id, first name, middle initial,
#               last name, and phone number.

import sys
import pathlib
import re
import pickle


# Class for a person
class Person:
    def __init__(self, last, first, mi, ids, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.ids = ids
        self.phone = phone

    # Function to display results to screen
    def display(self):
        print('Employee id: ', self.ids)
        print('\t', self.first, self.mi, self.last)
        print('\t', self.phone)
        print()


# Function to read file and input the lines into a list of object
def read_file():

    # Counter variable to count total amount of lines in file
    counter = 0

    # Open file and read csv file
    with open(sys.argv[1], mode='r') as data:
        data_line = data.read().splitlines()

        # For loop to count number of lines in variable
        for count_num in data_line:
            counter += 1

        # Create list of objects
        persons = [Person for count_num in range(counter - 1)]

        # Two more counters for the for loop
        # counter_second is for a counter for the list of objects
        # counter_third is for a counter for the lines we split already. Set to 1 to skip header line
        counter_second = 0
        counter_third = 1

        # Loop to get last, first, mi, id, phone from file line
        for count_num in range(1, counter):

            # Split the commas to get last, first, mi, id, and phone
            line = data_line[counter_third].split(',')

            # Put last, first, mi, id, and phone into object in the list of object
            persons[counter_second] = Person(line[0], line[1], line[2], line[3], line[4])

            # Increase both counters to get next line in file and next object in list of object
            counter_second += 1
            counter_third += 1

    # Return list of objects
    return persons


# Function to process text
def process(objs):

    count = 0

    # Loop to capitalize and lowercase letters in first name, last name, and middle initial
    for count_num in objs:
        # Capitalize first letter in last name and lower case the rest of the letters
        objs[count].last = objs[count].last.lower()
        objs[count].last = objs[count].last.capitalize()

        # Capitalize first letter in first name and lower case the rest of the letters
        objs[count].first = objs[count].first.lower()
        objs[count].first = objs[count].first.capitalize()

        # Capitalize middle initial
        objs[count].mi = objs[count].mi.capitalize()

        # Input X into mi variable if there is nothing in variable
        if objs[count].mi == "":
            objs[count].mi = 'X'

        # Increase variable by 1 to access rest of list of objects
        count += 1

    return objs


# Main function to execute code
if __name__ == "__main__":

    counters = 0

    # Check if user input data/data.csv in sysarg
    if len(sys.argv) == 1:
        print('Please input correct file name in system arg')
        quit()

    # Call function to read file and return list of objects from the function
    obj = read_file()

    # Call function to process text and fix any mistake in data
    obj = process(obj)

    # Loop to display results
    for i in obj:

        # Call function to display results
        obj[counters].display()
        counters += 1
