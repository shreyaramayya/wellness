import datetime as dt
import csv

#get information on today in dd/mm/yy format
today = dt.date.today()
d1 = today.strftime("%d/%m/%y")

# collect information on the work day
rot = input("What rotation are you on? ")
start = input("When did you start work? ")
end = input("When did you leave work? ")
notes = input("What happened today at work? ")

# calculate hours worked
start_dt = dt.datetime.strptime(start, '%d/%m/%y %H:%M')
end_dt = dt.datetime.strptime(end, '%d/%m/%y %H:%M')
diff = (end_dt - start_dt)
hours = diff.total_seconds()/3600

#print summary
print ("Today's Summary", d1, rot, hours, notes)

#write to hour log
with open('WorkHours.csv', 'a', newline='') as file:
    fieldnames = ['Date', 'Rotation', 'Hours', 'Notes']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow({'Date': d1, 'Rotation': rot, 'Hours': hours, 'Notes': notes})

