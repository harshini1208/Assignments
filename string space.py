#Write a python program to replace string space with given character in Python.
#ex 2
string = input("enter string:")
space = "" #empty string
replace_with = input("enter char:")
for i in string:
    if i == " ": #if any space found in the string
        i = replace_with #replacing space with character
    space += i #concatenating each character with the string without space
print(space)