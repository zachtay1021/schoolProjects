# Zachary Taylor - CINF405 Advanced Concepts and Practices in Software Development

import getData


class RAM:  # creates ram class
    def __init__(self):
        self.__self = self
        self.clean_ram = {}

    def clean_dict(self):
        ram = getData.Data()  # instantiate Data class
        ram = ram.create_ram_dict()  # creates ram dictionary from Data class

        for key, value in ram.items():  # iterate over ram dictionary
            if len(value) == 1:  # if the value's length is equal to 1 (checks to see if list has only 1 number)
                self.clean_ram[key] = value  # set key and value in new dictionary
            else:
                len_of_list = len(value)  # gets length of value list
                valueSum = (sum(map(int, value)))  # sets each entry in list equal to an integer and getting sum
                avg_trans_count = str(round((valueSum / len_of_list), 2))  # finds average by dividing total sum by length of list. round to 2 decimal places
                self.clean_ram[key] = [avg_trans_count]  # set key and value in new dictionary
        return self.clean_ram

    def avg_perc_inc(self):
        self.clean_dict()

        year1 = 1963  # sets year1 equal to first year in dataset
        year2 = year1 + 1

        while year2 < 2019:
            for x, y in self.clean_ram.items():  # iterate through dictionary
                if str(year1) in self.clean_ram.keys():  # checks if year1 is a key
                    if str(year2) in self.clean_ram.keys():  # checks if year2 is a key
                        val1 = self.clean_ram[str(year1)]  # sets val1 equal to value of key
                        val2 = self.clean_ram[str(year2)]  # sets val2 equal to value of key
                        val1 = float(val1[0])  # sets val1 and val2 to a float
                        val2 = float(val2[0])
                        avg_num = (((val2 - val1) / val1) * 100)  # calculates change between val1 and val2
                        avg_num = round(avg_num, 2)  # round avg to 2 decimals
                        print('The average percentage increase in number of transistors between {} and {} in RAM is {}%'.format(year1, year2, avg_num))

                year1 += 1
                year2 += 1

    def two_year_inc(self):
        self.clean_dict()

        year1 = 1963
        year2 = year1 + 2

        while year2 < 2019:
            for x, y in self.clean_ram.items():  # iterate through dictionary
                if str(year1) in self.clean_ram.keys():  # checks if year1 is a key
                    if str(year2) in self.clean_ram.keys():  # checks if year2 is a key
                        val1 = self.clean_ram[str(year1)]  # sets val1 equal to value of key
                        val2 = self.clean_ram[str(year2)]  # sets val2 equal to value of key
                        val1 = float(val1[0])  # sets val1 and val2 to a float
                        val2 = float(val2[0])
                        avg_num = (((val2 - val1) / val1) * 100)  # calculates change between val1 and val2
                        avg_num = round(avg_num, 2)  # round avg to 2 decimals
                        print('The average percentage increase in number of transistors between {} and {} in RAM is {}%'.format(year1, year2, avg_num))

                year1 += 1
                year2 += 1
