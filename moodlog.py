import datetime as dt
import csv

#get information on today in dd/mm/yy format
today = dt.date.today()
d1 = today.strftime("%d/%m/%y")

# collect information on workouts
med = input("Did you meditate today? ")
exer = input("Did you exercise today? ")
ther = input("Did you have therapy today? ")
cry = input("How many times did you cry today? ")
mood = input("How would you rate your mood today, 1-10? ")
notes = input("What contributed to your mood today? ")

if cry == 0:
    print("Yay, you didn't cry today!")

#write to exercise log
with open('Mood.csv', 'a', newline='') as file:
    fieldnames = ['Date', 'Meditation', 'Exercise', 'Therapy', 'Cry', 'Mood', 'Notes']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow({'Date': d1, 'Meditation': med, 'Exercise': exer, 'Therapy': ther, 'Cry': cry, 'Mood': mood, 'Notes': notes})