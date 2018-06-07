#1
'''
Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −

Index	Field	Values
0	4-digit year	2008
1	Month	1 to 12
2	Day	1 to 31
3	Hour	0 to 23
4	Minute	0 to 59
5	Second	0 to 61 (60 or 61 are leap-seconds)
6	Day of Week	0 to 6 (0 is Monday)
7	Day of year	1 to 366 (Julian day)
8	Daylight savings	-1, 0, 1, -1 means library determines DST
The above tuple is equivalent to struct_time structure. This structure has following attributes −

Index	Attributes	Values
0	tm_year	2008
1	tm_mon	1 to 12
2	tm_mday	1 to 31
3	tm_hour	0 to 23
4	tm_min	0 to 59
5	tm_sec	0 to 61 (60 or 61 are leap-seconds)
6	tm_wday	0 to 6 (0 is Monday)
7	tm_yday	1 to 366 (Julian day)
8   tm_isdst	-1, 0, 1, -1 means library determines DST
'''

#2
import time
ti=time.gmtime()
print("Formated time :",ti)
print(time.asctime(ti))

#3
import datetime
print(datetime.date.today().strftime("%B"))

#4
from datetime import date
d=date.today()
print("day :",d.day)

#5
from datetime import date
d=date.today()
print("day :",d.day)

#6
print("local time:",time.ctime())

#7
import math
n=int(input("enter a number"))
print("factorial :",math.factorial(n))

#8
n1=int(input("Enter a number"))
n2=int(input("Enter another number"))
print(math.gcd(n1,n2))

#9
import os
print(os.getcwd())

print(os.environ) 
