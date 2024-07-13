list_input = input("Enter the list with commas:- ")
palindrome_list = [palindrome.strip() for palindrome in list_input.split(",")]
length= len(palindrome_list)
main_length= int(length/2)
first_half = palindrome_list[0:main_length]
second_half = palindrome_list[-main_length:][::-1]

if(first_half == second_half):
    print("Palindrome")
else:
    print("Not palindrome")
'''
palindrome is a variable name used in the list comprehension. Let's break down the code:

1.list_input.split(","): This splits the string list_input into a list of substrings, using a comma (,) as the delimiter.

2.for palindrome in list_input.split(","): This part iterates over each substring produced by the split() method. For each substring, the variable palindrome takes its value.

3.palindrome.strip(): This applies the strip() method to the palindrome variable, which removes any leading or trailing whitespace from the substring.

4.[palindrome.strip() for palindrome in list_input.split(",")]: This list comprehension constructs a new list by applying strip() to each substring in the split input list.

So, palindrome is just a variable name used to refer to each element in the list produced by list_input.split(",") during the iteration within the list comprehension.
'''
list_input = input("Enter the list with commas:- ")
palindrome_list = [palindrome.strip() for palindrome in list_input.split(",")]
copied_palindrome_list= palindrome_list.copy()
copied_palindrome_list.reverse() 
if(copied_palindrome_list== palindrome_list) :
    print("Palindrome")
else:
    print("Not Palindrome")