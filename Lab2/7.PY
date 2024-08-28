for i in range(2,21):
    curr=i
    flag=1
    for j in range(2,i-1):
        if curr%j==0:
            flag=0
            break
    if (flag==1):
        print(curr,end=" ")