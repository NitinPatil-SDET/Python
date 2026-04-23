#del keywords
#Use to delete object properties or object itsel

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Nitin")
# print(s1.name)  #Nitin
# del s1
# print(s1.name)  #NameError: name 's1' is not defined

#Private(like) attribute & method
#This attribute & method are menant to be used only within the class and are not accessible from outside the clas
# Public & Private (in java)
# To make private in python just applye __acc_no

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no        # public attribute
#         self.__acc_pass = acc_pass  # private attribute
    
#     def printpass(self): # This a public method to access private method/attribute within class 
#         return self.__acc_pass

# acc1 = Account("12345", "test")
# print(acc1.acc_no)       #12345
# #print(acc1.acc_pass)    #AttributeError: 'Account' object has no attribute 'acc_pass'
# print(acc1.printpass())  #test

#to access __acc_pass we have to create new public method to access private attribute in same class

#-------------------------------------------------------------------------------------------------------------------------------------
# super() Function
# super() function is used to call the parent class’s methods. In particular, 
# it is commonly used in the child class's __init__() method to initialize inherited attributes. 
# This way, the child class can leverage the functionality of the parent class.

# Parent Class: Animal
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print("Animal name:", self.name)

# # Child Class: Dog
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)   # Call parent constructor
#         self.breed = breed

#     def details(self):
#         print(self.name, "is a", self.breed)

# d = Dog("Buddy", "Golden Retriever")
# d.info()      # Parent method
# d.details()   # Child method


#--------------------------------------------------------------------------------------------------------------------------------------------
#class method --> A class method is bound to the class & recive the class an 

class Person:
    name="anonymous"

    def changeName(self, name):
        self.name = name
