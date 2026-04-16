# 🔹 Basics
#  A dictionary is an unordered, mutable collection of key-value pairs.
#  Defined using curly braces {}.
#  Format → {key: value}
#  Keys must be unique and immutable (int, string, tuple).
#  Values can be any data type.

my_dict = {"name":"Halku",
            "age":5,
            "Gav": "Mirzapur",
            "Skill": ["AI lang", "Insta Reel", "Famous"]}

print(my_dict)  #{'name': 'Halku', 'age': 5, 'Gav': 'Mirzapur', 'Skill': ['AI lang', 'Insta Reel', 'Famous']}
print(type(my_dict)) #<class 'dict'>

# 🔹 Accessing Data
# dict[key] → access value (throws error if key not found)
# dict.get(key) → safe access (returns None if not found)

print(my_dict["name"]) #Halku
print(my_dict.get("name")) #Halku
     
#print(my_dict["name1"]) #KeyError: 'name1' and terminate the program
print(my_dict.get("name1")) #None and contniue the program
my_dict.clear()
# 🔹 Adding / Updating
# dict[key] = value → add or update
# dict.update({...}) → update multiple values
print("----------Adding / Updating-----------") 

# Example dictionary
person = {"name": "Alice", "age": 25}

# 1️⃣ Add or update a single key-value pair using subscript notation
person["city"] = "Mumbai"       # Adds new key 'city'
person["age"] = 26              # Updates existing key 'age'

# 2️⃣ Add or update multiple key-value pairs using update()
person.update({"age": 27, "country": "India"})

# 3️⃣ You can also use keyword arguments with update()
person.update(language="Python", hobby="Reading")

# Display final dictionary
print(person)

# ✅ Key Points:
# dict[key] = value → Adds a new key if it doesn’t exist, otherwise updates the value.
# dict.update({...}) → Updates multiple keys at once; adds new keys if they don’t exist.
# dict.update(key1=value1, key2=value2) → Another way to update using keyword arguments.

print("------------------------Removing----------------------")
# Removing
# pop(key) → removes key and returns value
# popitem() → removes last inserted item
# del dict[key] → deletes key
# clear() → removes all items

print(person.pop("age"))
print(person.popitem())
del person["name"]
print(person.get("name"))
person.clear()
print(person)

print("----------------------------- Common Methods-----------------------------------------------------")
# 🔹 Common Methods
# keys() → returns all keys
# values() → returns all values
# items() → returns (key, value) pairs
# get() → safe access
# update() → merge dictionaries
# copy() → shallow copy

student = {"name":"IronMan", "rollno":101, "subject":["Marathi", "Hindi", "English"] }
print(student.keys()) #dict_keys(['name', 'rollno', 'subject'])
print(student.values())
print(student.items())

#🔹 Nested Dictionary
data = {
    "user1": {"name": "A", "age": 25},
    "user2": {"name": "B", "age": 30}
}

print(data) #{'user1': {'name': 'A', 'age': 25}, 'user2': {'name': 'B', 'age': 30}}