def isDivisibleByChunkSize(length, chunk_size):
    #returns True if the length of the bitstring is dividisible by the chunksize
    if ((length % chunk_size) == 0):
        return True
    else:
        return False

def packToChunks(bit_string, n):
    #returns chunks after grouping the bitstring to n
    chunks = []
    if(isDivisibleByChunkSize(len(bit_string), n)):
        chunks = [bit_string[i:i+n] for i in range(0, len(bit_string), n)]
    else:
        newBitString = bit_string + '00000000'
        packToChunks(newBitString, n)
    return chunks
        
def convertToBinary(text, symbol_space):
    #returns converted text after converting text to binary
    convertedText = ""
    for symbol in text:
        if symbol in symbol_space:
            index = symbol_space.index(symbol)
            convertedChar = f'{index:08b}'
            convertedText += convertedChar
        else:
            print(symbol," is not in our symbol space.")
    return convertedText

def encryptMsg(msg_to_encrypt, S, n, public_key, symbol_space):
    #returns encrypted message
    chunks = []
    bitString = convertToBinary(msg_to_encrypt, symbol_space)
    chunks = packToChunks(bitString, n)
    string = ''

    for index in chunks:
        total = 0
        A = list(index)
        j = 0
        for i in A:
            if i == '1':
                total += int(i) * public_key[j]
            j += 1
        string += str(total) + ' '
    return string
