str=input("Enter string : ")
a=dict()
for ch in str:
    if ch not in a:
        a[ch]=1
    else:
        a[ch]=a[ch]+1
print(a)