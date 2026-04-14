# if → Executes a block of code when the condition is true
# elif → Checks another condition if the previous if/elif condition is false
# else → Executes a block when all previous conditions are false
# 👉 Python checks conditions top to bottom and executes the first true block, otherwise runs else
# in


age = 21
if(age >= 18):
    print("can vote & Apply for Driving liecence")

light = "green"
if(light == "red"):
    print("STOP")
elif(light == "green"):
    print("GO")
elif(light =="yellow"):
    print("LOOK")

#Indentation means using spaces (or tabs) to define code blocks (scope) in Python.
if True:
    print("Hello")   # indented → inside if block
print("Outside")     # not indented → outside block

