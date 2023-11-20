# Secure File Transfer via AES-RSA Encryption over Tor
This project combines the security of AES and RSA encryption with the anonymity benefits of Tor to create a robust and efficient method for securely sharing files.

## Overview
The project provides a PyQt5-based graphical user interface (GUI) for seamless file handling, encryption, decryption, and transmission and reception over the Tor network.


## Features

- **AES Encryption in CBC Mode:** Utilizes the Fernet class from the cryptography.fernet module for AES encryption in Cipher Block Chaining (CBC) mode.
- **Dynamic AES Key Generation:** Generates a dynamic AES key for each file to enhance security.
- **RSA Encryption:** Utilizes the Crypto.PublicKey module for RSA encryption to securely transmit the AES key using the recipient's public key.
- **Tor Integration:** Sends encrypted files over the Tor network, generating recipient-accessible Tor URLs for encrypted file retrieval.
- **Sender Options:**
  1. **Send Files on Tor and Generate Link:** Allows the sender to share files on the Tor network and generate a unique link for secure file access.
  2. **Send Files on Receiver's Link in Tor:** Enables the sender to send files directly to the recipient's Tor link for secure sharing.
- **Receiver Options:**
  1. **Generate Link and Send to Sender:** The receiver can generate a Tor link, send it to the sender, and receive files securely on Tor.
  2. **Receive Files on Sender's Link in Tor:** The receiver can receive files directly on the sender's Tor link for secure file retrieval.


## Usage
1. Run the application using `main.py`.
2. Use the GUI to select files, enter public/private keys, encrypt, and choose sender/receiver options for Tor file sharing.
3. Recipients can utilize the private key sent by the sender to access Tor URLs and decrypt the received files.


## Detailed Steps

### Scenario 1: Send Files on Tor and Generate Link

**Step 1:** Browse the file to be encrypted and provide the recipient's public key.

**Step 2:** Apply AES encryption to the browsed file using a randomly generated key.

**Step 3:** Obtain the key and the encrypted file from AES encryption.

**Step 4:** Encrypt the key generated from AES using RSA with the recipient's public key.

**Step 5:** Now, we have encrypted data and an encrypted key.

**Step 6:** Generate a Tor URL for file (encrypted file) sharing on any system with a Tor environment.

**Step 7:** Share the generated Tor link and the private key with the recipient for secure access to the encrypted files.

**Step 8:** The recipient can use the Tor link and the private key sent by the sender to securely download and decrypt the files using their private key on the Tor browser.

**Step 9:** The recipient now has the decrypted file without any security breaches.


### Scenario 2: Send Files on Receiver's Link in Tor

**Step 1:** Browse the file to be encrypted and provide the recipient's public key.

**Step 2:** Apply AES encryption to the browsed file using a randomly generated key.

**Step 3:** Obtain the key and the encrypted file from AES encryption.

**Step 4:** Encrypt the key generated from AES using RSA with the recipient's public key.

**Step 5:** Now, we have encrypted data and an encrypted key.

**Step 6:** The recipient provides the sender with a Tor link and the private key to access the Tor link.

**Step 7:** The sender uses the provided Tor link and the private key to securely upload the encrypted files.

**Step 7:** The sender uses the provided Tor link and the private key to securely upload the encrypted files.

**Step 8:** The recipient receives the uploaded files from the sender on their system at the specified path, which was set when generating the reception Tor link. Subsequently, the recipient decrypts the files using their private key.

**Step 9:** The recipient now has the decrypted file without any security breaches.


## Dependencies
- PyQt5
- cryptography
- Crypto

- ## Setup

1. Install dependencies: `pip install PyQt5 cryptography pycryptodome`
2. Run the application: `python main.py`

## Found a Bug or Want to Contribute?

If you've encountered an issue or have a suggestion for improvement, your feedback is always welcome. Feel free to [open an issue](https://github.com/pratikmpp22/AES-Encrypted-File-Transfer-over-Tor/issues
) on our GitHub repository.

## Show Your Support

If you find this project useful or appreciate the work done, consider leaving a star on our GitHub repository. Your support motivates me to continue improving and maintaining the project.


