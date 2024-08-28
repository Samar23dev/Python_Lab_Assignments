import math
def iscollide(a,b):
    dis=math.sqrt(pow(a[1]-b[1],2)+pow(a[0]-b[0],2))
    rad_sum=a[2]+b[2]
    if(dis<=rad_sum):
        return True
    else:
        return False

a=(0,0,2)
b=(2,0,2)
print("A : ",a,"\nB : ",b)
if (iscollide(a,b)):
    print("A and B are colliding")
else:
    print("A and B are not collding")