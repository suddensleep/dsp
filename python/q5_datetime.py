from datetime import datetime as dt

def getDuration(d1, d2):
    """Returns a string representation of the number of days 
    between MIDNIGHT on two dates.

    Arguments: d1, d2 are datetime objects.
    Returns: string object.
    """
    return str((d2 - d1).days)

def printDuration(start, stop, format):
    """Prints a message stating the number of days between 
    two dates in a given format.

    Arguments: start, stop, format are string objects.
    Returns: None.
    """
    print 'The number of days between', date_start, 'and', date_stop, 'is',
    print getDuration(dt.strptime(start, format), dt.strptime(stop, format))+'.'
    

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

printDuration(date_start, date_stop, '%m-%d-%Y')
# month-day-year

####b)  
date_start = '12312013'  
date_stop = '05282015'  

printDuration(date_start, date_stop, '%m%d%Y')
# monthdayyear

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

printDuration(date_start, date_stop, '%d-%b-%Y')
# day-month(str)-year
