# Portfolio Assignment 1: Text Processing
# File Name:    hw1_vtn180000.py
# Name:         Vincent Nguyen
# NetID:        VTN180000
# Course:       CS 4395.001
# Description:  This program reads employees data from a file and processes the data. The program will
#               fix any mistake the data has. In the end, the program will display the id, first name, middle initial,
#               last name, and phone number.

import sys
import re
import pickle


# Class for a person
class Person:

    # Constructor
    def __init__(self, last, first, mi, ids, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.ids = ids
        self.phone = phone

    # Function to display results to screen
    def display(self):
        print('Employee id:', self.ids)
        print('\t', self.first, self.mi, self.last)
        print('\t', self.phone)
        print()


# Function to read file and get lines from file
def read_file():

    # Open file and read csv file
    with open(sys.argv[1], mode='r') as data:
        data_line = data.read().splitlines()

    # Close file
    data.close()

    # Return lines
    return data_line


# Function to process text
def process(lines):

    counter = 0
    error = -1
    dict_one = {}

    # For loop to count number of lines gotten from file
    for count_line in lines:
        counter += 1

    # counter_second is for a counter for the lines we split. Set to 1 to skip header line
    counter_second = 1

    # Loop to get last, first, mi, id, phone from file line
    for num in range(1, counter):

        # Split the commas to get last, first, mi, id, and phone
        line_data = lines[counter_second].split(',')

        # Lower case the letters then capitalize first letter in last name
        line_data[0] = line_data[0].lower()
        line_data[0] = line_data[0].capitalize()

        # Lower case the letters then capitalize first letter in first name
        line_data[1] = line_data[1].lower()
        line_data[1] = line_data[1].capitalize()

        # Capitalize first letter in middle initial
        line_data[2] = line_data[2].capitalize()

        # Put 'X' as the middle initial if there is no middle initial from data file
        if line_data[2] == "":
            line_data[2] = 'X'

        # Loop to make sure the id is valid
        while error != 0:

            # Error counter is set to 0 for a fresh start to properly error check
            error = 0

            # Check if the id is within 6 characters
            if len(line_data[3]) < 6:
                error += 1

            # Check if first two characters in id is letters and capitalized
            elif not line_data[3][0].isalpha() or not line_data[3][1].isalpha() or not line_data[3][0].isupper() \
                    or not line_data[3][1].isupper():
                error += 1

            # Check if last four characters in id is a number
            elif not line_data[3][2].isnumeric() or not line_data[3][3].isnumeric() or not line_data[3][4].isnumeric() \
                    or not line_data[3][5].isnumeric():
                error += 1

            # Print out message to user and get valid id back from user
            if error != 0:

                # Print out message to user to let them know of the error
                print("ID", line_data[3], "is invalid.")
                print("ID has two letters capitalized first, then four numbers. Example: SA1234 is a valid ID")
                print("Please enter valid ID: ")

                # Get user input back and replace non-valid id with the id the user input in
                user_input = input()
                line_data[3] = re.sub("[A-Z]+[0-9]*", user_input, line_data[3])

        # Error counter set back to -1 to let while loop check phone number
        error = -1

        # Loop to check if the phone number is in the correct form
        while error != 0:

            # Error counter is set to 0 for a fresh start to properly error check
            error = 0

            # Check if the phone number has 12 characters
            if len(line_data[4]) < 12:
                error += 1

            # Check if there is a dash after the first three numbers, then another dash three numbers after first dash
            elif not line_data[4][3] == '-' or not line_data[4][7] == '-':
                error += 1

            # Check if the numbers are in its correct spot. So this checks if there is three numbers first, then
            # another three numbers after the first dash, then four numbers after the second dash
            elif not line_data[4][0].isnumeric() or not line_data[4][1].isnumeric() or not line_data[4][2].isnumeric() \
                    or not line_data[4][4].isnumeric() or not line_data[4][5].isnumeric() \
                    or not line_data[4][6].isnumeric() or not line_data[4][8].isnumeric() \
                    or not line_data[4][9].isnumeric() or not line_data[4][10].isnumeric() \
                    or not line_data[4][11].isnumeric():
                error += 1

            # Output error message to user and get valid phone number from user
            if error != 0:

                # Output error message to user
                print("Phone number", line_data[4], "is invalid.")
                print("Phone number has three numbers, then a dash, then three numbers, then a dash, then four numbers")
                print("Please enter valid phone number: ")

                # Get user input and replace phone number with the phone number the user input
                user_input = input()
                line_data[4] = re.sub("^[0-9]+\\-*\\s*\\.*\\?*\\**[0-9]+\\-*\\s*\\.*\\?*\\**[0-9]*", user_input,
                                      line_data[4])

        # Set error counter back to -1 to let while loop check for id once the for loop loops again
        error = -1

        # Put last, first, mi, id, and phone into class object
        persons = Person(line_data[0], line_data[1], line_data[2], line_data[3], line_data[4])

        # Check if there is duplicate keys, and if there are, output error message
        for key in dict_one:
            if key == persons.ids:
                print("Duplicate id", persons.ids, "detected in file")

        # Add object into dictionary
        dict_one[persons.ids] = persons

        # Increase both counters to get next line in file
        counter_second += 1

    # Return dictionary to main function
    return dict_one


# Main function to execute code
if __name__ == "__main__":

    counters = 0

    # Check if user input data/data.csv in sysarg
    if len(sys.argv) == 1:
        print('Please input correct file name in system arg')
        quit()

    # Call function to read file and return lines gotten from file from the function
    line = read_file()

    # Call function to process text and fix any mistake in data
    data_dict = process(line)

    # Create pickle file and write dictionary into file
    pickle.dump(data_dict, open('employee.p', 'wb'))

    # Read pickle file
    read_dict = pickle.load(open('employee.p', 'rb'))

    # Loop to display results
    for count_num in read_dict:

        # Call function to display results
        read_dict[count_num].display()