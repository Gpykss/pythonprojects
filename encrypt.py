import random
import string
from operator import index

chars = string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

print(chars)
print(keys)


#encrypt
plain_text = input("Enter  message: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]
print(cipher_text)


#decypt
cipher_text_ = input("Enter  message: ")
plain_text1  = ""

for letter in cipher_text_:
    index = keys.index(letter)
    plain_text1 += chars[index]
print(plain_text1)