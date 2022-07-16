#Finding the files
import os
from cryptography.fernet import Fernet

files =[]
for file in os.listdir():
        if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py" or file == "a1" or file == "d1" or file == "r1":
                continue
        if os.path.isfile(file):    
                 files.append(file)   
print(files)   

with open("thekey.key", "rb") as key:
         secretkey = key.read()

secretphrase = "delete"         
userphrase = input("Enter The Secret Phrase To Decrypt:\n")

if userphrase == secretphrase:
     for file in files:
            with open(file, "rb") as thefile:
                     contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open (file, "wb") as thefile:
                     thefile.write(contents_decrypted)