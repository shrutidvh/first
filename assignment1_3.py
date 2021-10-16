
#Assignment: 1 | 16 Oct 2021
#Q3: In a small company, the average salary of three employees is Rs1000 per week. If one employee earns Rs1100 and other earns Rs500, how much will the third employee earn? Solve by using Python programm

emp1_sal = 1100
emp2_sal = 500
emp3_sal = 0
avg_sal = 1000

sal_of_all_emp = emp1_sal+emp2_sal+emp3_sal
emp3_sal=(avg_sal*3)-sal_of_all_emp
print("salary of 3rd employee: ",emp3_sal)
