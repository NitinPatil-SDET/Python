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


