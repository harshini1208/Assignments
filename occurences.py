#Write a python program to count occurrence of given character in string. 
print("enter the string:") 
text=input()
print("enter the character:")
char=input()
textLen=len(text)
sum=0
for i in range(textLen):
    if char==text[i]:
        sum=sum+1
print("\n Occurences of given character is:")
print(sum)        