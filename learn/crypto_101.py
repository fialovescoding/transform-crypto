#REF: https://www.youtube.com/watch?v=vsLBErLWBhA

import random
import string

# First we creat a string, chars
chars = " " + string.punctuation + string.digits + string.ascii_letters
print (chars)
# Then we convert it into a list
chars = list(chars)
# We make a variable, key
key = chars.copy()
# Then we randomly shuffle key 
random.shuffle(key)

#ENCRYPT
# We make two variables plain_text and cipher_text
plain_text = input("Enter a message to encrypt : ")
cipher_text = ""
# Now we stat a for loop to encrypt the plain text
for letter in plain_text:
    index = chars.index(letter)
    cipher_text = cipher_text + key[index]
# Then we print the original message and encrypted message
print (f"original message : {plain_text}")
print (f"encrypted message : {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to decrypt : ")
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text = plain_text + chars[index]

print (f"encrypted message : {cipher_text}")
print (f"original message : {plain_text}")
