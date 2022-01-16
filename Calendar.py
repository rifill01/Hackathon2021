#This program is used for getting user inputs on Events to be placed in the To-do list

import datetime
from datetime import date
from time import strptime

#Optional, but might be useful
class myEvent():
    def __init__(self, eventName, addNotes, timeStart, timeEnd):
        self.eventName = eventName
        self.addNotes = addNotes
        self.timeStart = timeStart
        self.timeEnd = timeEnd


today = date.today()

dayEvent = today - datetime.timedelta(days=1)
dateToday = datetime.datetime (today.year, today.month, today.day)


eventName = input ("What is the name of this event?  : ")
print (eventName)

addNotes = input ("*Optional* Do you have any additional notes for this event?  :")
print (addNotes)

while True:
    try:
        dayEvent = datetime.datetime.strptime(input ("Input date in yyyy-mm-dd format: "), "%Y-%m-%d")
        if (dayEvent < dateToday):
            print ("Not a valid input. Please try again.")
        else:
            break
    except:
        print("The format of the date input is incorrect. Please try again.")

#Input for start time
while True:
    try:
        timeStart = datetime.datetime.strptime(input("Input start time in HH:MM format: "), "%H:%M")
        print (timeStart.strftime("%H:%M"))
        break
    except:
        print("The format of the time input is incorrect. Please try again.")

#Input for end time
while True:
    try:
        timeEnd = datetime.datetime.strptime(input("Input end time in HH:MM format: "), "%H:%M")
        print (timeEnd.strftime("%H:%M"))
        if(timeStart > timeEnd):
            print ("Time given should be later than the start time.")
        else:
            break
    except:
        print ("The format of the time input is incorrect. Please try again.")

