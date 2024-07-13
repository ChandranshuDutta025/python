#In set we can enter only immutable values it is unordered it can give differnet value for differnt case 
#But sets are mutable
# set = {1,2,3.14,"abc"}
# print(set)
#Null set
collection = set()
collection.add(1)
collection.add(4)
collection.add("abc")
print(collection)
collection.remove(1)#If we put something that doesnot exist then it will give key error
print(collection.pop())#Random element will pop
collection.clear()#All clear

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))