#Abstraction - Hiding the implementation details of the class and only showing the essential feature to the user
#Inheritance - Wrapping data and function into a single unit(Object)


class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.acc=True
        self.clutch=True
        print("Car Stared........")
    
c1 = Car()
c1.start() #Abstraction 











