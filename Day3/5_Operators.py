# Operators in Python
# Arithmetic: +, -, *, /, %, **, //
# Comparison: ==, !=, >, <, >=, <=
# Logical: and, or, not
# Bitwise: &, |, ^, ~, <<, >>
# Assignment: =, +=, -=, *=, /=, %=, **=, //=
# Identity: is, is not
# Membership: in, not in


print('-----Arithmetic Operators---------')
# Arithmetic: +, -, *, /, %, **, //
a=5
b=20

print(a+b)
print(a-b)
print(a*b)
print(a/b) #In case division Output always be in float

print('-----Comparison Operators---------')
# Comparison: ==, !=, >, <, >=, <=
print(a==b)   #False
print(a!=b)   #True
print(a>b)    #False
print(a>=b)   #False
print(a<b)    #True
print(a<=b)   #True

print('-----Logical Operators---------')
# Logical: and, or, not
x=True
y=False

print(x and y) #False
print(x or y)  #True
print(not x)   #False
print(not y)   #True

# Bitwise: &, |, ^, ~, <<, >>
# x & y  → Bitwise AND: returns 1 only where both bits are 1  
# x | y  → Bitwise OR: returns 1 where at least one bit is 1  
# x ^ y  → Bitwise XOR: returns 1 where bits are different  
# x >> n → Right Shift: shifts bits right (divides by 2ⁿ)  
# x << n → Left Shift: shifts bits left (multiplies by 2ⁿ)  
# ~x     → Bitwise NOT: flips all bits (gives -(x+1))
print('-----Bitwise Operator')
p=2
q=5
print(p&q)  #0
print(p|q)  #7
print(p^q)  #7
print(p>>q) #0
print(p<<q) #64
print(~q)   #-6
print(~p)   #-3



print('-----Assignment Operators---------')
# =   → Assigns value to a variable  
# +=  → Adds and assigns (a = a + value)  
# -=  → Subtracts and assigns (a = a - value)  
# *=  → Multiplies and assigns (a = a * value)  
# /=  → Divides and assigns  
# //= → Floor divides and assigns  
# %=  → Modulus and assigns (remainder)  
# **= → Power and assigns (exponent)  

a=3 
print(a) #3

a += 3
print(a) #3+3=6

a -= 3
print(a) #6-3=3

a *= 3
print(a) #3*3=9

a /= 3
print(a) #9/3=3.0

print('-----Identity  Operators---------')

# * `is` → checks if two variables refer to the **same object in memory**
# * `is not` → checks if two variables refer to **different objects**
# * `==` → checks if two variables have the **same value**
# * Same value ≠ same object (don’t confuse `==` with `is`)
# * Use `is` only for **`None` comparison** (`x is None`)
# * Never use `is` for comparing numbers, strings, or lists
# * Python may reuse objects (interning), so `is` can be **unpredictable for values**
# * `is` → identity check, `==` → value check
# * Two variables can look identical but still be **different objects**
# * Safe rule: **use `==` for data, `is` only for `None`**

# Identity: is, is not
a=3
b=6
print(a is b) #False

b=3
print(a is b) #True


print('-----Membership  Operators---------')
# * `in` → checks if an element **exists inside a collection**
# * `not in` → checks if an element **does NOT exist in a collection**
# * Works with lists, tuples, sets, strings, and dictionaries
# * For lists/tuples → checks **value presence**
# * For strings → checks **substring presence**
# * For dictionaries → checks **keys only (not values)**
# * `x in dict` → checks key, not value
# * To check value in dict → use `x in dict.values()`
# * Membership returns **True or False**
# * Faster in sets/dicts, slower in lists (due to search time)
# * Case-sensitive for strings (`"a" in "Apple"` → False)
# * Safe rule: **use `in` for existence check, not for indexing or position**


