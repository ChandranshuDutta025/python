
def length(list2):
    i = 0
    for val in list1:
        i += 1
    print("The length of list is ",i)

list1 = [1,2,3,4,5]
length(list1)

#Printing items of list i single line
list2 = [1,2,3,4,5]
def print_list(a):
    result = ""
    for val in a:
        result += str(val) + ","
    print(result)

print_list(list2)
#factorial
n = int(input("Enter the number: "))
def factorial(n):
    result = 1
    for val in range(1,n+1):
        result *= val
    print(result)

factorial(n)
#usd to inr
usd = float(input("USD : "))
def converter(a):
    inr = 83.49*usd
    print("INR : ",inr)

converter(usd)