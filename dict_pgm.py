#dictionary = {} , unorderd, mutable 

d={'1':'a','2':'b','3':'c','4':'d','5':'e'}
print("dict first item")
d['s']='apple' #add key value
print('item:',d.items()) #return all items from the dict
print('key:',d.keys()) #return all keys
d.pop('3') #delete ele with specified key
d.popitem() #delete last kay-pair value
d.clear() #remove all ele from dict

print('last print: ',d)
