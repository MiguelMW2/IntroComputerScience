# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#


#if (year is not divisible by 4) then (it is a common year)
##else if (year is not divisible by 100) then (it is a leap year)
#else if (year is not divisible by 400) then (it is a common year)
#else (it is a leap year)

def year_list(year1, year2):
    yearList = []
    for year in range(year1, year2 + 1):
        if not year % 4 == 0:
            yearList.append(365)
        elif not year % 100 == 0:
            yearList.append(366)
        elif not year % 400 == 0:
            yearList.append(365)
        else:
            yearList.append(366)
    return yearList

def days_pass(year1, month1, day1):
    daysOfMonths1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysOfMonths2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    i = 0
    if year1 == 365:
        while i < month1-1:
            days = days + daysOfMonths1[i]
            i = i + 1
    elif year1 == 366:
        while i < month1-1:
            days = days + daysOfMonths2[i]
            i = i + 1
    return days + day1

def countDays(yearList):
    count = 0
    for i in range(0, len(yearList) - 1):
        count = count + yearList[i]
    return count

def check_months(year1, month1, day1, year2, month2, day2):
    yearList = year_list(year1, year2)
    left_days = days_pass(yearList[0], month1, day1)
    right_days = days_pass(yearList[-1], month2, day2)
    total = countDays(yearList) - left_days + right_days
    return total

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    daysOfLife = check_months(year1, month1, day1, year2, month2, day2)
    return daysOfLife
    


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

test()
