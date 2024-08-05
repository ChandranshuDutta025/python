with open("practice.txt","w+") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in Java")
    f.seek(0)
    data = f.read()
    print(data)