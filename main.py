from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os

# Generating a key
private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
public_key = private_key.public_key()

# Storing the keys
key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
privkey = open('private_key.pem', 'wb')
privkey.write(key)

key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
pubkey = open('public_key.pem', 'wb')
pubkey.write(key)
key = ""

# Encrypting
file = open("text1.txt", "rb")
encrypt = public_key.encrypt(
        file.read(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
file.close()
file = ""

# Delete Originals and make new encrypted file
os.remove("text1.txt")
encryptedFile = open("text1.txt.enc", "wb")
encryptedFile.write(encrypt)
encryptedFile.close()
encryptedFile = ""

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
