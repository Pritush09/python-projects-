import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
# creating the set of the encrypted letter from which we will use the letters of the given message

chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(chars)
print(key)

# ENCRYPT

plain_text = input(" Enter a message : ")
cipher 