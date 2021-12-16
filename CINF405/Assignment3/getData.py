# Zachary Taylor - CINF405 Advanced Concepts and Practices in Software Development

import csv


class Data:  # Creates Data class
    gpuDict = {}
    ramDict = {}

    def __init__(self):
        self.__self = self

    def create_cpu_dict(self):
        with open('cpu.csv', 'r') as cpu_data:  # Open cpu csv file
            next(cpu_data)  # Skip first line
            reader = csv.reader(cpu_data)  # Read each line in file. Creates list for each line
            cpuDict = {}

            for line in reader:  # Loop through each list in reader
                if line[1] == 'NA':
                    continue  # Skips adding to dictionary if value equals 'NA'
                else:
                    if line[2] in cpuDict:  # Checks to see if the year is already a key
                        cpuDict[line[2]].append(line[1])  # Appends the value to the key
                    else:
                        cpuDict[line[2]] = [line[1]]
        return cpuDict

    def create_gpu_dict(self):
        with open('gpu.csv', 'r') as gpu_data:  # Open gpu csv file
            next(gpu_data)  # Skip first line
            reader = csv.reader(gpu_data)  # Read each line in file. Creates list for each line
            gpuDict = {}

            for line in reader:  # Loop through each list in reader
                if line[1] == 'NA':
                    continue  # Skips adding to dictionary if value equals 'NA'
                if line[2] == 'NA':
                    continue  # Skips adding to dictionary if value equals 'NA'
                else:
                    if line[2] in gpuDict:  # Checks to see if the year is already a key
                        gpuDict[line[2]].append(line[1])  # Appends the value to the key
                    else:
                        gpuDict[line[2]] = [line[1]]
        return gpuDict

    def create_ram_dict(self):
        with open('ram.csv', 'r') as ram_data:  # Open ram csv file
            next(ram_data)  # Skip first line
            reader = csv.reader(ram_data)  # Read each line in file. Creates list for each line
            ramDict = {}

            for line in reader:  # Loop through each list in reader
                if line[4] == 'NA':
                    continue  # Skips adding to dictionary if value equals 'NA'
                else:
                    if line[5] in ramDict:  # Checks to see if the year is already a key
                        ramDict[line[5]].append(line[4])  # Appends the value to the key
                    else:
                        ramDict[line[5]] = [line[4]]
        return ramDict
