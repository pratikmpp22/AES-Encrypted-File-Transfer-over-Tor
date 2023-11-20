# Secure File Transfer via AES-RSA Encryption over Tor

This project combines the security of AES and RSA encryption with the anonymity benefits of Tor to create a robust and efficient method for securely sharing files.

## Overview

The project provides a PyQt5-based graphical user interface (GUI) for seamless file handling, encryption, decryption, and transmission and reception over the Tor network.

## Features

- **AES Encryption in CBC Mode:** Utilizes the Fernet class from the cryptography.fernet module for AES encryption in Cipher Block Chaining (CBC) mode.

- **Dynamic AES Key Generation:** Generates a dynamic AES key for each file to enhance security.

- **RSA Encryption:** Utilizes the Crypto.PublicKey module for RSA encryption to securely transmit the AES key using the recipient's public key.

- **Tor Integration:** Sends encrypted files over the Tor network, generating recipient-accessible Tor URLs for encrypted file retrieval.
