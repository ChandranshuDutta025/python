#list problem
dict = {
    "table" : ["a piece of furniture","list of facts & figures"],
    "cat":"a small animal"
}
print(dict)
#set problem
set1 = {"python","java","c++","javascript","java","python","java","c++","c"}
print(len(set1))
#blank dictionary filling UI
dict = {}

x = int(input("Enter the physics number: "))
y = int(input("Enter the chemistry number: "))
z = int(input("Enter the Math number: "))
dict.update({"phy" : x})
dict.update({"Chem" : y})
dict.update({"Math" : z})
print(dict)
#saving same value in one set
set2 ={
    ("float" ,9.0),
    ("int" ,9)
}
print(set2)