a,b=6,5
if a<b:
   print("b is greater than a")
else:                                                                                                                                
    print("a is greater than b")

#example 2
a,b=9,10
if a<b:
   print("a is less than b")
elif a==b:
   print("a is equal to b")
else:
   print("a is greater than b") 


   #startswith and endswith
s="python is very easy"
print(s.startswith('py'))
print(s.endswith("easy"))
print(s.endswith('y'))

#find prog example 1
s="python is very easy"
print(s.find("is"))
print(s.find(" "))
print(s.find("xy"))

#example 2
s="geeks for geeks"
print(s.find('for'))

#example 3
p="I am learning python and it is a great language"
print(p.find('I'))
print(p.find('q'))

#index and rindex prog example 1
s="python is very easy and is oop"
print(s.index("is"))
print(s.rindex("is"))#highest index of substring

#example 2
s="my name is harshini and sister name is nikki"
print(s.index("name"))
print(s.rindex("name"))

#example 3
s="geeks for geeks"
result=s.rindex('geeks')
print("substring 'geeks:",result)

#example 1
print(":".join("PYTHON"))

#example 2
tuple=("harshini","nikki","uday")
x="#".join(tuple)
print(x)

#example 3
list=['h','a','r','s','h','i','n','i']
print("".join(list))

#program using logical operators
a=10
b=-10
c=0
if a>0 and b>0:
    print("either of number is greater")
else:
    print("No number is greater than 0")
if b>0 or c<0:
    print("either of the number is greater")
else:
    print("no number is greater than 0") 

    #memebership operator
#example 1
lst=[2,3,4,5,6,7,8]
print(2 in lst)
print(100 in lst)
print(100 not in lst)

#example 2
print('n' in 'python')
print('b' in 'python')
print('s' not in 'python')

#example 3
num=45
s1=list(range(1,30))
print(num not in s1)
print(num in s1)

#example 4
a='apple'
list_1=['mango','apple','banana']
print(a in list_1)

num=6
for i in range(1,11):
    print(num,'x',i,'=',num*i)

#program using relational operators
a,b=10,20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# example 1:
s="my name is harshini"
print(s)
s1=s.replace('harshini','nikki')
print(s1)

#example 2:
food='biryani,pizza'
replaced_food=food.replace('i','e')
print(replaced_food)

#example 3:
string="good morning"
new_string=string.replace("good","great")
print(new_string)

#example 4:
s="i am good"
print(s)
s1=s.replace("good","bad")
print(s1)

#example 1
lst=[1,2,3,4,5,6,7,8]
print(lst[-6:-1:2])

#example 2
tpl=(1,2,3,4,5,6,7)
print(tpl[-4:-1:2])

#example 3
alpha=("a","b","c","d","e","f")
x=slice(3,5)
print(alpha[x])

#example 1
lst=[1,2,3,4,5,6,7,8]
print(lst[-6:-1:2])

#example 2
tpl=(1,2,3,4,5,6,7)
print(tpl[-4:-1:2])

#example 3
alpha=("a","b","c","d","e","f")
x=slice(3,5)
print(alpha[x])

#comparing two strings
print("geek"=="GEEK")
print("Geek"<"geek")
print("Geek"!="Geek")

#example 2
str1="hello"
str2='Hello'
str3='Hellos'
print("str1=str2",str1 is str2)
print("str1=str3",str1 is str3)
print("ID of str1=",id(str1))
print("ID of str3=",id(str3))
str1+="s"
print("str1=str3",str1 is str3)

#example 3:
str1="Hello"
str2="World"
print(str1>str2)
print(str1>str2)
print(str1>=str2)
print(str1<=str2)


#strip program example 1
s="harshini"
s="aharshinia"
print(s.strip('a'))
s="uday"
print(s.lstrip("ud"))
s="preeti"
print(s.rstrip("ti"))

#example 2
s="hello world!"
new_string=s.strip()
print(new_string)
s="Welcome"
print(s.lstrip("We"))
s="Home"
print(s.rstrip("me"))

#example 3
s="hyderabad is famous for biryani"
s1=s.strip()
print(s1)
s2=s.lstrip("hyd")
print(s2)
s3=s.rstrip("yani")
print(s3)
