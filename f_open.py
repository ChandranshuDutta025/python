

# Open a file in read mode
f = open("sample.txt", "r")

# Read the contents of the file
contents = f.read()

# Print the contents
print(contents)

# Read the first line of the file
line1 = f.readline()

# Print the contents of line
print(line1)
#it will give us nothing because we have already read the file

# Close the file
f.close()



# Open a file in write mode
f= open("sample.txt", "w")

# Write to the file
written = f.write("I will learn python,c++ and java by the end of 2024")

#print the contents of the file
print(written)

# Close the file
f.close()

# Open a file in append mode
f = open("sample.txt", "a")

# Append to the file
append = f.("I will get a job by the end of 2025")

# Print the contents of the file
print(append)

#close the file
f.close()


