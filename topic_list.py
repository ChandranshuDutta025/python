#List are mutable(changable) in python but strings are immutable
random_things = ["Arjun" , 97.7, 98,"Blue"]
#print(random_things[4]) :--> It gives IndexError
random_things[0] = "Karna"
print(random_things)