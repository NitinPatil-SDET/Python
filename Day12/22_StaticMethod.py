#Static Method : Method that don't use the self parameter (work at class level)
#Decoratore : allow us to wrap another function in order to extend the behaviour of the wrapped function,
#without permanetly modifying it


class Student:
    @staticmethod # decoratore
    def colleg():
        print("This is Static method....")

s1 = Student()
s1.colleg()

