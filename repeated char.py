#Write a python program to Remove Repeated Character from String.
str=input("enter string :")
p=""
for char in str:
    if char not in p:
        p=p+char
print(p)        