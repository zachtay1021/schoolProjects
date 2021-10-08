# Zach Taylor - CINF405 Advanced Concepts and Practices in Software Development

def main():  # Creates the main loop. User will only interact with this function
    exitFalse = True
    while exitFalse:  # Continues to run until exitFalse is set to False
        print('''
            This program displays mask wearing data during the COVID-19 pandemic during the Summer of 2020 in the United States. 
            Data is displayed for a specific state or the entire Country.

            1) Entire United States
            2) Specific State
            3) Exit
            ''')
        userInput = int(input('Please select one of the above options: '))

        if userInput == 1:
            option_1()
        elif userInput == 2:
            option_2()
        elif userInput == 3:
            print('Exiting')
            exitFalse = False  # Closes the main while loop
        else:
            print('Invalid input')  # If the user inputs something other than one of the above options, print an error


def usdata():  # Function to get entire us data percentages
    maskuse = open('mask-use-by-county.csv', 'r')  # opens mask use file
    stategeo = open('State-geocodes-v2018.csv', 'r')  # opens state geocode file

    next(maskuse)  # skips first line
    columns = []  # set up lists to be used later
    never = []
    rarely = []
    sometimes = []
    frequently = []
    always = []

    for line in maskuse:  # iterate through each line in the mask use file
        columns = line.split(',')  # split each line by a comma
        never.append(columns[1])  # appends specific column in mask use file to list
        rarely.append(columns[2])
        sometimes.append(columns[3])
        frequently.append(columns[4])
        always.append(columns[5])

    never = map(float, never)  # maps each item in list to a float
    neverSum = sum(never) # finds the sum of the list

    rarely = map(float, rarely)
    rarelySum = sum(rarely)

    sometimes = map(float, sometimes)
    sometimesSum = sum(sometimes)

    frequently = map(float, frequently)
    frequentlySum = sum(frequently)

    always = map(float, always)
    alwaysSum = sum(always)

    # Used to find the percentage of each category
    totalSum = (neverSum + rarelySum + sometimesSum + frequentlySum + alwaysSum)

    # format the output to make it look nice
    print('\n')
    print('Nationwide Percentages: {:20} {:20} {:20} {:20} {:20}'.format('Never', 'Rarely', 'Sometimes', 'Frequently', 'Always'))
    print('-' * 120)
    print('{:>28} % {:18} % {:19} % {:18} % {:18} %'.format(round(neverSum / totalSum * 100, 2), round(rarelySum / totalSum * 100, 2), round(sometimesSum / totalSum * 100, 2), round(frequentlySum / totalSum * 100, 2), round(alwaysSum / totalSum * 100, 2)))


def option_1(): # function for county mask percentages
    global countyhighcode, countylowcode
    stategeo = open('State-geocodes-v2018.csv', 'r')  # opens state geocode file

    next(stategeo)  # skips first line
    statedict = {}
    columns = []
    for line in stategeo:
        line = line.replace('\n', '')  # replace any \n with blank space
        columns = line.split(',')
        k, v = columns[1], columns[6]  # sets column index 1 to k, column index 6 to v
        k = k.zfill(2)  # ensures that every k value has 2 digits, if not add leading zero
        statedict[k] = v  # sets up the dictionary
    stategeo.close()

    maskuse = open('mask-use-by-county.csv', 'r')
    next(maskuse)
    statenever = []
    staterarely = []
    statesometimes = []
    statefrequently = []
    statealways = []
    count = 0  # create a count to use for finding percentages
    resultdict = {}
    countyhigh = 0  # create variable to find highest county
    countylow = 99999  # create variable to find lowest county

    for key in statedict.keys():  # for each key in statedict, run through this loop
        for line in maskuse:  # iterate through each line of mask use file
            columns = line.split(',')
            if len(columns[0]) == 4:  # if the length of column index 0 is 4, add leading zero. Normalizing the data!
                columns[0] = columns[0].zfill(5)
            if ((columns[0])[0:2]) == key:  # compares first 2 digits in county code to key value
                statenever.append(columns[1])
                staterarely.append(columns[2])
                statesometimes.append(columns[3])
                statefrequently.append(columns[4])
                statealways.append(columns[5])
                count += 1  # adds 1 to count

                countyhighsum = float(columns[4]) + float(columns[5])  # add together frequently and always column
                countyhighsum = round(countyhighsum * 100 / 2, 2)  # find percentage
                if float(countyhighsum) > float(countyhigh):  # if the percentage is greater than countyhigh,
                    # set countyhigh equal to new percentage and grab the county code
                    countyhigh = countyhighsum
                    countyhighcode = columns[0]

                countylowsum = float(columns[1]) + float(columns[2])  # add together rarely and never column
                countylowsum = round(countylowsum * 100 / 2, 2)  # find percentage
                if float(countylowsum) < float(countylow):  # if the percentage is less than countylow, set countylow
                    # equal to new percentage and grab the county code
                    countylow = countylowsum
                    countylowcode = columns[0]

                stateneverfloat = list(map(float, statenever))
                stateneversum = sum(stateneverfloat)
                statenevertotal = round(stateneversum / count * 100, 2)

                staterarelyfloat = list(map(float, staterarely))
                staterarelysum = sum(staterarelyfloat)
                staterarelytotal = round(staterarelysum / count * 100, 2)

                statesometimesfloat = list(map(float, statesometimes))
                statesometimessum = sum(statesometimesfloat)
                statesometimestotal = round(statesometimessum / count * 100, 2)

                statefrequentlyfloat = list(map(float, statefrequently))
                statefrequentlysum = sum(statefrequentlyfloat)
                statefrequentlytotal = round(statefrequentlysum / count * 100, 2)

                statealwaysfloat = list(map(float, statealways))
                statealwayssum = sum(statealwaysfloat)
                statealwaystotal = round(statealwayssum / count * 100, 2)

                # creates the result dictionary. key is state code, value is list of data from above
                resultdict[key] = [statenevertotal, staterarelytotal, statesometimestotal, statefrequentlytotal, statealwaystotal, countyhigh, countyhighcode, countylow, countylowcode]

            else:   # if the key is not equal to the first two digits, do the stuff below
                # This is used to reset the data to then move on to the next state. We already added the data for the
                # state to the resultdictionary so we are safe to set this stuff to blank
                countyhigh, countyhighcode, countyhighsum = 0, 0, 0
                countylow, countylowcode, countylowsum = 999, 999, 999
                count = 0
                statenever = []
                staterarely = []
                statesometimes = []
                statefrequently = []
                statealways = []
                stateneverfloat = 0
                stateneversum = 0
                statenevertotal = 0

                staterarelyfloat = 0
                staterarelysum = 0
                staterarelytotal = 0

                statesometimesfloat = 0
                statesometimessum = 0
                statesometimestotal = 0

                statefrequentlyfloat = 0
                statefrequentlysum = 0
                statefrequentlytotal = 0

                statealwaysfloat = 0
                statealwayssum = 0
                statealwaystotal = 0

                break  # breaks the current loop in order to move onto the next iteration of the loop, i.e. the next state

    maskuse.close()

    for x, y in statedict.items():
        if x in resultdict:
            resultdict[x].insert(0, y)  # adds the state name to the dictionary value for corresponding key

    print('{:20} {:21} {:22} {:21} {:22} {:22} {:21} {:30} {}'.format('State Name', 'State Code', 'Never', 'Rarely', 'Frequently', 'Sometimes', 'Always', ' County Best Mask %', 'County Worst Mask %'))
    print('-' * 210)
    for x, y in resultdict.items():
        print('{:20} {:5} {:20} % {:20} % {:20} % {:20} % {:20} % {:>20} {:10} % {:>18} {:10} %'.format(y[0], x, y[1], y[2], y[3], y[4], y[5], y[7], y[6], y[9], y[8]))
    usdata()


def option_2():  # function for specific state from user input
    global statename, statecode, countyhighcode, countylowcode, statenevertotal
    stateabbr = open('State_Abbreviations.csv', 'r')
    next(stateabbr)
    stateaccept = False
    statenamedict = {}

    for line in stateabbr:  # uses the state abbreviation file to get the 2 letter code for each state.
        # creates a dictionary with the 2 letter code as the key and the state name as the value
        line = line.replace('\n', '')
        line = line.split(',')
        statenamedict[line[1]] = line[0]

    while not stateaccept:  # continue the loop until stateaccept is set to True
        state = input('Please enter the two-letter code for the state (i.e. NY for New York): ').upper()
        for x, y in statenamedict.items():
            if state == x:  # checks to see if the user input is an acceptable state code
                statename = y  # sets the statename variable equal to the full length state name
                stateaccept = True

    stateabbr.close()

    stategeo = open('State-geocodes-v2018.csv', 'r')
    next(stategeo)

    for line in stategeo:
        line = line.split(',')
        if statename in line[6]:  # if the statename variable is in the stategeo column index 6
            statecode = line[1]  # set statecode variable equal to the state fips code
            statecode = statecode.zfill(2)  # adds leading zero to normalize the data

    stategeo.close()

    # pretty much same code as option_1 function
    maskuse = open('mask-use-by-county.csv', 'r')
    next(maskuse)
    statenever = []
    staterarely = []
    statesometimes = []
    statefrequently = []
    statealways = []
    count = 0
    resultdict = {}
    countyhigh = 0
    countylow = 99999

    for line in maskuse:
        columns = line.split(',')
        if len(columns[0]) == 4:
            columns[0] = columns[0].zfill(5)

        if ((columns[0])[0:2]) == statecode:
            statenever.append(columns[1])
            staterarely.append(columns[2])
            statesometimes.append(columns[3])
            statefrequently.append(columns[4])
            statealways.append(columns[5])
            count += 1

            countyhighsum = float(columns[4]) + float(columns[5])
            countyhighsum = round(countyhighsum * 100 / 2, 2)
            if float(countyhighsum) > float(countyhigh):
                countyhigh = countyhighsum
                countyhighcode = columns[0]

            countylowsum = float(columns[1]) + float(columns[2])
            countylowsum = round(countylowsum * 100 / 2, 2)
            if float(countylowsum) < float(countylow):
                countylow = countylowsum
                countylowcode = columns[0]

            stateneverfloat = list(map(float, statenever))
            stateneversum = sum(stateneverfloat)
            statenevertotal = round(stateneversum / count * 100, 2)

            staterarelyfloat = list(map(float, staterarely))
            staterarelysum = sum(staterarelyfloat)
            staterarelytotal = round(staterarelysum / count * 100, 2)

            statesometimesfloat = list(map(float, statesometimes))
            statesometimessum = sum(statesometimesfloat)
            statesometimestotal = round(statesometimessum / count * 100, 2)

            statefrequentlyfloat = list(map(float, statefrequently))
            statefrequentlysum = sum(statefrequentlyfloat)
            statefrequentlytotal = round(statefrequentlysum / count * 100, 2)

            statealwaysfloat = list(map(float, statealways))
            statealwayssum = sum(statealwaysfloat)
            statealwaystotal = round(statealwayssum / count * 100, 2)

            resultdict[statecode] = [statenevertotal, staterarelytotal, statesometimestotal, statefrequentlytotal,
                               statealwaystotal, countyhigh, countyhighcode, countylow, countylowcode]

    maskuse.close()

    for x, y in statenamedict.items():
        if y in statename:
            resultdict[statecode].insert(0, y)

    print('{:20} {:21} {:22} {:21} {:22} {:22} {:21} {:30} {}'.format('State Name', 'State Code', 'Never', 'Rarely', 'Frequently', 'Sometimes', 'Always', ' County Best Mask %', 'County Worst Mask %'))
    print('-' * 210)
    for x, y in resultdict.items():
        print('{:20} {:5} {:20} % {:20} % {:20} % {:20} % {:20} % {:>20} {:10} % {:>18} {:10} %'.format(y[0], x, y[1],
                                                                                                        y[2], y[3],
                                                                                                        y[4], y[5],
                                                                                                        y[7], y[6],
                                                                                                        y[9], y[8]))
    print('\n')


main()
