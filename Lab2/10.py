num=int(input("Enter a number:"))
reversenum=0
n=num
Dict={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,0:0}
while n>0:
    t=n%10
    Dict[t]+=1
    reversenum=(reversenum*10)+t
    n=n//10

if num==reversenum :
    print(num,"is palindrome")
else :
    print(num,"is not a palindrome")

for key in Dict.keys():
    if (Dict[key]!=0):
        print(key,"appears : ",Dict[key],"times")