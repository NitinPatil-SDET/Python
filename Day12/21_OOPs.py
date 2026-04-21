#    What is OOP?
#   OOP = organizing code using objects and classes
#   Focus = real-world modeling + reusability
#The concept of reusability up and redundancy down suggests that as software components become more reusable, 
# the need for redundancy in code decreases.


# Class
# A class is a collection of objects. Classes are blueprints for creating objects. 
# A class defines a set of attributes and methods that the created objects (instances) can have. 
# Classes are created by keyword class.
# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using the dot (.) operator. 
# Example: Myclass.Myattribute


# Objects
# An Object is an instance of a Class. 
#  It represents a specific implementation of the class and holds its own data. An object consists of:
# State: It is represented by the attributes and reflects the properties of an object.
# Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.
# Identity: It gives a unique name to an object and enables one object to interact with other objects.


#__init__() is a constructor method that runs automatically when a new object is created. 
# It is used to initialize object data.
#self refers to the current object, allowing each object to store and access its own data.
#self.name and self.age are instance attributes, unique to each Dog object created from the class.


# class Student:                  # Class name should start with capital
#     name = "Nitin Patil"

# s1 = Student()          #Obeject initialization
# print(s1.name)

# class Car:
#     colour = "Red"
#     brand = "Tesla"

# car1 = Car()
# print(car1.colour)
# print(car1.brand)





class Dog:
    species = "Canine"  # Class attribute
    #Parameterised constructor
    def __init__(self, name, age): 
        print("Adding new Dog in database")    
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

dog1 = Dog("tillu", 3)
print(dog1.age)
print(dog1.name)

dog2 = Dog("billu", 5)
print(dog2.age)
print(dog2.name)

#Class & Instance Attribute
#class attribute -->
#Instance attribute --> 


#class --> data(Attributes) & method

class Student:
    def welcom(self):
        print("Welcome Student", self.nams1)


class Student:
    school = "ABC"   # class variable

    def __init__(self, name):
        self.name = name   # instance variable
