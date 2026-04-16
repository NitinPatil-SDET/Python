#WAP to enter marks of 3 subject from the user and store them in a dictionary. start with an empty 
# dictionary & add one by one. Use subject name as key & marks as Value

marks = {}

x = int(input("Enter Physics marks: "))
marks.update({"Phy":x})

y = int(input("Enter Math marks: "))
marks.update({"Math":y})

z = int(input("Enter Biology marks: "))
marks.update({"Bio":z})

print(marks)

