def findModInverse(a, b):
    a = a % b; 
    for x in range(1, b) :
        if ((a * x) % b == 1) : 
            return x
    return 1

def findSuperIncreasingSet(a_inv, public_key, a):
    #returns the super increasing sequence computed from the inverse of a and public key
    super_increasing_set = []
    for key in public_key:
        i = (a_inv * key) % a
        super_increasing_set.append(i)
    return super_increasing_set

def findBitStringChunks(a_inv, ciphertext, super_increasing_set, b):
    #returns the chunks generated from the a_inv, ciphertext, super increasing set and 
    chunks = []
    splitted_ciphertext = ciphertext.strip().split(' ')
    for key in splitted_ciphertext:
        val = (int(key) * a_inv) % b
        i = 3
        chunk = ''
        while (i > -1):
            if val >= super_increasing_set[i]:
                chunk = chunk + '1'
                val -= super_increasing_set[i]
            else:
                chunk = chunk + '0'
            i -= 1
        chunks.append(chunk[::-1])
    return chunks

def mergeChunks(chunks, no_of_bits):
    #returns the bitstring
    bitstring = []
    block = ''
    for key in chunks:
        block += key
        if(len(block) == no_of_bits):
            bitstring.append(block)
            block = ''
    return bitstring

def convertToInt(bitstring):
    #converts the bitstring to integer and returns a list of it
    int_bitstring = []
    for key in bitstring:
        convertedBitString = int(key, 2)
        int_bitstring.append(convertedBitString)
    return int_bitstring

def convertToPlaintext(int_bitstring, symbol_space):
    #returns the plaintext retrieved from the symbol space
    plaintext = ''
    for index in int_bitstring:
        plaintext += symbol_space[index]
    return plaintext

def decryptMsg(ciphertext, a, b, public_key, symbol_space):
    a_inv = findModInverse(a, b)
    super_increasing_set = findSuperIncreasingSet(a_inv, public_key, a)
    chunks = findBitStringChunks(a_inv, ciphertext, super_increasing_set, a)
    bitstring = mergeChunks(chunks, 8)
    int_bitstring = convertToInt(bitstring)
    plaintext = convertToPlaintext(int_bitstring, symbol_space)
    return (plaintext)
