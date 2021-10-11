#NAME
name=input("ENTER YOUR NAME: ")

#taking marks as input from user
print("ENTER THE MARKS OF SUBJECT: ")
maths=float(input("MATHS: "))
science=float(input("SCIENCE: "))
history=float(input("HISTORY: "))
geography=float(input("GEOGRAPHY: "))
marathi=float(input("MARATHI: "))

#calculating the CGPA of perticular subject 
maths=maths/10 
science=science/10
history=history/10
geography=geography/10
marathi=marathi/10

#printing the cgpa of subjects
print("CGPA OF ALL SUBJECT: ")
print("MATHS: ",maths)
print("SCIENCE: ",science)
print("HISTORY: ",history)
print("GEOGRAPHY: ",geography)
print("MARATHI: ",marathi)

#calculating cgpa of all subjects
adding_CGPA_of_all_subjects = maths+science+history+geography+marathi
print("ADDITION OF ALL SUBJECT'S CGPA: ",adding_CGPA_of_all_subjects)

#calculating 
stud_CGPA=adding_CGPA_of_all_subjects/5
print("CGPA OF STUDENT IS: ",stud_CGPA)

#calculating percentage from cgpa
spercentage = (stud_CGPA)*9.5
print(spercentage)

#returning the class\
if spercentage >= 1 and spercentage <= 35:
    print("Fail")
elif spercentage >= 36 and spercentage <= 65:
    print("second class")
elif spercentage >= 66 and spercentage <= 75:
    print("first class")
elif spercentage >= 76 and spercentage <= 100:
    print("distinction")
else: 
    print("Not able to calculate your percentge")     
     



