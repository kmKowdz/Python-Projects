"""
Assignment #2: Affine Cryptography
Student ID: 201690653
Student Name: Alarcon, Karen Michelle
Submitted on: 9/24/2018

References:
[1] https://en.wikipedia.org/wiki/Euclidean_algorithm#Procedure
[2] https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
[3] https://inventwithpython.com/hacking/chapter15.html

"""

#m = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
#THIS IS THE SYMBOL SPACE
m = """ abcdefghijklmnopqrstuvwxyz{}[]\|:;"'<,>./?1234567890`~!@#$%^&*()-_=+ABCDEFGHIJKLMNOPQRSTUVWXYZ"""

def calcGCD(a, b):
    #returns the GCD of two numbers
    if b == 0:
        return a
    else:
        return calcGCD(b, a % b)

def findModInverse(a, m):
    #returns the modular multiplicative inverse of a number
    a = a % m;
    for x in range(1, m):
        if ((a * x) % m == 1):
            print
            return x
    return 1

def checkRelPrime(a, b):
    result = calcGCD(a, b)
    if result != 1:
        print('The keys are not relatively prime.')
        return 1
    return None

def encryptMsg(a, b, msg):
    encryptedMsg = ''
    for symbol in msg:
        if symbol in m:
            x = m.index(symbol)
            encryptedMsg += m[(a*x + b) % len(m)]
        else:
            encryptedMsg += symbol
    return encryptedMsg

def decryptMsg(a, b, msg):
    decryptedMsg = ''
    c = findModInverse(a, len(m)) # c is the modulo inverse of a

    for symbol in msg:
        if symbol in m:
            x = m.index(symbol)
            decryptedMsg += m[(c * (x - b)) % len(m)]
        else:
            decryptedMsg += symbol
    return decryptedMsg

def getUserInput():
    while True:
        task = input('Please type [E] for encryption, [D] for decryption or [Q] to quit: ')
        if task.upper() == 'E':
            print('========ENCRYPTION========')
            a = int(input('Please assign a value for key a: '))
            b = int(input('Please assign a value for key b: '))
            if checkRelPrime(a, b) == None:
                msg = input('Enter the message to encrypt: ')
                print('ENCRYPTED MESSAGE: ' + encryptMsg(a, b, msg))
                print('========================')
            else:
                print('Invalid Input. Please select other key combination.')
        elif task.upper() == 'D':
            print('========DECRYPTION=======')
            a = int(input('Please assign a value for key a: '))
            b = int(input('Please assign a value for key b: '))
            if checkRelPrime(a, b) == None:
                msg = input('Enter the message to decrypt: ')
                print('DECRYPTED MESSAGE: ' + decryptMsg(a, b, msg))
                print('========================')
            else:
                print('Invalid Input. Please select other key combination.')
        elif task.upper() == 'Q':
            print('Exiting Application... \nBYE!')
            break
        else:
            print('Invalid Input.')

def main():
    getUserInput()
    
if __name__ == '__main__':
    main()
