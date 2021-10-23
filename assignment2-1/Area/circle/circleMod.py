import math
def cir_area():
    try:
        r=int(input("Enter the radious "))
        a=(math.pi)*r*r 
        print(a)
      
    except:
        print("An error occured")
cir_area()