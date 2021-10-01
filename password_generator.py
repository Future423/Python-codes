import random
password_length = int(input("Enter the length of password you want to generate"))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(s, password_length))
print(password)
