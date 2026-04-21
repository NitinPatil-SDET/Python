#WAF to find in which line of the file does the word "learning" occurec first.
#Print -1 if word not found

path = "Day11/Practice.txt"
word = "learning"
def find_word(word):
    with open(path, "r") as f:
        line_no = 1
        found = False
        for line in f :
            if word in line:
                print(line_no)
                found = True
                break
            line_no += 1
        if not found:
            print(-1)

find_word(word)     #1
find_word("AI")     #2
find_word("Nitin")  #-1
            


