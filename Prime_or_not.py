#This code take a intiger as input and check the input is a prime number or not 

a=int(input("Enter any number :"))
f=0
i=2
while(i<=a//2):
    if(a%i==0):
        f=1
        break #it break the loop if a is devided my i
    i+=1
    
if(f==0):
    #f=0,it means a is not devided by i
    print(a,"is prime")
    
else:
    #else,f=1,it means it devided by i
    print(a,"is not prime")
