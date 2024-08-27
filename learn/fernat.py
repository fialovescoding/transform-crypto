# REF :https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/  
from cryptography.fernet import Fernet   
key = Fernet.generate_key()  
f = Fernet(key)  
token = f.encrypt(b"welcome to geeksforgeeks") 
print(token)  
d = f.decrypt(token)  
print(d.decode()) 