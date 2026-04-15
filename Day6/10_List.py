#List is built-in datatype that store set of value
#It can store elements of different type(int, float, string, etc)
#String is immutble & List are mutabale


# A list is an ordered, mutable collection of elements.
# Defined using square brackets [].
# Allows duplicate values.
# Supports multiple data types.
# Indexed starting from 0 (supports negative indexing).
# Mutable → elements can be added, removed, or modified anytime.
# Supports dynamic size (can grow/shrink).
# Supports slicing (list[start:end:step]).
# Can be iterated using loops.
# Common methods: append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy().
# Supports nested lists (list inside list).
# Cannot be used as dictionary keys (because mutable).
# Supports list comprehension for concise creation.
# Slower than tuples due to mutability overhead.
# Can be converted to tuple using tuple().
# ⚠️ Straight truth
# Overusing lists when data is fixed = bad design (use tuple)
# Misusing sort() expecting return value = common mistake

myList = [1, 2, 3, 4, 5]
print(myList)
print(type(myList))
print(len(myList))

student = ["Halku", 105, "Dholakpur"]
print(student[0])
student[0] = "spidy"
print(student[0])
#print(student[4]) #IndexError: list index out of range

#List Slicing
#list_name[starting_index: ending_index]

marks = [1,2,33,44,5,6,7,8]
print(marks[1:])
print(marks[:len(marks)])
print("------------------------------List Methos--------------------------------")
#List Method
marks.append(99) #None
print(marks) #[1, 2, 33, 44, 5, 6, 7, 8, 99]
print(marks.sort()) #None
print(marks) #[1, 2, 5, 6, 7, 8, 33, 44, 99]

print(marks.sort(reverse=True)) #None
print(marks) #[99, 44, 33, 8, 7, 6, 5, 2, 1]

fruits=["Apple", "yak", "Banana"]
fruits.sort()
print(fruits) #['Apple', 'Banana', 'yak']

marks.reverse()
print(marks) #[1, 2, 5, 6, 7, 8, 33, 44, 99]

# append(x) → adds element to end
# extend(iterable) → adds multiple elements to end
# insert(i, x) → inserts element at specific index
# remove(x) → removes first occurrence of value
# pop() → removes last element (or index if given)
# clear() → removes all elements
# index(x) → returns index of first occurrence
# count(x) → counts occurrences of element
# sort() → sorts list (ascending by default)
# reverse() → reverses list order
# copy() → returns shallow copy of list
