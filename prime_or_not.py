a=int(input("Enter any number :"))
f=0
i=2
while(i<=a//2):
    if(a%i==0):
        f=1
        break 
    i+=1
if(f==0):
    print(a,"is prime")
else:
    print(a,"is not prime")