from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os

# Create list of files in directory to encrypt
list = os.listdir(path='.')
list.remove("Key_Encrypt.py")
list.remove("Decrypt_key.py")

# Generate public and private keys
priv_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
pub_key = priv_key.public_key()

# Sterilize private key
key = priv_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
# Store private key in seperate file
privkey = open('priv_key.pem', 'wb')
privkey.write(key)

# Sterilize private key
key = pub_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
# Store private key in seperate file
pubkey = open('pub_key.pem', 'wb')
pubkey.write(key)
# Clear key varible
key = ""

# Loop through all files in directory and encrypt
for x in list:
    # Open x file
    file = open(x, "rb")
    # Encrypt x file
    encrypt = pub_key.encrypt(
        file.read(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Close x file and clear file varible
    file.close()
    file = ""

    # Delete original x file
    os.remove(x)
    # Make new encrypted file and write to it
    filename = str(x + ".enc")
    encryptedFile = open(filename, "wb")
    encryptedFile.write(encrypt)
    # Close encyrpted file and clear encryptedfile varible
    encryptedFile.close()
    encryptedFile = ""