n=int(input("enter any number:"))
m=n
f=0
while n>0 :
    c=n%10
    f=f+(c*c*c)
    n=n//10
if f==m:
    print("it is Armstrom number")
else:
    print("it is not Armstrom number")