# Zachary Taylor - CINF405 Advanced Concepts and Practices in Software Development

import getData


class CPU:  # creates cpu class
    def __init__(self):
        self.__self = self
        self.clean_cpu = {}

    def clean_dict(self):
        cpu = getData.Data()  # instantiate Data class
        cpu = cpu.create_cpu_dict()  # creates cpu dictionary from Data class

        for key, value in cpu.items():  # iterate over cpu dictionary
            if len(value) == 1:  # if the value's length is equal to 1 (checks to see if list has only 1 number)
                self.clean_cpu[key] = value  # set key and value in new dictionary
            else:
                len_of_list = len(value)  # gets length of value list
                valueSum = (sum(map(int, value)))  # sets each entry in list equal to an integer and getting sum
                avg_trans_count = str(round((valueSum / len_of_list), 2))  # finds average by dividing total sum by length of list. round to 2 decimal places
                self.clean_cpu[key] = [avg_trans_count]  # set key and value in new dictionary
        return self.clean_cpu

    def avg_perc_inc(self):
        self.clean_dict()

        year1 = 1971  # sets year1 equal to first year in dataset
        year2 = year1 + 1

        while year2 < 2020:
            for x, y in self.clean_cpu.items():  # iterate through dictionary
                if str(year1) in self.clean_cpu.keys():  # checks if year1 is a key
                    if str(year2) in self.clean_cpu.keys():  # checks if year2 is a key
                        val1 = self.clean_cpu[str(year1)]  # sets val1 equal to value of key
                        val2 = self.clean_cpu[str(year2)]  # sets val2 equal to value of key
                        val1 = float(val1[0])  # sets val1 and val2 to a float
                        val2 = float(val2[0])
                        avg_num = (((val2 - val1) / val1) * 100)  # calculates change between val1 and val2
                        avg_num = round(avg_num, 2)  # round avg to 2 decimals
                        print('The average percentage increase in number of transistors between {} and {} in a CPU is {}%'.format(year1, year2, avg_num))

                year1 += 1
                year2 += 1

    def two_year_inc(self):
        self.clean_dict()

        year1 = 1971
        year2 = year1 + 2

        for x, y in self.clean_cpu.items():  # iterate through dictionary
            if str(year1) in self.clean_cpu.keys():  # checks if year1 is a key
                if str(year2) in self.clean_cpu.keys():  # checks if year2 is a key
                    val1 = self.clean_cpu[str(year1)]  # sets val1 equal to value of key
                    val2 = self.clean_cpu[str(year2)]  # sets val2 equal to value of key
                    val1 = float(val1[0])  # sets val1 and val2 to a float
                    val2 = float(val2[0])
                    avg_num = (((val2 - val1) / val1) * 100)  # calculates change between val1 and val2
                    avg_num = round(avg_num, 2)  # round avg to 2 decimals
                    print('The average percentage increase in number of transistors between {} and {} in a CPU is {}%'.format(year1, year2, avg_num))

            year1 += 1
            year2 += 1
