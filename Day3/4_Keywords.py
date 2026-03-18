#Python is case sensitive
#Keywords: reserved words, special meanings
#Cannot use as variable names

# Python has 33 keywords.
import keyword
print(keyword.kwlist)

#Identifiers
#Identifier are name for var, func, class, module, etc.

# Rules:
# 1.Start with letter or _
# 2.Followed by letters, digits, _
# 3.Not a Python keyword

'''
False – Boolean value representing false  
None – Represents absence of value (null)  
True – Boolean value representing true  
and – Logical operator (both conditions must be true)  
as – Used for aliasing (import/context manager)  
assert – Checks condition, raises error if false  
async – Defines asynchronous function  
await – Waits for async operation to complete  
break – Exits loop immediately  
class – Defines a class (OOP structure)  
continue – Skips current loop iteration  
def – Defines a function  
del – Deletes variable or object  
elif – Else-if condition  
else – Executes if previous conditions fail  
except – Handles exceptions (errors)  
finally – Executes always after try-except  
for – Loop over iterable  
from – Imports specific parts from module  
global – Declares global variable inside function  
if – Conditional statement  
import – Imports module  
in – Checks membership in collection  
is – Checks object identity (same memory)  
lambda – Anonymous one-line function  
nonlocal – Refers to outer (non-global) variable  
not – Logical negation  
or – Logical operator (any condition true)  
pass – No operation (placeholder)  
raise – Manually throws exception  
return – Returns value from function  
try – Defines block to catch exceptions  
while – Loop while condition is true  
with – Context manager (auto resource handling)  
yield – Returns value from generator (lazy execution)
'''