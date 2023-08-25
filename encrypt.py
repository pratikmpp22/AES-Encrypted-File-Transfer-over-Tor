from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.fernet import Fernet
import os


def rsa_encrypt(data: bytes, public_key: bytes) -> bytes:
    key = serialization.load_pem_public_key(public_key)
    ciphertext = key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return ciphertext

def save_aes_key(aes_key, rsa_public_key):
    encrypted_aes_key = rsa_encrypt(aes_key, rsa_public_key)

    with open("secret.txt", "wb") as file:
        file.write(encrypted_aes_key)

def generate_aes_key() -> bytes:
    return Fernet.generate_key()

def encrypt_file_with_aes(input_filename, aes_key):
    with open(input_filename, "rb") as file:
        file_data = file.read()
        cipher_suite = Fernet(aes_key)
        encrypted_data = cipher_suite.encrypt(file_data)

    with open(input_filename, "wb") as file:
        file.write(encrypted_data)

def encrypt(public_key: bytes, file_path: str) -> str:
    try:
        with open(file_path, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        return "File does not exist"

    key = generate_aes_key() 

    enc_data = encrypt_file_with_aes(file_path, key)
    save_aes_key(key, public_key)

    return "Encrypted Successfully"
