#write a program to check given string is palindrome or not
string=input(("enter a string:"))# ex-madam
if(string==string[::-1]):
    print("The string is palindrome")
else:
    print("Not a palindrome")    