from string import ascii_uppercase, ascii_lowercase, digits
import secrets
import random
'''
Creates a strong password of 8 characters
At least one character of each type
'''
# create ordered alphabet of 3 types
A = [ascii_uppercase, ascii_lowercase, digits]
# At least one of each type
p = [1,1,1]

# Choose frequency of types
for i in range(5):
    p[secrets.choice([0,1,2])] += 1

# begin with empty list
password = []
# add characters to password
for x in range(3):
    for y in range(p[x]):
        # add p[x] many of A[x] type
        password.append(secrets.choice(A[x]))
# shuffle list
random.shuffle(password)
# print password as a string
print("".join(password))
