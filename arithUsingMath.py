#read file make arithmatic operation using file content
f1=open("math.txt","r")
b=f1.read()
l1=str(b)
b=l1.split()

ad1=0
ad2=0
ad3=0
ad4=0

print("Elements of math file:",b)
for i in range(0, len(b)):
    b[i] = int(b[i])
    ad1=ad1+b[i]
print("addition of all ele: ",ad1)

for i in range(0, len(b)):
    b[i] = int(b[i])
    ad2=ad2-b[i]
print("substraction of all ele: ",ad2)

for i in range(0, len(b)):
    try:
        b[i] = int(b[i])
        ad3=ad3/b[i]
    except: 
        print("zeroerror")
        print("division of all ele: ",ad3)

for i in range(0, len(b)):
    b[i] = int(b[i])
    ad4=ad4*b[i]
print("multiplication of all ele: ",ad4)