
#Nested if-else is used to check conditions inside another condition for multi-level decision making
marks = 85

if marks >= 50:
    if marks >= 75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")