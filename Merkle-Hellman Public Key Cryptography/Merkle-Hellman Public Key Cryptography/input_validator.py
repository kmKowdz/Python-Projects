def isSuperIncreasing(a, S):
#returns True if the input satisfies the  super increasing sequence property,
#otherwise, False if the input is not valid
    if(sum(S) < a):
        return True
    else:
        total = str(sum(S))
        print("The elements of A are " + str(S) + ". Sum is: " + total)

        if(int(total) == a):
            print(total + " = " + str(a))
        else:
            print(total + " > " + str(a))

        print("So it's not a valid input.")
        print("Hint: Select a value greater than " + total )
        return False

def getSuperIncreasingSequence(n):
    #prompt for taking an input for A
    S = []
    print("FOR SUPER-INCREASING SEQUENCE:")
    while len(S) < n:
        user_input = input('Please assign a value for key [a' + str(len(S) + 1) + ']: ')
        if(user_input != ""):
            if(user_input.isdigit()):
                a = int(user_input)
                if(isSuperIncreasing(a, S)):
                    S.append(a)
                    print(str(S))            
            else:
                print(user_input + " is not an integer.")
        else:
            print("You entered an empty input.")
    return S

def isValidA(a, S):
    #returns True if the input is a valid M, otherwise, False if the input is invalid
    if(a < max(S)):
        print(str(a) + " < " + str(max(S)))
        print("Invalid Input.")
        print("Hint: Enter a value greater than " + str(max(S)))
        return False
    elif(a == max(S)):
        print(str(a) + " = " + str(max(S)))
        print("Invalid Input.")
        print("Hint: Enter a value greater than " + str(max(S)))
        return False
    else:
        return True

def getValueForA(S):
    #prompt for taking an input for a
    print("\nFOR A:")
    while True:
        user_input = input('Please assign a value for key a: ')
        if(user_input != ""):
            if(user_input.isdigit()):
                if(isValidA(int(user_input), S)):
                    a = int(user_input)
                    print("S :", S)
                    print("a :", a)
                    break
            else:
                print(user_input + " is not an integer.")
        else:
            print("You entered an empty input.")
    return a


def calcGCD(a, b):
    #returns the GCD of two numbers
    if b == 0:
        return a
    else:
        return calcGCD(b, a % b)

def isRelPrime(a, b):
    #returns true if the given value is relatively prime to a
    #otherwise, false
    result = calcGCD(a, b)
    if result == 1:
        return True
    else:
        print(str(a) + " and " + str(b) + " are not relatively prime.")
        return False

def getValueForB(S, a):
    #prompt for taking an input for co-prime of a
    print("\nFOR B:")
    while True:
        user_input = input('Please assign a value for b: ')
        if(user_input != ""):
            if(user_input.isdigit()):
                if(isRelPrime(a, int(user_input))):
                    b = int(user_input)
                    print("S :", S)
                    print("a :", a)
                    print("b :", b)
                    break
            else:
                print(user_input + " is not an integer.")
        else:
            print("You entered an empty input.")
    return b
    
def generatePublicKey(S, a, b):
    #returns a public key generated from the 3 inputs 
    A = []
    for s in S:
        result = (s*b) % a
        A.append(result)
    print("Your PUBLIC KEY is:", A)
    return A
