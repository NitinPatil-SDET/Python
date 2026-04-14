#WAP to find the greatest of 3 numbers enter by th user 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
max = 0

if(a>b and a>c):
    max=a
elif(b>c and b>a):
    max=b
else:
    max = c

print("The greatest number is: ", max)


