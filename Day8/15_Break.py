#The break statement in Python is used to exit a loop immediately, even if the loop condition is still true.
#When Python encounters break, it stops the loop right away and moves to the next line after the loop.

i=1
while i<=5:
    if i==3:
        break
    print(i)
    i += 1

#The loop stops when i == 3, so 3, 4, 5 are never printed.