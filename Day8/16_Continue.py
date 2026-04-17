#The continue statement in Python is used to skip the current iteration of a loop and move to the next iteration, 
# without stopping the loop

#When Python sees continue, it:
#Skips the remaining code inside the loop for that iteration
#Goes back to the loop condition and continues with the next cycle

i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)