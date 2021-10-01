def gcd(x, y):
  if x%y == 0:
    return x
  else:
    return gcd(y, x%y) 
  
print(gcd(23, 40)) 
