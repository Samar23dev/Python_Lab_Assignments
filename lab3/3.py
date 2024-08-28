def gcd(a,b):
     if (b==0):
          return a
     return gcd(b,a%b)

def lcm(x,y):
     gc=gcd(a,b)
     return (a*b)/gc
     
     

a=int(input("Enter value of a : "))
b=int(input("Enter value of b : "))
print("Gcd of a and b : ",gcd(a,b))
print("Gcd of a and b : ",lcm(a,b))