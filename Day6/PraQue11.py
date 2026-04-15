#WAP to check if a list contains a palindrome of element.

myList = ["N","I","T","I","N"]
copyList = myList.copy()
#reverse() modifies the list and returns None, so never use it directly in comparisons.
copyList.reverse()

if myList == copyList:
    print("The given list is palindrome")
else:
    print("The given list is not palindrome")