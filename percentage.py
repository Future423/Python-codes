n=int(input("Enter number of subjects:" ))
m=int(input("Enter maximum marks: "))
if m<=0:
            print("INVALID INPUT")
            m=int(input("please enter valid maximum marks: "))
t=0
m=m*n
for i in range (n):
            print("Enter marks of ",i+1," subject")
            a=int(input())
            t=a+t
per=(t/m)*100
print("Percentage gain is: ",per)                       
            
