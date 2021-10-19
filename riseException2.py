try:
    a=int(input('a= '))
    b=int(input('b= '))
    if b == 0:
        raise ZeroDivisionError;
    else: 
        print('a/b: ',a/b)
except ZeroDivisionError :
    print('value of cannot be 0 ')
