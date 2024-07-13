# class hero :
#     a = 3
#     #mrthods 
#     def __init__(self) -> None:
#         pass
#     def abhi():
#         print('function')

# print(hero)    

# #function
# def abhi():
#     print('function')


# class hero :
#     a = 3
#     #mrthods
#     def __init__(self , name):
#         self.name = name
#         print(name)
   
# obj = hero('dipen')

# class animal :
#     # work = "bark"
#     def __init__(self ,name ,  food , work):
#         self.name = name
#         self.food = food 
#         self.work = work
#         print(f"Name : {self.name} , food : {self.food} , work : {self.work}")

#     def view_details(self):
#         print( self.name +self.food + self.work)

# #Creating objects of class animal 

# #object_name = class_name(parameters value)

# anil1 = animal("dog" , "pasta" , "bark")
# anil2 = animal("cat " , "noodles" , "meow")
# # anil1.view_details()
# # anil2.view_details()



                             #INSTANCE_CLASS

class house ():
    def __init__(self , owner):
        self.owner = owner

    def set_house_color(self , color):
        self.color = color 

    def get_house_color(self):
        return (f"House Owner : {self.owner}" +" , " + f"House color : {self.color}")

mero_ghar = house ('lily')
mero_ghar.set_house_color("blue")
print(mero_ghar.get_house_color())

mero_ghar2 = house ("Abhishek")
mero_ghar2.set_house_color("yellow")
print(mero_ghar2.get_house_color())

