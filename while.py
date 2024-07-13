# count = 1
# while count <=100 :
#     print(count)
#     count += 1

# reverse_count = 100
# while reverse_count >=1 :
#     print(reverse_count)
#     reverse_count -=1

# n = int(input("Enter your number : "))
# count1 = 1
# while count1 <=10 :
#     print(n * count1)
#     count1 += 1
    
tuple = (1,4,9,16,25,36,49,64,81,100)
# num1 = int(input("Enter the number: "))
num2 = 36
idx = 0
while idx < len(tuple):
    if tuple[idx] == num2 :
        print("It is present at index ",tuple.index(num2))
        break
    idx +=1
else :
    print("Finding...")
    
      