print("--------------------Number from 1 to 10---------------") 
i=1
while i<=10:
    print(i)
    i+=1

print("---------------------Number from 10 to 1---------------")
j=10
while j>=1:
    print(j)
    j-=1

print("---------------------Multiplication table of n (Number given by user)---------------")
n = int(input("Please enter numbe: "))
k=1
while k<=10:
    print(k*n)
    k+=1

print("--------------Print the elements of the following list using while loop---------------")
mylist = [1,4,6,8,33,67,93,76,100]
lenth= len(mylist)
i=0
while i<lenth:
    print(mylist[i])
    i+=1

print("--------Search the number x(user input) in the given tuple-------")
tup =(4,6,8,33,67,93,76,100)
x =int(input("Enter number to search: "))

found = False 
n=0

while n<len(tup):
    if tup[n]==x:
        print("found at index", n)
        found = True
        break
    n+=1
if not found:
    print("Not found")


