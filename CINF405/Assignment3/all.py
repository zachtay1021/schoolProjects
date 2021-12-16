# Zachary Taylor - CINF405 Advanced Concepts and Practices in Software Development

import cpu
import gpu
import ram


class ALL:
    def __init__(self):
        self.__self = self
        self.all_dict = {}

    def create_all_dict(self):
        data1 = cpu.CPU()
        cpu_dict = data1.clean_dict()  # instantiate cpu class, creates cpu dict

        data2 = gpu.GPU()
        gpu_dict = data2.clean_dict()  # instantiate gpu class, creates gpu dict

        data3 = ram.RAM()
        ram_dict = data3.clean_dict()  # instantiate ram class, creates ram dict

        year1 = 1960
        value_list = []

        while year1 < 2021:
            if str(year1) in ram_dict.keys():
                if str(year1) in gpu_dict.keys():
                    if str(year1) in cpu_dict.keys():  # checks to see if year1 value is a key in all three dictionaries (cpu, gpu, and ram)
                        ram_value = ram_dict[str(year1)]  # sets variable equal to value of dictionary key
                        gpu_value = gpu_dict[str(year1)]
                        cpu_value = cpu_dict[str(year1)]
                        value_list.append(ram_value)  # appends value to list
                        value_list.append(gpu_value)
                        value_list.append(cpu_value)

                        for x in value_list:  # iterate through list of values
                            x = (map(float, x))
                            valueSum = (sum(x) / 3)
                            self.all_dict[year1] = round(valueSum, 2)

            year1 += 1

    def avg_perc_inc(self):
        self.create_all_dict()

        year1 = 1960
        year2 = year1 + 1

        while year2 < 2021:
            for x, y in self.all_dict.items():  # iterate through dictionary
                if year1 in self.all_dict.keys():  # checks if year1 is a key
                    if year2 in self.all_dict.keys():  # checks if year2 is a key
                        val1 = self.all_dict[year1]  # sets val1 equal to value of key
                        val2 = self.all_dict[year2]  # sets val2 equal to value of key
                        val1 = float(val1)  # sets val1 and val2 to a float
                        val2 = float(val2)
                        avg_num = (((val2 - val1) / val1) * 100)  # calculates change between val1 and val2
                        avg_num = round(avg_num, 2)  # round avg to 2 decimals
                        print('The average percentage increase in number of transistors between {} and {} in CPU, GPU, and RAM is {}%'.format(year1, year2, avg_num))

                year1 += 1
                year2 += 1

    def two_year_inc(self):
        self.create_all_dict()

        year1 = 1960
        year2 = year1 + 2

        while year2 < 2021:
            for x, y in self.all_dict.items():  # iterate through dictionary
                if year1 in self.all_dict.keys():  # checks if year1 is a key
                    if year2 in self.all_dict.keys():  # checks if year2 is a key
                        val1 = self.all_dict[year1]  # sets val1 equal to value of key
                        val2 = self.all_dict[year2]  # sets val2 equal to value of key
                        val1 = float(val1)  # sets val1 and val2 to a float
                        val2 = float(val2)
                        avg_num = (((val2 - val1) / val1) * 100)  # calculates change between val1 and val2
                        avg_num = round(avg_num, 2)  # round avg to 2 decimals
                        print('The average percentage increase in number of transistors between {} and {} in CPU, GPU, and RAM is {}%'.format(year1, year2, avg_num))

                year1 += 1
                year2 += 1
