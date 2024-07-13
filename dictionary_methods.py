student = {
    "Name" : "Chandu",
    "score" : {
        "Math" : 97,
        "Chem" : 97,
        "Phy" : 97
    }
}
print(student.keys)#It says the position where the keys are at
print(student.keys())#All the keys in dictionary
print(len(student))#LEntgh of the dictionary
print(student.items())#Result:-dict_items([('Name', 'Chandu'), ('score', {'Math': 97, 'Chem': 97, 'Phy': 97})])
print(student.get("Name"))#It is used because if somehohow i write name 2 the it will return None and the rest of the code will run 
print(student["Name"])# otherwise it will give error and in this case nothing willl run after it
student.update({"City":"Delhi"})#If I write  student = student.update({"City":"Delhi"}) then it will return none
student.update({"Name":"Chandrasnhu Dutta"})#It can also upodate esxisting key

print(student)