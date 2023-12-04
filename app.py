from SauES import *
from time import time

if __name__ == '__main__':
    key = input()
    operation, text = input().split()

    sauES = SauES(key)
    if operation == 'Encrypt':
        # record the time before encryption
        start_time = time()
        print(sauES.encrypt(text))
        # record the time after encryption
        end_time = time()
        # print the time taken to encrypt in milliseconds
        print(f'Encoded in {round((end_time - start_time) * 1000, 2)}ms') 
    elif operation == 'Decrypt':
        start_time = time()
        print(sauES.decrypt(text))
        end_time = time()
        print(f'Decoded in {round((end_time - start_time) * 1000, 2)}ms')