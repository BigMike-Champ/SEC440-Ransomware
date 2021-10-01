from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os

list = os.listdir(path='.')
list.remove("Key_Encrypt.py")
list.remove("Decrypt_key.py")
list.remove("private_key.pem")
list.remove("public_key.pem")
print(list)

with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

for x in list:
    file = open(x, "rb")
    original_message = private_key.decrypt(
        file.read(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    file.close()
    y = len(x) - 4
    filename = str(x[:y])
    file2 = open(filename, "wb")
    file2.write(original_message)

    print(original_message)