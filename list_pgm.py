#list = [], ordered, mutable

l1=[1,2,3,4,5,6,7]
l1.append(1) #add specified element at the end
l1.extend([1,'hey']) #add multiple elelment at the last
l1[3]=2021 #replace the 3rd element with 2021
l1[3:6]=['a','b','c'] #replace ele index wise
del l1[2] #delete 2 index ele
a=l1.count(1) #return the no of time the specified element appears in the list 
print("count",a)
reverse=l1[::-1] #reverse the list
print('reverse of list:',reverse)
return_index=l1.index(2) #return the index no of given ele
print(return_index)
pop_by_index=l1.pop(3)
print(pop_by_index)
#l1.remove(1) #remove '1' from the list
#l1.clear() #remove all ele from the list
#del l1 #delete the complete list 

print(l1)

