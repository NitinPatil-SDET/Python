# 🔹 1. What is File I/O?
# File I/O = reading from and writing to files
# Used for logs, reports, test data, configs
# Text Files : .txt, .docx, .log etc


# 🔹 2. Opening a File
#f = open(r"Day11\data.txt", "r")
# "r" → read (Open for reading - default)
# "w" → write (overwrites file)
# "a" → append (End of the file if it exists)
# "x" → create new file
#f = open(r"Day11\data1.txt", "x")

# data = f.read()
# print(data)
# f.close()
#f.write("This is nitin")

# with open(r"Day11\data.txt", "r") as f: #Always Use with (Best Practice) Automatic close
#    # print(f.readline())     #one line
#    # print(f.readlines())    #Multiple line
#    # print(f.read(5))         #This_  (first 5 char only)
#     print(f.readline())  #This is Halku.
#     print(f.readline())     #this is spidy


#Writing to the file
a = open(r"Day11\data1.txt", "w")
a.write("I am Groooteee.......")
a.close()

#Write & read
b = open(r"Day11\data1.txt", "w+")
b.write("I am HAlku hu re .......")
b.close()

# r → read file (error if file doesn’t exist)  
# w → write file (creates file, overwrites if exists)
# x → create new file (error if already exists)
# a → append to file (creates if not exists, adds at end)
# b → binary mode (used for non-text files like images)
# t → text mode (default, for text files)
# + → read and write both (update mode)

# Deleting file
#Use os.remove() to delete a file
#pip - package installer python

import os
os.remove(r"Day11\data1.txt")



# open() → opens a file with a specific mode (r, w, a, etc.)
# with statement → auto-manages file closing (best practice)
# read() → reads entire file content
# readline() → reads one line at a time
# readlines() → reads all lines into a list
# write() → writes data to file (overwrites in w mode)
# append (a) → adds data without deleting existing content
# file modes → control how file is opened (read/write/append/binary)
# file pointer → tracks current position (tell(), seek())
# exception handling → prevents crashes (try-except)
# os module → used for file operations (exists, delete, rename)
# JSON handling → read/write structured data using json module
# CSV handling → read/write tabular data using csv module
# binary files → handle non-text files using b mode