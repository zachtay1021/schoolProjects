# Zach Taylor - CINF308 Programming for Informatics


class TimeType:  # Creates TimeType class
    def __init__(self):
        self.__hours = int(0)  # Sets starting hour to 0
        self.__minutes = int(0)  # Sets starting minute to 0
        self.__seconds = int(0)  # Sets starting second to 0

    def get_hours(self):
        return self.__hours  # Returns the given hour

    def get_minutes(self):
        return self.__minutes  # Returns the given minute

    def get_seconds(self):
        return self.__seconds  # Returns the given second

    def set_hours(self, hours):  # Changes the hour if hour is greater than 0 or less than 24
        if hours < 0 or hours > 23:
            return False
        else:
            self.__hours = hours
            return True

    def set_minutes(self, minutes):  # Changes the minute if minute is greater than 0 or less than 60
        if minutes < 0 or minutes > 59:
            return False
        else:
            self.__minutes = minutes
            return True

    def set_seconds(self, seconds):  # Changes the second if second is greater than 0 or less than 60
        if seconds < 0 or seconds > 59:
            return False
        else:
            self.__seconds = seconds
            return True

    def set_time(self, hours, minutes, seconds):  # Requires three attributes when creating. Does same checks as above
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        if hours < 0 or hours > 23:
            return False

        elif minutes < 0 or minutes > 59:
            return False

        elif seconds < 0 or seconds > 59:
            return False

        else:
            self.__hours = hours
            self.__minutes = minutes
            self.__seconds = seconds
            return True

    def increase_second(self):  # Increases the second by 1. If second = 60, increase minute by 1, etc.
        self.__seconds = int(self.__seconds) + 1
        if int(self.__seconds) == 60:
            self.__seconds = 0
            self.__minutes = int(self.__minutes) + 1

        if int(self.__minutes) == 60:
            self.__minutes = 0
            self.__hours = int(self.__hours) + 1

        if int(self.__hours) == 24:
            self.__hours = 0

    def decrease_second(self):  # Decreases the second by 1. If second = 0, decrease minute by 1, etc.
        self.__seconds = int(self.__seconds) - 1
        if int(self.__seconds) < 0:
            self.__seconds = 59
            self.__minutes = int(self.__minutes) - 1

        if int(self.__minutes) < 0:
            self.__minutes = 59
            self.__hours = int(self.__hours) - 1

        if int(self.__hours) < 0:
            self.__hours = 23

    def __str__(self):  # Returns statement depending on hour value. prints in standard time format.
        if int(self.__hours) == 0:
            self.__minutes = str(self.__minutes).zfill(2)
            self.__seconds = str(self.__seconds).zfill(2)
            return 'The time is 12:{}:{} AM'.format(self.__minutes, self.__seconds)

        elif int(self.__hours) < 11:
            self.__hours = str(self.__hours).zfill(2)
            self.__minutes = str(self.__minutes).zfill(2)
            self.__seconds = str(self.__seconds).zfill(2)
            return 'The time is {}:{}:{} AM'.format(self.__hours, self.__minutes, self.__seconds)

        elif int(self.__hours) == 12:
            self.__hours = str(self.__hours).zfill(2)
            self.__minutes = str(self.__minutes).zfill(2)
            self.__seconds = str(self.__seconds).zfill(2)
            return 'The time is {}:{}:{} PM'.format(self.__hours, self.__minutes, self.__seconds)

        else:
            displayHours = int(self.__hours) - 12
            self.__hours = str(self.__hours).zfill(2)
            self.__minutes = str(self.__minutes).zfill(2)
            self.__seconds = str(self.__seconds).zfill(2)
            return 'The time is ' + str(displayHours) + ':{}:{} PM'.format(self.__minutes, self.__seconds)
