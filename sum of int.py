#Write a python program to find sum of integers in the string.
s=input("Enter the string:")
sum=0
for i in s:
    if i.isdigit():
     sum=sum+int(i)
     print(sum)   
