#When one class(child / derived) derives the properties & methods of another class(parent / base)
class Car:                 #Parent class/ base class
    @staticmethod  #we use this to avoid the use of self 
    def start():
        print("Car Starded...........")

    @staticmethod
    def stop():
        print("Car stopedd..........")

class ToyataCar(Car):            #Child class/derived class derived from parent class
    def __init__(self, name):
        self.name = name

car1 = ToyataCar("fortuner")      #Obejct creation of child car

print(car1.name)        #fortuner               -->  child  class object calling
car1.start()            #Car Starded........... --> parent class object calling
car1.stop()             #Car stopedd..........  --> parent class object calling


#Single Inheritance -->  parent --> chlild
#Multi level Inheritance --> parent --> chlid -->grandchild
#Multiple Inheritance -->(like java interface)
# parent1 --> child <-- parent2

class parent1:
    varA = "Welcome to class PARENT1"

class parent2:
    varB = "Welcome to class PARENT2"

class child(parent1, parent2):
    varC = "Welcome to clas CHILD"

c1 = child()

print(c1.varA)
print(c1.varB)
print(c1.varC)

