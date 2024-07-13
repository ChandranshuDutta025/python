tuple = (1,4,9,16,25,36,49,64,81,100)
# for val in tuple:
#     print(val)

x = int(input("Enter your Number to search: "))
for index,value in enumerate(tuple):
     if value == x:
        print("it is at index ",{index})
        break
else :
        print("Number not found")