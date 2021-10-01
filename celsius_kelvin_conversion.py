def celsius_to_kelvin(degrees):
  return (degrees+273)


def kelvin_to_celsius(degrees):
  return (degrees-273)
n=int(input("enter temperature in celsius: "))
print("temperature in kelvin",celsius_to_kelvin(n))

m=int(input("enter temperature in kelvin: "))
print("temperature in celsius",kelvin_to_celsius(0))

