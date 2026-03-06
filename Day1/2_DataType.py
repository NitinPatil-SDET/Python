#Data Type in Python? - A data type defines what kind of value a variable can store.

#Main Categories of Python Data Types
#1. Numeric Types
#2. Boolean Type
#3. Sequence Types
#4. Set Type
#5. Mapping Type
#6. User-defined Types

#Numeric Types - These represent numbers.

#Integer (int) - Whole numbers without decimals.
print(10)
print(-5)
print(1000)
#Python integers have no fixed limit.
print(999999999999999999999999999)

#Float (float) - Numbers with decimal points.
print(4.5)
print(0.25)
print(-3.14)
#Python also supports scientific notation.
print(1e3)
print(1e308) #--> 1e+308
print(1e309) #--> inf (inf means infinity, because it exceeds the float limit.)

#Complex Numbers (complex) - Used in mathematics and engineering.
print(4 + 5j)

#Boolean Type
print(True)
print(False)
print(10 > 5)

#String Type (str) Strings store text data. You can use three quotation styles.
#Strings are immutable, meaning they cannot be changed after creation.
print('Kolkata')
print("Kolkata")
print("""Kolkata""") #Triple quotes (multiline strings)