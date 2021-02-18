##
# Determine all the magic days in the 1900s
#
import calendar

def days_in_month(year, month):
    if (month < 1) or (month > 12):
        print ("please enter a valid month")
    elif (year < 1) or (year > 9999):
        print ("please enter a valid year between 1 - 9999")
    else:
        return calendar.monthrange(year, month)[1]

# Determine whether or not a date is magic
# @param day the day portion of the date
# @param month the month portion of the date
# @param year the year portion of the date
# @return True if the date is magic, False otherwise
def isMagicDate(day, month, year):
    if day * month == year % 100:
        return True
    return False

# Find and display all of the magice dates in the 1900s
def main():
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, calendar.monthrange(month, year) + 1):
                if isMagicDate(day, month, year):
                    print("%02d/%02d/%04d is a magic date." % (day, month, year))

# Call the main function
main()
