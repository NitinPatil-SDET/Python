#WAP to ask the user to enter 3 cuties name & store them in list
a = str(input("Enter first city name: "))       
b = str(input("Enter second city name: "))       
c = str(input("Enter third city name: ")) 

cityList = [a,b,c]
print(cityList)      

#direct method
cityList.append(input("Enter fourth city name: "))
print(cityList) 
