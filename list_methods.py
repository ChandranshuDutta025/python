list = [2,1,3]
'''
These Function can't be printed cause they never return a value
'''
list.append(5)#adds one element at end(Mutation).If the list is mpty then we can add any new thing using it.
list.sort(reverse=True)#sorts in descending order
list.sort(reverse=False)#sorts ascending
print(list)
list.reverse()
print(list)
list.insert(1,4)#list.insert(index,element to add)
print(list)
list.remove(2)#remove the element
print(list)
list.pop(2)#it removes the element inindex
print(list)

