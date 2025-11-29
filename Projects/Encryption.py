import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")

#ENCRYPT
plain_text = input("Enter a text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original text: {plain_text}")
print(f"encrypted text: {cipher_text}")

#DECRYPT
cipher_text = input("Enter a text to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"original text: {cipher_text}")
print(f"encrypted text: {plain_text}")
