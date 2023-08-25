#write a python program to check if given character is vowel or consonant
character=input("enter a character:")
vowels=['a','e','i','o','u','A','E','I','O','U']
if character in vowels:
    print("The character  is a vowel!")
else:
    print("The character  is a consonant!")
