#Write a recursive fuction to calculate the sum of n natural number

def add(n):
    if(n==0):
        return 0
    else:
        return (n + add(n-1))

#print(add(4))
#print(add(10))

#Write a recuresive function to print all elements in list
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "banana", "apple","halku"]

print_list(fruits, 0)