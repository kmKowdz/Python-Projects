"""
Assignment #3: Merkle-Hellman Cryptography
Student ID: 201690653
Student Name: Alarcon, Karen Michelle
Submitted on: 10/19/2018

References:
[1] https://www.datacamp.com/community/tutorials/python-data-type-conversion
[2] https://pynative.com/python-check-user-input-is-number-or-string/
[3] https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python
[4] https://pythonadventures.wordpress.com/2016/12/16/split-a-string-into-equal-length-substrings/
[5] https://stackoverflow.com/questions/7522533/how-can-i-turn-a-string-into-a-list-in-python
[6] https://www.mantidproject.org/Working_With_Functions:_Return_Values
"""

from input_validator import *
from encryption import *
from decryption import *

symbol_space = """ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}[]\|:;"'<,>./?1234567890`~!@#$%^&*()-_=+"""
n,a,b,public_key,S = 4,0,0,[],[]

def getUserInput():
    global n,a,b,public_key,S

    print('========SETUP========')
    S = getSuperIncreasingSequence(n)
    a = getValueForA(S)
    b = getValueForB(S,a)
    public_key = generatePublicKey(S,a,b)
    print('=====================')

    while True:
        task = input('\nPlease type in [E] for Encryption, [D] for Decryption or [Q] to Quit: ')
        if task.upper() == 'E':
            print('========ENCRYPTION========')
            msg = input('Enter the message to encrypt: ')
            ciphertext = encryptMsg(msg,S,n,public_key,symbol_space)
            print('ENCRYPTED MESSAGE:',ciphertext)
            print('==========================')
        elif task.upper() == 'D':
            print('========DECRYPTION=======')
            ciphertext = input('Enter the message to decrypt: ')
            plaintext = decryptMsg(ciphertext,a,b,public_key,symbol_space)
            print('DECRYPTED MESSAGE:',plaintext)
            print('=========================')
        elif task.upper() == 'Q':
            print('Exiting Application... \nThank you! :)')
            break
        else:
            print('Invalid Input.')

def main():
    getUserInput()
    
if __name__ == '__main__':
    main()
