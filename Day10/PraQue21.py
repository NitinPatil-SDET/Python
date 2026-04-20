#WAF to find the factorial of n.(n is the parameter)

def print_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i   
    print("The factorial is: ",fact)

print_fact(5)

#WAF to convert USD to INR (Current rate) 1 USD = 93 INR
 
def usd_to_inr(usd_val):
    inr_val = usd_val*93  
    print(usd_val, "USD =", inr_val, "INR") 

usd_to_inr(12)

#WAF to check EVEN & ODD 

def check_evn_odd(n):
    if(n%2==0):
        print("The given number is EVEN: ",n)
    elif(n%2!=0):
        print("The given number is ODD: ",n)
    else:
        print("Invalid Input")

check_evn_odd(6)
check_evn_odd(11)
