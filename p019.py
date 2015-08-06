

# https://projecteuler.net/problem=19
#You are given the following information, but you may prefer to do some 
#  research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century 
#   unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century
#   (1 Jan 1901 to 31 Dec 2000)?
# 
# Analysis: 
# All years in, and including, 1901 and 2000 are leap if divided by 4. 
# 1900 was not a leap year.. so 365 days
#  365 % 7 = 1 ; so last day of the year will be Monday again.
#  1 Jan 1901 must be Tue
# 
# Let's designate Sun=0, Mon=1 and so on
#  so we start 1 Jan 1901 as currentDay=2 (Tuesday)
#  Feb1  currentDay= (2+28)%7=2  
#   so of for each month. if we get 0, we got a sunday on 1st




currentDay = 2   
SundayCount = 0   # count number of Sundays on 1st of month

for year  in range(1901,2001) : 
        print "year = ", year , 
        if year % 4 == 0 : 
                monthDays = [31,29,31,30,31,30,31,31,30,31,30,31]
        else : 
                monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
        for days in monthDays : 
                if currentDay == 0 : 
                        SundayCount += 1
                currentDay = (currentDay + days) % 7
        print ""

print "Sunday on 1st of month = " , SundayCount



