from SauES import *
from time import time

if __name__ == '__main__':
    print("Enter key: ", end="")
    key = input()
    print("Enter operation (Encrypt/Decrypt): ", end="")
    operation = input()
    print("Enter text: ", end="")
    text = input()

    sauES = SauES(key)
    if operation.lower() == 'encrypt':
        # record the time before encryption
        start_time = time()
        print("Encrypted text: ", sauES.encrypt(text))
        # record the time after encryption
        end_time = time()
        # print the time taken to encrypt in milliseconds
        print(f'Encoded in {round((end_time - start_time) * 1000, 2)}ms') 
    elif operation.lower() == 'decrypt':
        start_time = time()
        print("Decrypted text: ", sauES.decrypt(text))
        end_time = time()
        print(f'Decoded in {round((end_time - start_time) * 1000, 2)}ms')