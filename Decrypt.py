from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os

# Decrypt file
original_message = private_key.decrypt(
        encrypt,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# Checking the results
newFile1 = open("newtext.txt", "wb")
newFile1.write(original_message)

# Make new text1.txt file
newFile1 = open("text1.txt", "w")
newFile1.write("here")