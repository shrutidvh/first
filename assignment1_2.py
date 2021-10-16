# Assignment: 1 | 16 Oct 2021
# Q2:   Assign Date to x variable in DD-MM-YYYY format extract and print Year from Date
from datetime import date as d
current_date = d.today()
s1 = current_date.strftime ('%d-%m-%Y')
print('DD-MM-YYYY:',s1)
print('YYYY: ',s1[6:])