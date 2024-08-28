import statistics
n=int(input("Enter length of list : "))
a=list()
print("Enter list of numbers ")
count=0
for i in range(0,n):
    val=int(input())
    a.insert(i,val)
    count+=val

print("Entered data set: ")
print(a)
print("mean : ",count/5)
print("Median : ",statistics.median(a))
print("Mode : ",statistics.mode(a))
    
