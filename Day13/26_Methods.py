# 🔹 1. Instance Method
# Works with object data (self)
# Can access & modify instance attributes
# Instance method → works on object (self) data

class Student:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):   # instance method
        self.name = new_name

s = Student("A")
print(s.change_name("B"))



# 🔹 2. Class Method
# Works with class data (cls)
# Can access/modify class variables
# Class method → works on class (shared) data

class Student:
    school = "ABC"

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

print(Student.change_school("XYZ"))

# 🔹 3. Static Method
# No access to self or cls
# Just a utility/helper function inside class
# Static method → no relation to object or class data
class Student:
    @staticmethod
    def greet():
        print("Hello")

print(Student.greet())




# | Type            | Uses `self` | Uses `cls` | Purpose               |
# | --------------- | ----------- | ---------- | --------------------- |
# | Instance Method | ✅           | ❌          | Work with object data |
# | Class Method    | ❌           | ✅          | Work with class data  |
# | Static Method   | ❌           | ❌          | Utility function      |


#----------------------------------------------------------------------------------------------------
# 🔹 What is @property?
# Allows you to access a method like an attribute
# Used to control access to data (getter/setter logic)

class Student:
    def __init__(self, marks):
        self._marks = marks   # internal variable

    @property
    def marks(self):         # getter
        return self._marks

s = Student(90)
print(s.marks)   # looks like variable, actually calls method

class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value < 0:
            print("Invalid marks")
        else:
            self._marks = value

s = Student(90)
s.marks = 80   # setter called

# 🔹 Why Use @property?
# Hide internal data (_marks)
# Add validation logic
# Maintain clean syntax (no need for getMarks())

# @property → use method like attribute (getter)
# @x.setter → set value with validation
# @x.deleter → delete attribute


