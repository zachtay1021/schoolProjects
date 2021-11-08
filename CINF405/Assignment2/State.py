# Zach Taylor - CINF405 Advanced Concepts and Practices in Software Development
from Data import Data


class State:  # Creates SpecificState class
    state = ''
    dict = Data()  # Creates object from Data class
    dict.create_dictionary()  # Executes the create_dictionary function

    def __init__(self, stateabbr):  # Instantiates class
        self.__self = self
        self.__get_state(stateabbr)
        self.avg = self
        self.avg_list = self

    def __get_state(self, stateabbr):
        abbr_to_state = {
            "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "FL": "Florida", "GA": "Georgia",
            "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts",
            "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "NewHampshire", "NJ": "NewJersey",
            "NM": "NewMexico", "NY": "NewYork", "NC": "NorthCarolina", "ND": "NorthDakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "RI": "RhodeIsland",
            "SC": "SouthCarolina", "SD": "SouthDakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "WestVirginia",
            "WI": "Wisconsin", "WY": "Wyoming",
        }

        for x, y in abbr_to_state.items():  # Looks through state dictionary
            if stateabbr.upper() == x:  # If user input is a key in the dictionary then set statename variable equal to the value of the key (i.e. full state name)
                self.state = y  # Doing this because the csv data has the full state name as the key instead of an abbreviation

    def avg_tuition(self):
        dict = Data()  # Creates object from Data class
        dict.create_dictionary()  # Executes the create_dictionary function

        for x, y in Data.statedict.items():  # Iterates through the created dictionary
            if self.state in x:  # If user input is a key in the dictionary
                for num in y:  # Iterates through the values assigned to the key
                    num_sum = sum([int(i) for i in y if type(i) == int or i.isdigit()])  # Takes the string in the values list and converts them to digits + sums it together
                avg_sum = (num_sum / 12)  # Takes the sum of values and divides by 12 to find the average
                return avg_sum

    def avg_rise(self):

        i = 0
        new = 1  # Used to calculate average rise
        old = 0  # Used to calculate average rise
        self.avg_list = []

        for x, y in Data.statedict.items():  # Iterates through the created dictionary
            if self.state in x:  # If user input is a key in the dictionary
                while i <= len(y):  # Runs through loop 12 times
                    val1 = int(y[new])  # Sets val1 equal to the int of the value in the dictionary with the index equal to new
                    val2 = int(y[old])  # Sets val2 equal to the int of the value in the dictionary with the index equal to old

                    avg_num = (((val1 - val2) / val2) * 100)  # Calculates change between val1 and val2
                    self.avg_list.append(avg_num)  # Appends change to list

                    new += 1  # Adds 1 to new
                    old += 1  # Adds 1 to old
                    i += 1

                    if new == 12:  # Breaks while loop if variable new is greater than the total index number for the values
                        i = 13

                avg_all_years = (sum(self.avg_list) / len(self.avg_list))  # Finds the average of all rises in avg_list
                self.avg = avg_all_years
                self.avg = round(avg_all_years, 2)  # Rounds average to only 2 decimal places
                return self.avg

    def pred_one_year(self):
        self.avg_rise()  # Executes the avg_rise method

        for x, y in Data.statedict.items():  # Iterates through the created dictionary
            if self.state in x:  # If user input is a key in the dictionary
                last_year_rise = self.avg_list[-1]  # Sets last_year_rise equal to the last entry in the avg_list from the avg_rise method
                last_year_cost = int(y[-1])  # Sets last_year_cost equal to the last entry in the values from the specified state / key

                pred_cost_last = (((last_year_rise / 100) * last_year_cost) + last_year_cost)  # Calculates the predicted year based on previous year rise
                pred_cost_last = str(round(pred_cost_last, 2))  # Rounds predicted cost to 2 decimal places

                avg_cost_all = self.avg  # Sets avg_cost_all equal to the average rise from all years
                pred_cost_all = (((avg_cost_all / 100) * last_year_cost) + last_year_cost)  # Calculates the predicted year based on average from all years
                pred_cost_all = str(round(pred_cost_all, 2))
                return pred_cost_last, pred_cost_all

    def pred_two_year(self):
        self.avg_rise()
        for x, y in Data.statedict.items():
            if self.state in x:
                last_year_rise = self.avg_list[-1]  # Sets rise equal to the rise between 14-15 and 15-16
                last_year_rise = str(round(last_year_rise, 2))

                avg_two_year = ((self.avg_list[-1] + self.avg_list[-2]) / 2)  # Sets rise equal to average rise between 13-14 and 14-15 and the rise between 14-15 and 15-16
                avg_two_year = str(round(avg_two_year, 2))

                avg_rise_two = self.avg  # Sets the rise equal to the average of all rises

                return last_year_rise, avg_two_year, avg_rise_two
