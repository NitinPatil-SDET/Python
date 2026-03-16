# Assigning values to variables
x = 10            #Integer
name = "Nitin"    #String
pi = 3.14         #float
flag = True       #boolean

#Printing variable
print(x)
print(name)


#Key Points
#1. Dynamic Typing – You can change the type of a variable at runtime:
a = 5                       #Int
a = 'chane in varibale'     #now String

#2. Naming Rules:
    #Must start with letter or _ (underscores)
    #can contains letter, numbers and underscores
    #Case sensitive (age & Age are diifrent)
    #cannot be Python keaword (if, for, class etc)

#3. Multiple Assignments:
p,q,r = 1,2,3
x=y=z=4

#4. Variable Types:
num = 42           # int
price = 19.99      # float
text = "Hello"     # str
flag = True        # bool
items = [1, 2, 3]  # list

#5. Type Checking:
print(type(num))  # <class 'int'>
print(type(price))  # <class 'float'>
print(type(text))   # <class 'str'>

# Example Program:
stuName = 'Iron Man'
rollNum = 12
marks = 77.77
isActive = True

#print(stuName, rollNum, marks, isActive) # Iron Man 12 77.77 True
print(f"The Student name is :{stuName} , his roll number is {rollNum}, and he has {marks}, is he Present Today {isActive}" )
