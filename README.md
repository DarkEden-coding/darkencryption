## Introduction
This code implements a simple encryption/decryption mechanism to secure messages using the cryptography library in Python.

### Features
```
- PBKDF2 key derivation is used to derive a secret key from a given password and salt
- The message is encrypted using the Fernet module from the cryptography library
- The encryption process uses a random 16-byte salt, a user-specified number of iterations for the key derivation function, and the derived key to encrypt the message.
- The encrypted message is returned as a base64 encoded string
- The decryption process takes the encrypted message, password and decodes the encrypted message to retrieve the salt, iteration count and encrypted token
- The secret key is derived again using the password and salt, and the encrypted message is decrypted using Fernet
- The decrypted message is returned as a string
```
### Requirements
```
- Python 3.x
- cryptography library
```
### Usage
The code provides two main functions:  
message_encrypt(message, password, iterations=100_000) and message_decrypt(token, password).

message_encrypt takes in the following arguments:

```
message: The message to be encrypted, as a string
password: The password used to derive the secret key, as a string
iterations: The number of iterations for the key derivation function. The default value is 100,000.
```
message_decrypt takes in the following arguments:

```
token: The encrypted message, as a string
password: The password used to derive the secret key and decrypt the message, as a string
The code returns the encrypted message or the decrypted message as a string.
```

### Limitations
The encryption mechanism is only secure if the password is strong and kept confidential.
