# def show(n):
#     if n == 0:
#         return
#     print(n)
#     show(n-1)

# n=5
# show(n)

def fact(n):
    if (n==1 or n==0):
        return 1
    else :
        return n *fact(n-1)
    
x=fact(5)
print(x)