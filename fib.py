def fibonacci(n):
   if n == 0 :
      return(0)
   elif n == 1:
      return(1)
   sum1 = fibonacci(n-1) + fibonacci(n-2)
   return(sum1)

print(fibonacci(7))

#without recurssion
num = int(input("Enter the number of series You want"))
a,b,count = 0,1,0
for var in range(num-1):
   sum2 = a + b
   a = b
   b = sum2
   count+=1
   if count == 1:
      print("0,1,1",end = ",")
   elif count == num-1:
      print(sum2,end = ".")
   else:
      print(sum2,end = ",")
