#Write a python program to check string is anagrams or not in Python
str1=input("enter the first string:") #ex:arc=car,cat=act,cider=cried
str2=input("enter the second string:")
#converting both strings into lowercase
str1=str1.lower()
str2=str2.lower()
#check if length is same
if(len(str1)==len(str2)):
    #sort strings
    sorted_str1=sorted(str1)
    sorted_str2=sorted(str2)
    #if sorted char arrays are same
    if(sorted_str1==sorted_str2):
        print(str1 +"and"+ str2 +"are anagram.")
    else:
        print(str1 + "and" + str2 + "are not anagram.")
else:
    print(str1 +"and" +str2 +"are not anagram.")            


    