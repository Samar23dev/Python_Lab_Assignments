name1=input("Enter name ")
a=input("Enter birthday in dd-mm-yy : ")
b=a.split("-")

name2=input("Enter name ")
x=input("Enter birthday in dd-mm-yy : ")
y=x.split("-")
ram={"Day":b[0],"Month":b[1],"Year":b[2]}
shyam={"Day":y[0],"Month":y[1],"Year":y[2]}


res1=name1+" borns on " + a +" and "+name2+" borns on "+x
print(res1)

print(name1,"turns ",2024-int(ram["Year"])," years on the date",ram["Day"],ram["Month"],2024)
print(name2," turns ",2024-int(shyam["Year"])," years on the date",shyam["Day"],shyam["Month"],2024)
