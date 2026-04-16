# 🔹 What is a Set?
# A set is an unordered, mutable collection of unique elements.
# Defined using curly braces {} or set()
# Automatically removes duplicates

my_set = {1, 2, 3, 3, 4}
print(my_set)   # {1, 2, 3, 4}

# 🔹 Key Properties (must know)
# ❌ No duplicates
# ❌ No indexing (my_set[0] → ERROR)
# ❌ Unordered (no fixed position)
# ✅ Fast operations (based on hashing)
# ✅ Mutable (can add/remove elements)

#🔹 Creating Sets
a = {1, 2, 3}
b = set([1, 2, 3])   # from list
empty = set()        # correct way (NOT {})--> It will create dict

# 🔹 Common Methods 
# add(x) → adds element
# remove(x) → removes element (error if not found)
# discard(x) → removes safely (no error)
# pop() → removes random element
# clear() → removes all elements

c = {1, 2, 3}
d = {3, 4, 5}
print("----------------------Common Methods -------------------------------")
print(c|d) #→ union → {1,2,3,4,5}
print(c&d) #→ intersection → {3}
print(c-d) #→ difference → {1,2}
print(c^d) #→ symmetric difference → {1,2,4,5}

#Membership Check (very important)
if 2 in a:
    print("Yes") #Yes

