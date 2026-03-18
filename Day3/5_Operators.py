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