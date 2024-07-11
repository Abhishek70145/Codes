# s=a+b 
# print("The sum of a:",a,"and b:",b,"is",s)

# a=input("Enter your name=")
# b=input("Enter your age=")
# c=input("Enter your address=")
# print ("My name is",a+".I'm",b+"years old."+"I live in",c+".")

# fruits=['apple','banana','mango']

# for fruit in fruits: a= 12
# b=14
# vowel=''
# for letter in fruit:
#                 if letter in 'aeiou'and letter not in vowel:
#             vowel+=letter
# print(fruit,vowel)

# a="Hello"
# b="Jarvis"
# c=12.4
# d="Could you please give me"
# e="30 rupees"
# print(a,b,c,d,e,'.')

# a="Hello"
# b="I am"
# c="programmer."
# d="a"
# print(a,",",b,d,c)
# a=12.5
# b=1028397
# c=5j
# d=[1,2,3,4]
# e={1,2,3,4}
# f=True
# g={'name':'Abhishek'}
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))

# l=int(input("Enter length="))
# b=int(input("Enter breadth="))
# A=l*b
# print("Area of rectangle=",A)

# p = "Hello I Am A Programmer And I am Very Pro At it"
# # Display output ---->  I Am Hari And I eAt grammer

# print(p[6:7],p[8:10],p[0:1]+p[-17:-16]+p[22:23]+p[-2:-3:-1],p[24:27],p[6:7],p[21:22]+p[8:9]+p[-1],p[16:23])

# a="Hello I am Abhishek. I live in butwal."
# print(a[0:20:2]
# print(a[0::])

# b="I am Python developer"
# print(b[-11:-17:-1])

# a="Hello i am Abhishek Chhetri and I live in butwal-8,Sukkhanagar....."
# print(len(a))

# print("Hello\nAbhishek")

# print("Hello\rworld")

# print("Hello\tAbhishek")

# print("Hello\bAbhishek")

# print("\'hello\'")

# print("\110\145\154\154\157")

# print("\x48\x65\x6c\x6c\x6f")

# name="Hi i am Hari"
# lname="and I'm a doctor."
# print(f"{name} {lname}")

# x="Hi"
# y=780
# print(bool(x))
# print(bool(y))

# import datetime
# x=datetime.datetime.now()
# print(x)
# print(x.year)

# x=5
# y=2

# print(x**y)

# print(x//y)

# print(x==y)

# print(x>y)

# print(x<y)

# print(x<+y)

# print(x>+y)

# age=int(input("Enter your age="))
# if age>0 and age<=11:
#     print("You are a child...")
# elif age>11 and age<=18:
#     print("You are a teenager..")
# elif age>18 and age<=40:
#     print("You are a youth..")
# elif age>40 and age<=60:
#     print("You are adult")
# elif age>60 and age<=100:
#     print("You are a grandparent.")
# else:
#     print("Something went wrong!!!!\nCheck from beginning!!!!")

# a=[]
# print(type(a))

# l1=[10,20,30,50,60,70,80,90]

# l1[3]=100
# print(l1)

# print(l1[-6])

# l1.append(40)
# print(l1)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# l1=["mango","banana"]
# l2=["apple","cherry"]
# l1.extend(l2)
# print(l1)

# l1=["apple","banana","mango"]
# l1.insert(1,"litchi")
# print(l1)

# i=0
# while i<10:
#     print("I'm a python programmar...\n I'm very good at python...")
#     i+=1

# i=2
# while i<100:
#     print ("Even number=",i)
#     i+=2

# i=0
# while i>10:
#     print(i)
# else:
#     i+=1
#     print(i)

# for i in range(1,15):
#     print(i)

# i=0
# while i<10:
#     i+=1
#     if i == 5:
#         continue
#     print(i)

# a=['apple','ball','cat','toy']

# for i in a :
#     print(i)
#     for j in i:
#         print(j)

# l=[]
# i=0
# while i<100:
#     i+=2
#     l.append(i)
# print(l)

# l=[]
# i=int(input("Enter a number="))
# for i in range(i,101):
#     if i % 2==0:
#         l.append(i)
# print(l)

# newlist = [x for x in range(1,101)]

# print(newlist)

# newlist = [x for x in range(1,101) if x%2==0]

# print(newlist)


# l=["abc.mp3","cdf.mp4","efd.pdf","isk.pdf"]
# l2=[]
# for i in l:
#         a=i[-3:]
#         if a=="pdf":
#                 l2.append(i)
# print(l2)



# l=["abc.mp3","cdf.mp4","efd.pdf","isk.pdf"]
# l2=[]

# l2 = [i for i in l if i.endswith(".pdf")]

# print(l2)
        
       


# l=["apple","banana","mango"]
# l2=[]

# l2=[(i,j) for i in l for j in i
#     if j=="a" or j=="e" or j=="i" or j=="o" or i=="u"]
# print(l2)


# l=[1,2,3,4,5,6,7,8,9,10]

# l2=[i**2 for i in l if i % 2 == 0 ]
# print(l2)


# a=50

# print("C") if a>30 else print("B")

# print("D") if a>40 else print("C")

# a = ['apple', 'banana' , 'mango']

# for i in a : 
#     v = ''
#     for j in i :
#         if j in 'aeiou' and j not in v :
#             v += j
#     print (f"{i} : {v}")


# tuple=("Apple","Banana","Mango","Cherry")

# for i in tuple:
#     print(i)

# a=1,2,3,4,5

# print(type(a))

# """     1
#       2 1 2
#     3 2 1 2 3
#   4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5"""


# d={'class':{
#     '12':['Ram','Shyam']},
#    'att':13}

# print(d['class']['12'][1])

# def anmol():
#     print("hello world")

# anmol()


# class car:
#     colour="red"
#     wheel=4
#     speed="200 km/hr"

# BMW=car()
# print(BMW)

# lamborgini=car()

# lamborgini.colour="blue"
# print(lamborgini.colour)



# class car:
#     colour="red"
#     wheel=4
#     speed="200 km/hr"

# def start():
#     print("Car started")

# BMW=car()
# print(BMW.start())

# # SWAP VARIABLES
# a = 55
# b = 45

# temp = a
# a = b
# b = temp

# print(f"The value of a = {a} and value of b = {b}")

# x = "Hello World"
# print(x[-1])

# x = 103.192
# print(int(x))


# l = [1,2,3,4,5]

# t = (6,7,8,9,10)

# print(list(t))


# a = 23
# b = 8392
# print(a == b)


# fruits = ["Apple", "Mango", "Cherry", "Banana", "Orange" , "Papaya"]

# x = len(fruits)

# a = int(input("Enter a number (1-6): "))

# if 1 <= a <= x:
#     print(fruits[a - 1])
# else:
#     print("Invalid input")


# def greet(hello):
#     return hello

# print(greet('Hello world'))

# l =["apple",["mango","cherry"],"banana"]


















