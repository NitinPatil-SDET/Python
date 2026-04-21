
#WAF for for chanhge java to python


path = "Day11/Practice.txt"

with open(path, "r") as f:
    data = f.read()
    print(data)

new_data = data.replace("Java", "Python")

with open(path, "w+") as f:
    f.write(new_data)
    print(f.read())

    
    

