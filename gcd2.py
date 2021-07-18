a=int(input("enter the number:"))
b=int(input("enter the number:"))
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
GCD=gcd(a,b)
print("GCD is:")
print(GCD)
