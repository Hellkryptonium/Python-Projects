import random
import string

pass_len = int(input("enter your password length : "))
charValues = string.ascii_letters + string.digits + string.punctuation

#list comprehension

result = "".join([random.choice(charValues) for i in range(pass_len)])

print(result)



password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("your random password is:", password)