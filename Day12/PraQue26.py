#Create a student class that takes name & mark of 3 subject as argument in constructor.
#Then create method to print the average

class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hii ", self.name, " your avaeage score is: ", sum/3)



s1 = Student("Halku", [12, 87,90,78])
# print(s1.name)
# print(s1.marks)
s1.get_avg()

s1.name = "IronMan"
s1.get_avg()

