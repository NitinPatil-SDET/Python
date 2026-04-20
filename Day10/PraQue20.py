#WAP to find average of the 3 number

def avrage(a,b,c):
    return (a+b+c)/3

print(avrage(2,2,2))
print(avrage(11,45,89))

#WAP to give product of 2 number
def product(a=2,b=3):
    return a*b

print(product())

#Wap to print the length of a list(list is parameter)
city = ["pUne","Mumbai", "Dholakpur", "chennai","Delhi","Nashik" ]
def length(list):
    print(len(list))
length(city)

#WAP to to print element of his list in single line (list is the parameter)
def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(city)      


