def Add(*p):
    s=[]
    r=0
    for i in p:
        s.append(i)
        r=r+i
    print("Entered Values:",s)
    print("Operation: Addition")
    print("Result: Sum of",s,"is",r)

def Sub(a,b):
    print("Entered Values:",a,',',b)
    print("Operation: Subtraction")
    print("Result: difference of",a,"and",b,"is",a-b)

def Mul(*m):
    s1=[]
    r1=1
    for j in m:
        s1.append(j)
        r1=r1*j
    print("Entered Values:",s1)
    print("Operation: Addition")
    print("Result: multification of",s1,"is",r1)

def Sqr(e):
    print("Entered Values:",e)
    print("Operation: Square")
    print("Result: square of",e,"is",e**2)

def Cub(f):
    print("Entered Values:",f)
    print("Operation: Cube")
    print("Result: cube of",f,"is",f**3)

def UndRoot(g):
    print("Entered Values:",g)
    print("Operation: Under root")
    print("Result: under root of",g,"is",g**0.5)

def Exp(no,po):
    print("Entered Values:",no,po)
    print("Operation: Exponentiation(Power)")
    print("Result: ",no,"to the power",po,"is",no**po)

def Div(c,d):
    print("Entered Values:",c,',',d)
    print("Operation: Division")
    if d==0:
        print("Division By 0")
    else:
        print("Result: division of",c,"and",d,"is",c/d)

def FlrDiv(c1,d1):
    print("Entered Values:",c1,',',d1)
    print("Operation: Floor Division")
    print("Result: floor division of",c1,"and",d1,"is",c1//d1)

def Mod(c2,d2):
    print("Entered Values:",c2,',',d2)
    print("Operation: Modulus(remainder)")
    print("Result:",c2," modulus",d2,"is",c2%d2)
