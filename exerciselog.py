import datetime as dt
import csv

#get information on today in dd/mm/yy format
today = dt.date.today()
d1 = today.strftime("%d/%m/%y")

# collect information on workouts
type = input("What type of exercise did you do? ")
time = input("How long did you work out? ")
cals = input("How many calories did you burn? ")
dist = input("What distance did you cover today? ")
notes = input("How was your workout? ")

#write to exercise log
with open('Exercise.csv', 'a', newline='') as file:
    fieldnames = ['Date', 'Type', 'Time_In_Mins', 'Cals', 'Distance', 'Notes']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow({'Date': d1, 'Type': type, 'Time_In_Mins': time, 'Cals': cals, 'Distance': dist, 'Notes': notes})
