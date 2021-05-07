# Zach Taylor - CINF308 Programming for Informatics

import tkinter as tk
import Clock

clock = Clock.Clock()  # Instantiates a clock object
screen = tk.Tk()  # Instantiates a tkinter object
screen.title("Clock")  # Window title is 'Clock'
screen.geometry("850x550")  # Window size is 850x550
screen.configure(bg="steelblue1")  # Sets window background color


def increaseDay():  # Defines the increaseDay command
    clock.increaseDay()  # Calls the increaseDay function from the Clock class
    label2.place(relx=.34, rely=.15)  # Resets the time label because setClock changes it if error
    label2.config(text=clock.__str__())  # Displays clock.__str__ in label 2

def decreaseDay():
    clock.decreaseDay()  # Calls the decreaseDay function from the Clock class
    label2.place(relx=.34, rely=.15)
    label2.config(text=clock.__str__())

def increaseSecond():
    clock.increaseSecond()  # Calls the increaseSecond function from the Clock class
    label2.place(relx=.34, rely=.15)
    label2.config(text=clock.__str__())

def decreaseSecond():
    clock.decreaseSecond()  # Calls the decreaseSecond function from the Clock class
    label2.place(relx=.34, rely=.15)
    label2.config(text=clock.__str__())


def setClock():
    hrs = int(hourBox.curselection()[0])  # Grabs the currently selected item from the hourBox.
    mins = int(minuteBox.curselection()[0])  # Because curselection returns as a tuple, index needs to be used [0].
    secs = int(secondBox.curselection()[0])  # Ex. if selection is 5 it would return (5,), so index[0] returns 5.
    mon = int(monthBox.curselection()[0] + 1)  # Month cannot be 0, so add 1 to index to get user selection
    dy = int(dayBox.curselection()[0] + 1)  # Day cannot be 0, so add 1 to index to get user selection
    yr = int((yearBox.curselection()[0]) + 1900)  # Year cannot be 0, so add 1900 to index to get user selection
    if clock.setClock(hrs, mins, secs, mon, dy, yr) is True:  # If all selections are accepted, setClock returns True
        label2.place(relx=.34, rely=.15)
        label2.config(text=clock.__str__())
    else:
        label2.config(text="Invalid Date and/or Time!")  # If selection does NOT work, change label2 to error
        label2.place(relx=.408, rely=.15)  # Centers error message


month = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
         "October", "November", "December"]

day = list(range(1, 32))  # Creates list from 1 to 31

year = list(range(1900, 2101))  # Creates list from 1900 to 2100

hour = list(range(0, 24))  # Creates list from 0 to 23

minute = list(range(0, 60))  # Creates list from 0 to 59

second = list(range(0, 60))  # Creates list from 0 to 59

frame1 = tk.Frame(screen, bg="lavender", height=90, width=700)  # Top frame
frame1.place(relx=.1, rely=.06)

frame2 = tk.Frame(screen, bg="lavender", height=222, width=700)  # Middle frame
frame2.place(relx=.1, rely=.26)

frame3 = tk.Frame(screen, bg="lavender", height=100, width=700)  # Bottom frame
frame3.place(relx=.1, rely=.70)

label1 = tk.Label(screen, bg="lavender", text="Current Time")  # First label
label1.place(relx=.45, rely=.1)

label2 = tk.Label(screen, bg="lavender", text=clock.__str__())  # Second label
label2.place(relx=.34, rely=.15)

setTimeButton = tk.Button(screen, bg="mediumturquoise", text="Set Clock", width=13, command=setClock)
setTimeButton.place(relx=.15, rely=.73)  # Calls setClock

increaseDayButton = tk.Button(screen, bg="mediumturquoise", text="Increase Day", width=13, command=increaseDay)
increaseDayButton.place(relx=.3, rely=.73)  # Calls increaseDay

decreaseDayButton = tk.Button(screen, bg="mediumturquoise", text="Decrease Day", width=13, command=decreaseDay)
decreaseDayButton.place(relx=.45, rely=.73)  # Calls decrease Day

increaseSecondButton = tk.Button(screen, bg="mediumturquoise", text="Increase Second", width=13, command=increaseSecond)
increaseSecondButton.place(relx=.60, rely=.73)  # Calls increaseSecond

decreaseSecondButton = tk.Button(screen, bg="mediumturquoise", text="Decrease Second", width=13, command=decreaseSecond)
decreaseSecondButton.place(relx=.75, rely=.73)  # Calls decreaseSecond

quitButton = tk.Button(screen, bg="mediumturquoise", text="Quit", width=13, command=screen.destroy)
quitButton.place(relx=.45, rely=.8)  # Closes the window. Terminates program.

monthScrollBar = tk.Scrollbar(screen, orient="vertical")  # Scrolls bars next to each listbox
dayScrollBar = tk.Scrollbar(screen, orient="vertical")
yearScrollBar = tk.Scrollbar(screen, orient="vertical")
hourScrollBar = tk.Scrollbar(screen, orient="vertical")
minuteScrollBar = tk.Scrollbar(screen, orient="vertical")
secondScrollBar = tk.Scrollbar(screen, orient="vertical")

#  Listbox for each selection
monthBox = tk.Listbox(screen, width=10, exportselection=0, selectmode="single", yscrollcommand=monthScrollBar.set)
dayBox = tk.Listbox(screen, width=10, exportselection=0, selectmode="single", yscrollcommand=dayScrollBar.set)
yearBox = tk.Listbox(screen, width=10, exportselection=0, selectmode="single", yscrollcommand=yearScrollBar.set)
hourBox = tk.Listbox(screen, width=10, exportselection=0, selectmode="single", yscrollcommand=hourScrollBar.set)
minuteBox = tk.Listbox(screen, width=10, exportselection=0, selectmode="single", yscrollcommand=minuteScrollBar.set)
secondBox = tk.Listbox(screen, width=10, exportselection=0, selectmode="single", yscrollcommand=secondScrollBar.set)

# Month listbox
monthLabel = tk.Label(screen, bg="dodgerblue3", text="Month", width=10, fg="white")
monthLabel.place(relx=.1425, rely=.285)
for x in range(len(month)):
    monthBox.insert("end", month[x])
monthBox.select_set(0)
monthScrollBar.config(command=monthBox.yview)
monthBox.place(relx=.15, rely=.33)
monthScrollBar.place(relx=.225, rely=.4)

# Day listbox
dayLabel = tk.Label(screen, bg="dodgerblue3", text="Day", width=10, fg="white")
dayLabel.place(relx=.2725, rely=.285)
for x in range(len(day)):
    dayBox.insert("end", day[x])
dayBox.select_set(0)
dayScrollBar.config(command=dayBox.yview)
dayBox.place(relx=.28, rely=.33)
dayScrollBar.place(relx=.355, rely=.4)

# Year listbox
yearLabel = tk.Label(screen, bg="dodgerblue3", text="Year", width=10, fg="white")
yearLabel.place(relx=.4025, rely=.285)
for x in range(len(year)):
    yearBox.insert("end", year[x])
yearBox.select_set(0)
yearScrollBar.config(command=yearBox.yview)
yearBox.place(relx=.41, rely=.33)
yearScrollBar.place(relx=.485, rely=.4)

# Hour listbox
hourLabel = tk.Label(screen, bg="dodgerblue3", text="Hour", width=10, fg="white")
hourLabel.place(relx=.5325, rely=.285)
for x in range(len(hour)):
    hourBox.insert("end", hour[x])
hourBox.select_set(0)
hourScrollBar.config(command=hourBox.yview)
hourBox.place(relx=.54, rely=.33)
hourScrollBar.place(relx=.615, rely=.4)

# Minute listbox
minuteLabel = tk.Label(screen, bg="dodgerblue3", text="Minute", width=10, fg="white")
minuteLabel.place(relx=.6625, rely=.285)
for x in range(len(minute)):
    minuteBox.insert("end", minute[x])
minuteBox.select_set(0)
minuteScrollBar.config(command=minuteBox.yview)
minuteBox.place(relx=.67, rely=.33)
minuteScrollBar.place(relx=.745, rely=.4)

# Second listbox
secondLabel = tk.Label(screen, bg="dodgerblue3", text="Second", width=10, fg="white")
secondLabel.place(relx=.7925, rely=.285)
for x in range(len(second)):
    secondBox.insert("end", second[x])
secondBox.select_set(0)
secondScrollBar.config(command=secondBox.yview)
secondBox.place(relx=.8, rely=.33)
secondScrollBar.place(relx=.875, rely=.4)


screen.mainloop()
