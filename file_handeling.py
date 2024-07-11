# file = open ('example.txt' , 'r')

# file_name_read = file.read()

# print(file_name_read)

# file.close()



# with open ('example.txt', 'r') as file:
#     content = file.read()
#     print(content)


# file = open ('example.txt' , 'w')
# file.write("Hi world")

# file.close()


# file = open ('example.txt' , 'a')
# file.write("Hi world . ")

# file.close()

# file = open('example.txt' , 'r')
# name = file.read
# print(name)
# file.close()


import json
data = {
    'name' : 'Ram',
    'age' : 18 ,
    'city' : 'Butwal'
}

with open('example.txt' , 'w') as file :
    json.dump(data , file , indent=4)




