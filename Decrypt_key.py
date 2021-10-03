from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os

# Make list of encrypted files in directory
list = os.listdir(path='.')
list.remove("Key_Encrypt.py")
list.remove("Decrypt_key.py")
list.remove("priv_key.pem")
list.remove("pub_key.pem")

# Open read priv_key.pem and read private key
with open("priv_key.pem", "rb") as key_file:
    priv_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

# Loop through all files in directory and decrypt
for x in list:
    # Open encrytped x file
    encryptedfile = open(x, "rb")
    # Decrypt x file
    original = priv_key.decrypt(
        encryptedfile.read(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Close encrypted x file
    encryptedfile.close()
    # Find lengeth of orginal file name
    filelen = len(x) - 4
    # Assign filename to varible
    filename = str(x[:filelen])
    # Create new x file and write original contents
    file2 = open(filename, "wb")
    file2.write(original)
