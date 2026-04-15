#A built-in data type that lets us create immuatable sequence of value
#Once you create, then u can't modify

# A tuple is an ordered, immutable collection of elements.
# Defined using parentheses () (or just commas).
# Allows duplicate values.
# Supports multiple data types.
# Indexed starting from 0 (supports negative indexing).
# Immutable → cannot add, remove, or modify elements after creation.
# Faster than lists due to immutability.
# Uses less memory compared to lists.
# Supports slicing (tuple[start:end:step]).
# Can be iterated using loops.
# Common methods: count(), index() (only two, because immutable).
# Can be used as dictionary keys (if elements are immutable).
# Supports packing and unpacking (a, b = (1, 2)).
# Single-element tuple requires comma ((5,)).
# Nested tuples are allowed.
# Cannot be sorted/modified directly (need conversion to list).



tup1 = (3,5,7,3,2)
print(tup1) #{2, 3, 5, 7}

tup2 ={}
print(tup2) #{}
print(type(tup2)) #<class 'dict'>

#Slicing is posssible in tupple is same as list 

#Tuple methos
tup3 = (2,1,3,1)
print(tup3.index(1))
print(tup3.count(1))


# | Feature     | List                 | Tuple                         |
# | ----------- | -------------------- | ----------------------------- |
# | Mutability  | Mutable (can change) | Immutable (cannot change)     |
# | Syntax      | `[]`                 | `()`                          |
# | Performance | Slower               | Faster                        |
# | Memory      | More                 | Less                          |
# | Methods     | Many methods         | Only `count()`, `index()`     |
# | Use Case    | Dynamic data         | Fixed/constant data           |
# | Hashable    | ❌ No                 | ✅ Yes (if elements immutable) |
# | Sorting     | `sort()` available   | Not available                 |


