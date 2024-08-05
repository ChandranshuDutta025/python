def check_line():
    line_number = 1
    word = "learning"
    with open("practice.txt", "r") as f:
        for line in f:
            if word in line.split():
                print(word)
                print(f"Line {line_number}: {line.strip()}")
            line_number += 1

check_line()

with open("practice.txt","r+") as f:
    data = f.read()
    num = data.split(",")
    print(num)

