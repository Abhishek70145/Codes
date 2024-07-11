"""Homework:-
1.take input from user so that which file user wants to create 
2.insert content inside file by asking user 
3.user needs to read file 
4. New input add garna paryo 
5.At last file must be deleted by asking user"""

1.
file_name = input("Enter a file name = ")
file = open (file_name , 'a')

2.
name = input("Enter your name = ")
surname = input("Enter your surname = ")
age = input("Enter your age = ")
address = input("Enter your address = ")

import json
data = {
    'Name' : name ,
    'Surname' : surname ,
    'Age' : age ,
    'Address' : address  
}
with open(file_name , 'w') as file :
    json.dump(data , file , indent=4)

3.
choice = input("Do you want to read the file Yes/No =")
if choice == "Yes" :
    with open ( file_name , 'r') as file:
          print(file.read())

4.
file = open (file_name , 'a')
file.write(input("Enter some content ="))

5.
delete = input(f"Do you want to delete the file : {file_name} ? (Yes/No) = ")

if delete == "Yes":
     import os
     os.remove(file_name) 









