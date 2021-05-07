# Zach Taylor - CINF308 Programming for Informatics
from TimeType import TimeType  # Imports the class TimeType from the TimeType file

daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # List to hold maximum days in a month


class Clock(TimeType):
    def __init__(self):  # Initializes the attributes of the class
        self.__hrs = int(0)
        self.__mins = int(0)
        self.__secs = int(0)
        self.__mon = int(1)
        self.__dy = int(1)
        self.__yr = int(1980)
        super().__init__()  # Access the constructor method of the base class (TimeType)

    def leapyear(self, year):  # Function to determine if year is leap year
        if year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False

    def setClock(self, hrs, mins, secs, mon, dy, yr):  # Set the time and date of the clock using the given values
        if Clock.leapyear(self, yr) is True:  # Checks to see if the year if a leap year
            daysInMonth[1] = 29  # If year is leap year, set the index of 1 (February) to 29

        if TimeType.set_hours(self, hrs) is False:
            return False

        elif TimeType.set_minutes(self, mins) is False:
            return False

        elif TimeType.set_seconds(self, secs) is False:
            return False

        elif mon < 0 or mon > 12:
            return False

        elif dy < 0 or dy > daysInMonth[mon - 1]:
            return False

        elif yr < 0:
            return False

        else:

            self.__hrs = hrs
            self.__mins = mins
            self.__secs = secs
            self.__mon = mon
            self.__dy = dy
            self.__yr = yr
            daysInMonth[1] = 28  # Resets February back to 28 days
            return True

    def increaseDay(self):  # Increases the day by 1
        if Clock.leapyear(self, self.__yr) is True:
            daysInMonth[1] = 29

        self.__dy = int(self.__dy) + 1
        if int(self.__dy) == (daysInMonth[self.__mon - 1] + 1):  # If day is greater than the month + 1
            self.__dy = int(1)  # Set day to 1
            self.__mon = self.__mon + 1  # Increase month by 1
            if self.__mon > 12:  # If month is greater than 12
                self.__mon = int(1)  # Set month to 1
                self.__yr = self.__yr + 1  # Increase year by 1
        daysInMonth[1] = 28


    def decreaseDay(self):  # Decrease the day by 1
        if Clock.leapyear(self, self.__yr) is True:
            daysInMonth[1] = 29

        self.__dy = int(self.__dy) - 1
        if int(self.__dy) == 0:  # If day is equal to 0
            self.__mon = self.__mon - 1  # Decrease month by 1
            self.__dy = daysInMonth[self.__mon - 1]  # Set day to max number of month
            if self.__mon == 0:  # If month is equal to 0
                self.__mon = 12  # Set month to 12
                self.__yr = int(self.__yr) - 1  # Decrease year by 1
        daysInMonth[1] = 28

    def increaseSecond(self):  # Increase the second
        if Clock.leapyear(self, self.__yr) is True:
            daysInMonth[1] = 29

        TimeType.increase_second(self)  # Calls the TimeType function 'increase_second'
        if TimeType.get_seconds(self) == 0 and TimeType.get_minutes(self) == 0 and TimeType.get_hours(self) == 0:
            self.increaseDay()  # If hours, minutes, seconds == 0, increase the day
        daysInMonth[1] = 28

    def decreaseSecond(self):  # Decrease the second
        if Clock.leapyear(self, self.__yr) is True:
            daysInMonth[1] = 29

        TimeType.decrease_second(self)  # Calls the TimeType function 'decrease_second'
        if TimeType.get_seconds(self) == 59 and TimeType.get_minutes(self) == 59 and TimeType.get_hours(self) == 23:
            self.decreaseDay()  # If the hours == 23, minutes == 59, and seconds == 59, decrease the day
        daysInMonth[1] = 28

    def __str__(self):
        return 'The date is {:02d}/{:02d}/{}. {}.'.format(self.__mon, self.__dy, self.__yr, super().__str__())
        #  Adds leading 0 to month and day. Calls base class __str__ function
