#🔹 Basics
#Recursion is when a function calls itself to solve a problem.
#Used to break a problem into smaller subproblems.

#🔹 Structure (must follow)
# Must have base case → stops recursion
# Must have recursive case → function calls itself

# def func(n):
#     if n == 0:      # base case
#         return
#     func(n-1)       # recursive call

def show(n):
    if(n == 0):     # base case
        return
    print(n)
    show(n-1)       # recursive call

#show(5)

#Recursion for factoreal
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

print(fact(5))


