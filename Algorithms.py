1.
print("Hello world")

2.
a=int(input("Enter a number="))
b=int(input("Enter another number="))
s=a+b
print("Sum of a :",a,"and b :",b,"is =",s,".")

3.
a=int(input("Enter a number="))
b=int(input("Enter another number="))
c=int(input("Enter another number="))
m=a*b*c
print("Multiplication of three numbers a:",a,",b:",b,"and c:",c,"is =",m)

4.
a=int(input("Enter a number="))
if a % 2 ==0:
      print("Entered number is even.")
else:
      print("Entered number is odd.")

5.
age = int (input("Enter your age ="))
if age>=10 and age <40:
   print("You get 20 % discount ")
elif age>=40 and age <80: 
   print ("You get 50% discount ")
elif age<10 and age >=80 and age >0:
   print ("You get 100 % discount")
else:
   print ("Invalid!!!!")

6.
a=input("Enter your CT scan report=")
if a=="OK":
    b=input("Enter your MRI scan report=")
    if b=="OK":
        print("You are discharged from the hospital!!")
    else:
        print("Admit in hospital for 7 days!!!")
else :
    print("Admit in hospital for 7 days!!!!")