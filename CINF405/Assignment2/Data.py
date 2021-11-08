# Zach Taylor - CINF405 Advanced Concepts and Practices in Software Development

import csv


class Data:  # Creates GetData Class
    statedict = {}

    def __init__(self):  # Instantiates class
        self.__self = self

    def create_dictionary(self):  # Defines a function
        with open('us_avg_tuition.csv', 'r') as f:  # Open csv file
            next(f)  # Skip first line
            reader = csv.reader(f)  # Read each line in file. Creates list for each line
            statedict = {}
            for line in reader:  # Loop through each list in reader
                v = []  # Resets v to empty list after going through each line
                for x in line:  # Loop through each item inside list
                    value = ''.join(filter(str.isalnum, x))  # Filter out anything not alphanumeric
                    v.append(value)  # Append clean data to v
                    self.statedict[v[0]] = v[1:13]  # Sets index 0 to key, index 1-12 as value in list form
