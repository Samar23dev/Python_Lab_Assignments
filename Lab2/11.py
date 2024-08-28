s=input("Enter string : ")
word,digit,up,low=1,0,0,0
for ch in s:
    if ch.isdigit():
        digit+=1
    if ch==" ":
        word+=1
    if ch.islower():
        low+=1
    if ch.isupper():
        up+=1
print("This sentence has ",word," words")
print("This sentence has ",digit," digits")
print("This sentence has ",up," uppercase")
print("This sentence has ",low," lowercase")