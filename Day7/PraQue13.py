#1. Count Frequency
#Write a program to count how many times each element appears in a list.
# Input: [1, 2, 2, 3, 1, 4, 2]
# Output: {1:2, 2:3, 3:1, 4:1}

Input = [1, 2, 2, 3, 1, 4, 2]

Output ={}
for item in Input:
    if item in Output:
        Output[item] += 1
    else: 
        Output[item] = 1

for Input, count in Output.items():
    print(f"{Input}: {count}")


