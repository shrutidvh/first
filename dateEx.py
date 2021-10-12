#returning year from the date using list
from datetime import date

current_date=str(date.today())
b=list(current_date[0:4])
c=''.join([str( ele) for ele in b])
print('2021: ',str(c))