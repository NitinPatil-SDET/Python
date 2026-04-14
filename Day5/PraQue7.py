# Write a Python program to assign a grade to a student based on marks.

# Conditions:
# 90–100 → A
# 75–89 → B
# 60–74 → C
# 40–59 → D
# Below 40 → Fail

marks = int(input("Please Enter your marks: "))

if(marks >= 90):
    print("Congratulations! You got an A grade.")
elif(marks <90 and marks >= 75):
    print("Congratulations! You got an B grade.")
elif(marks <75 and marks >= 60):
    print("Congratulations! You got an C grade.")
elif(marks <60 and marks >= 40):
    print("Kathavar Pass")
else:
    print("Bhai tu ata jeev de")