#Print function in python work as below 

#1. What print() Does print() sends output to the standard output stream, usually the console/terminal.
print("Hello Nitin")

#2. Printing Multiple Values
print("Name:", "Nitin", "Age:", 26)

#3. sep Parameter (Separator) sep defines what separates multiple values.Default separator = space " "
print("Java", "Python", "Selenium", sep="-")
print("2026", "03", "05", sep="/")

#4. end Parameter By default, print() ends with a newline \n.
print("Hello")
print("World")

#If you change end:
print("Hello", end=" ")
print("World")

#Another example:
print("Loading", end="...")
print("Done")

#5. Printing Variables
name = "Nitin"
age = 26

print(name)
print(age)

#6. Formatted Printing (Very Important)
name = "Nitin"
print("Hello %s" % name)

#.format() Method
name = "Nitin"
age = 26
print("My name is {} and I am {}".format(name, age))

#f-Strings (Best Way) Modern Python uses f-strings.
name = "Nitin"
age = 26
print(f"My name is {name} and I am {age}")

#7. Printing Different Data Types - Python automatically converts objects to string.
print(10)
print(3.14)
print(True)
print([1,2,3])
print({"name":"Nitin"})

#8. Escape Characters Escape characters allow special formatting.
print("Hello\nWorld")

#| Escape | Meaning      |
#| ------ | ------------ |
#| `\n`   | New line     |
#| `\t`   | Tab          |
#| `\\`   | Backslash    |
#| `\"`   | Double quote |
