n=float(input("Enter temperature : "))
str=input("Enter degree C->Celcius and F-> fahrenhiet : ")
if (str=='c' or str=='C'):
    print("Temperature in Celcius : ",n)
    print("Temperature in Fahrenheit : ",((9/5)*n) + 32)
elif(str=='F' or str=='f'):
    print("Temperature in Fahrenheit : ",n)
    print("Temperature in Celcius : ",((n-32)*5)/9)
