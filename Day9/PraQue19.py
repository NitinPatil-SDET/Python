#WAP to find the sum of first n natural number (Using while)

n=10
sum=0
for i in range (1,n+1):
    sum += i

# print("Total sum :",sum)

n=10
sum=0
i=1
while i<=n:
    sum += i
    i+=1

print("Total sum :",sum)




#WAP to find the factorial of first n number 
n=12
fact=1
i=1
while i<=n:
    fact *= i
    i+=1
print("Tha factorial: ", fact)    

n=5
fact=1
for i in range(1,n+1):
    fact*=i

print("Tha factorial: ", fact)  