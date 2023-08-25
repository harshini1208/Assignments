#Write a python program to count alphabets, digits, and special characters in the string.
string=input("enter a string:")
alphabets=0
digits=0
specialchars=0
for i in string:     #check for each character in the string
    if i.isalpha():
        alphabets+=1  #if character of string is alphabet
    elif i.isdigit():
        digits+=1    #if character of string is alphabet
    else:
        specialchars+=1  #if character of string is special character
print("alphabets=",alphabets,"digits=",digits,"specialchars=",specialchars)                 