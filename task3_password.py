#simple password jenerator

import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "~!@#$%^&*(_+-*)"
all = lower + upper + numbers + symbols
len_password = int(input("enter your password length :"))
password = "".join(random.sample(all,len_password))

print(password)