import string
import random

print("".join(random.sample(string.ascii_letters+string.digits+string.punctuation, 10)))