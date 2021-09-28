from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os
import Privkey
list = os.listdir(path='.')
list.remove("KeyGen.py")
list.remove("Decrypt.py")
list.remove("Privkey.py")

Privkey.private()

# Decrypt file
for x in list:
    original_message = Privkey.private_key.decrypt(
            x,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

# Checking the results
# newFile1 = open("newtext.txt", "wb")
# newFile1.write(original_message)

# Make new text1.txt file
# newFile1 = open("text1.txt", "w")
# newFile1.write("here")
