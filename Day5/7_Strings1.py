#Basic Operations
#1. Creation of the string 

str1 = 'This is Single Quotes'
str2 = "This is Double Quotes"
str3 = '''This is Triple Quotes'''

# When to choose one over the other:
# Use ' ' when your string contains "
# Use " " when your string contains '

a = "It's fine"     # no escape needed
b = 'He said "Hi"' # no escape needed

# | Type      | Use Case               | Multi-line | Escape needed |
# | --------- | ---------------------- | ---------- | ------------- |
# | `' '`     | Normal string          | ❌ No       | Sometimes    |
# | `" "`     | Normal string          | ❌ No       | Sometimes    |
# | `''' '''` | Multi-line / docstring | ✅ Yes      | ❌ No        |
# | `""" """` | Multi-line / docstring | ✅ Yes      | ❌ No        |



#2. Python escape sequence characters:
# \n → New line (moves text to next line)
# \t → Tab space (adds horizontal spacing)
# \\ → Backslash (\)
# \' → Single quote
# \" → Double quote
# \r → Carriage return (moves cursor to start of line)
# \b → Backspace (removes previous character)
# \f → Form feed (page break, rarely used)
# \v → Vertical tab (rarely used)
# \0 → Null character

#Only \n, \t, \\, quotes are used daily

# print ("Hello \nWorld!!!")
# print ("Hello \t world")
# print("This is backslash : \\")
# print('It\'s fine')
# print("He said \"Hello\"")
# print("Hello\rWorld")
# print("Helloo\b")
# print("Hello\fWorld")
# print("Hello\vWorld")
# print("Hello\0World")

#3 Concatenation
print(str1+str2) #This is Single QuotesThis is Double Quotes
print(str1+" "+str2) #This is Single Quotes This is Double Quotes
print(str1+"---"+str2) #This is Single Quotes---This is Double Quotes

#4 Length
print(len(str1)) #21


# 5. Indexing
# Used to access a particular character in a string
# We can only access characters, not modify them (strings are immutable)
str = "This is Nitin"
print(str[1]) #h

#6 Slicing
# Accessing part of a string 
# string[start : end : step]
# start → where to begin (included)
# end → where to stop (excluded)
# step → how many steps to move

text = "Mai Halku hure"
print(text[1:6]) #ai Ha

print(text[0:6:2]) #MiH
print(text[0:6:1]) #Mai Ha
print(text[0:len(text):3]) #MHu-4  #M l-3


text = "Python"
print(text[::-1])

text = "Python"
print(text[:3])   # start default = 0
print(text[3:])   # end till last

print("----------------------String Function---------------------")
#7 String function : String functions (methods) are used to perform
# operations on strings without modifying the original string (because strings are immutable).

# endswith() → Checks if the string ends with a given substring
# startswith() → Checks if the string starts with a given substring
# capitalize() → Converts the first character to uppercase
# upper() → Converts all characters to uppercase
# lower() → Converts all characters to lowercase
# title() → Converts first letter of each word to uppercase
# replace() → Replaces all occurrences of a substring with a new value
# find() → Returns index of first occurrence of substring (-1 if not found)
# index() → Same as find but throws error if not found
# count() → Counts occurrences of a substring
# strip() → Removes spaces from both ends of string
# lstrip() → Removes spaces from left side
# rstrip() → Removes spaces from right side
# split() → Splits string into list based on delimiter
# join() → Joins elements of list into a string
# isalpha() → Checks if all characters are alphabets
# isdigit() → Checks if all characters are digits
# isalnum() → Checks if string is alphanumeric
# isspace() → Checks if string contains only spaces



String = "i am spidy"
print(String.endswith("idy")) # True

print(String.capitalize()) 

print(String.replace("spidy", "halku"))

print(String.find("m"))
print(String.find("spidy"))
print(String.find("q"))

print(String.count("i"))
print(String.count("am"))



