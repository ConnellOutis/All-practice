import os 

os.system('cls') 

list1 = [1,2,3,4,5] 
list2 = [2,5,4,7,8] 

set1 = set(list1) 
set2 = set(list2) 

inter = set1.difference(set2)

print(set1) 

print(set2) 

print(inter)