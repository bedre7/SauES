from SauES import *

if __name__ == '__main__':
    key = input()
    operation, text = input().split()

    sauES = SauES(key)
    if operation == 'Encrypt':
        print(sauES.encrypt(text))
    elif operation == 'Decrypt':
        print(sauES.decrypt(text))