from Crypto.PublicKey import RSA
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.fernet import Fernet
import os

def rsa_decrypt(data: bytes, private_key: bytes) -> bytes:
    key = serialization.load_pem_private_key(private_key, password=None)
    plaintext = key.decrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return plaintext

def load_aes_key(rsa_private_key, encrypted_aes_key_filename) -> bytes:

    with open(encrypted_aes_key_filename, "rb") as file:
        encrypted_aes_key = file.read()

    decrypted_aes_key = rsa_decrypt(encrypted_aes_key, rsa_private_key)
    return decrypted_aes_key

def decrypt_file_with_aes(input_filename, aes_key):
    with open(input_filename, "rb") as file:
        encrypted_data = file.read()

    cipher_suite = Fernet(aes_key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open(input_filename, "wb") as file:
        file.write(decrypted_data)

def decrypt(priv_key, file_path) -> str:
    try:
        with open(file_path, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        return "File does not exist"

    aes_key = load_aes_key(priv_key, "secret.txt")
    decrypt_file_with_aes(file_path, aes_key)

    return "Decrypted Successfully"
