with open("practice.txt","r+") as f1:
    programm=f1.read()
    new_data= programm.replace("Java","python")
    f1.seek(0)
    f1.write(new_data)
    f1.truncate()
    f1.seek(0)
    update_data = f1.read()
    print(update_data)
    search=update_data.find("learning")
    search= True
    if search != True:
        print("Not find")
    else :
        print("Find")