import string
import random

choice = string.ascii_letters + string.digits + string.punctuation

passwordList = random.sample(choice, 10)

password = "".join(passwordList)

print(password)