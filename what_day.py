from datetime import date, datetime
import calendar

if calendar.day_name[datetime.today().weekday()] == "Saturday":
    print ("Have fun")
elif calendar.day_name[datetime.today().weekday()] == "Sunday":
    print ("Recover")
else:
    print ("Work Work Work!!!!")
        