import time
import calendar

print 'Number of ticks since 12:00 am, January 1,1970(epoch) =', time.time()

print '''
#------------------Time Tuple---------------------------#
    Field           Values
    Hour            0 to 23
    Minute          0 to 59
    Second          0 to 61 (60 or 61 are leap-seconds)
    Day of Week     0 to 6 (0 is Monday)
    Day of Year     1 to 366 (Julien Day)
#-------------------------------------------------------#
'''
print 'Local Current Time =', time.localtime(time.time())  # time.struct_time(tm_year=2017, tm_mon=12, tm_mday=26, tm_hour=16, tm_min=18, tm_sec=26, tm_wday=1, tm_yday=360, tm_isdst=0)
# tm_yday = 1 to 366 (Julien Day)

print '''
#--------------struct_time Structure--------------------#
tm_year	    2008
tm_mon	    1 to 12
tm_mday	    1 to 31
tm_hour	    0 to 23
tm_min	    0 to 59
tm_sec	    0 to 61 (60 or 61 are leap-seconds)
tm_wday	    0 to 6 (0 is Monday)
tm_yday	    1 to 366 (Julian day)
tm_isdst    -1, 0, 1, -1 means library determines DST
#--------------------------------------------------------#
'''
print 'Getting Formatted Time =', time.asctime(time.localtime(time.time()))  # Tue Dec 26 16:18:26 2017


print calendar.month(2018, 1)
