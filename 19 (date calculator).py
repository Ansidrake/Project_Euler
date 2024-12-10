Days_Weeks = ['MON','TUE','WED','THUR','FRI','SAT','SUN']
Days_Month = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec']
Current_month = 'Jan'
Current_Day = 'Mon'
Current_Date = 1
Current_year = 1901

import sys
sys.setrecursionlimit(50000)
print(sys.getrecursionlimit())

def month_days(month,year):
    if month in ['Sept','Apr','June','Nov']:
        return 30
    elif month == 'Feb':
        return leap_year(year)
    else:
        return 31

def leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            #print('leap year')
            return 29
        else:
            return 28
    elif year % 4 == 0:
        #print('leap year')
        return 29

    else:
        return 28

def day_adder(Day):
    index = Days_Weeks.index(Day)
    if index == 6:
        return Days_Weeks[0]
    else:
        return Days_Weeks[index+1]
    
def month_adder(month):
    index = Days_Month.index(month)
    if index == 11:
        return Days_Month[0]
    else:
        return Days_Month[index+1]

def date_add(Current_Date,Current_Day,Current_month,Current_year):
    limit = month_days(Current_month,Current_year)
    
    if Current_Date + 1 > limit:
        month = month_adder(Current_month)
        date = 1 
        if month == 'Jan':
            year = Current_year + 1
        else:
            year = Current_year
    else:
        date = Current_Date + 1
        month = Current_month
        year = Current_year
    
    day = day_adder(Current_Day)
    return [date,day,month,year]

def calculate(date,day,month,year,count = 0 ):
    new_date = date_add(date,day,month,year)
    #if new_date[2] == 'Jan' and new_date[0] == 1:
    #    print([new_date[1],count])
    if date_add(date,day,month,year)[3] == 2001:
        return count
    else:
        if new_date[1] == 'SUN' and new_date[0] == 1:
            return calculate(new_date[0],new_date[1],new_date[2],new_date[3],count + 1)
        else:
            return calculate(new_date[0],new_date[1],new_date[2],new_date[3],count)

print(calculate(31,'MON','Dec',1900))