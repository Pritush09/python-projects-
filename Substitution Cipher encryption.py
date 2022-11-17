import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
# creating the set of the encrypted letter from which we will use the letters of the given message

chars = list(chars)
key = chars.copy() #This for the comparing with the chars so the given charater in char is replaced by the same character in key and vice versa

random.shuffle(key)

print(chars)
print(key)

# ENCRYPT

plain_text = input(" Enter a message : ")
# encrpted text
cipher_text = ""

# we will iterate though all the element in the input string
for letter in plain_text:
    index = chars.index(letter) # index of the character in the input string
    cipher_text += key[index]  # taking that index and replacing with the key one and adding to the encrypted string


print(cipher_text)
plain = ''
encrypted_text = input("Enter the encrypted text : ")
# this for the decryption of the message
for letter in cipher_text:
    index_ = key.index(letter)
    plain += chars[index_]

print(plain)