
from abc import ABC, abstractmethod

# get index of a symbol and return index for modular math and difference value
def indexCheck(index):
    diff = 0
    lowLetterFirst = 97
    lowLetterLast = 122
    upLetterFirst = 65
    upLetterLast = 90
    if index >= lowLetterFirst and index <= lowLetterLast:
        index -= lowLetterFirst
        diff = lowLetterFirst
    elif index >= upLetterFirst and index <= upLetterLast:
        index -= upLetterFirst
        diff = upLetterFirst
    else:
        return False

    return { "modular" : index, "asci" : diff}

# change ASCII index to new one using key
def modularAdding(letter, key, module = 26):

    index = indexCheck(ord(letter))
    if index:
        letter = chr(((index["modular"] + key) % module)+index["asci"])

    return letter

#func a 0-255 num to 8-bit string
def toBit(num):
    if num < 0:
        print("You cant convert negative value to binary")
        return False
    bitValue = 1
    bits = ""
    while True:
        if num > bitValue:
            bitValue *= 2
        else:
            if bitValue >= 2 and bitValue != num:
                bitValue /= 2
            break

    while True:
        if bitValue < 1:
            break
        if num >= bitValue:
            bits += "1"
            num -= bitValue
        else:
            bits += "0"
        bitValue /= 2

    return bits

def fromBit(bits):
    index = len(bits) - 1
    result = 0
    for i in range(len(bits)):
        if (int(bits[index - i]) == 1):
            result += 2**i

    return result

def addEmptyBit(bits, length = 8):
    result = ""
    if len(bits) < length:
        for i in range(length - len(bits)):
            result += "0"
    return result + bits

def permutation(bits, pattern):

    result = ""
    if pattern.find(",") > 0:
        pattern = pattern.split(",")
    if bits.find(",") > 0:
        bits = bits.split(",")
    for i in range(len(pattern)):
        result += bits[int(pattern[i])-1]

    return result

def splitInTwo(bits):
    if len(bits) % 2 == 1:
        print("The bit number should be even")
        return False
    return {"left" : bits[:int(len(bits)/2)], "right" : bits[int(len(bits)/2):]}

def shift(bits, value):
    result = ""
    for i in range(len(bits)):
        result += bits[(i+value) % len(bits)]

    return result

def xor(a,b):
    if a < 0 or a > 1 or b < 0 or b > 1:
        print("Input values for XOR are not 0 or 1")
        return False

    return (a+b) % 2

def xorLines(lineA, lineB):
    result = ""
    if len(lineA) == len(lineB):
        for i in range(len(lineA)):
            result += str(xor(int(lineA[i]), int(lineB[i])))
        return result
    print("Function XOR (xorLines) need to take equal length strings")
    return False

    # s1 = "1123,2013,3010,2103"
def substitutionBox(table, value):
    table = table.split(",")
    if len(value) != 4:
        print("The finding input shout be a 4 bit number")
        return False
    row = fromBit(value[0]+value[3])
    column = fromBit(value[1]+value[2])

    result = toBit(int(table[row][column]))
    result = addEmptyBit(result, 2)

    return result


class Cypher():

    @abstractmethod
    def encrypt(plainText):
        pass

    @abstractmethod
    def decrypt(cypherText):
        pass


class Caesar(Cypher):

    @staticmethod
    def encrypt(plainText, key):
        output = ""
        if isinstance(key, int):
            k = key
        else:
            k = indexCheck(ord(key))["modular"]
        for letter in plainText:
            output += modularAdding(letter, k)
        return output

    @staticmethod
    def decrypt(cypherText, key):
        output = ""
        if isinstance(key, int):
            k = key
        else:
            k = indexCheck(ord(key))["modular"]
        for letter in cypherText:
            output += modularAdding(letter, -k)
        return output

class Vizhener(Cypher):

    @staticmethod
    def encrypt(plainText, key):
        output = ""
        i = 0
        for letter in plainText:
            # finfing index for letter in key
            k = indexCheck(ord(key[i % len(key)]))["modular"]
            if indexCheck(ord(letter)):
                i += 1
            output += modularAdding(letter, k)
        return output

    @staticmethod
    def decrypt(cypherText, key):
        output = ""
        i = 0
        for letter in cypherText:
            # finfing index from key
            k = indexCheck(ord(key[i % len(key)]))["modular"]
            if indexCheck(ord(letter)):
                i += 1
            output += modularAdding(letter, -k)
        return output

class DES(Cypher):

    # keys
    initialPermutation = "2,6,3,1,4,8,5,7"
    finalPermutation = "4,1,3,5,7,2,8,6"
    permutationTen = "3,5,2,7,4,10,1,9,8,6"
    permutationEight = "6,3,7,4,8,5,10,9"
    expansionPermutation = "4,1,2,3,2,3,4,1"
    permutationFour = "2,4,3,1"
    s_zero= "1032,3210,0213,3131"
    s_one = "1123,2013,3010,2103"

    @staticmethod
    def generateKeys(key, rounds = 1):
        keys = []
        key = permutation(key, DES.permutationTen)
        parts = splitInTwo(key)
        for i in range(1, rounds+1):
            left = shift(parts["left"], i)
            right = shift(parts["right"], i)
            key = left + right
            # parts["left"] = shift(parts["left"], i)
            # parts["right"] = shift(parts["right"], i)
            # key = parts["left"] + parts["right"]
            keys.append( permutation(key, DES.permutationEight) )
        return keys

    @staticmethod
    def cryptFunc(bits, key):
        splitedInitPerm = splitInTwo(bits)

        rightInitPerm = permutation(splitedInitPerm["right"], DES.expansionPermutation)
        xorWithKey = splitInTwo(xorLines(rightInitPerm, key))
        sBoxResult = substitutionBox(DES.s_zero, xorWithKey["left"]) + substitutionBox(DES.s_one, xorWithKey["right"])
        sBoxResult = permutation(sBoxResult, DES.permutationFour)

        splitedInitPerm["left"] = xorLines(splitedInitPerm["left"], sBoxResult)
        result = splitedInitPerm["right"] + splitedInitPerm["left"]

        return result


    @staticmethod
    def encrypt(bits, keys):
        bits = permutation(bits, DES.initialPermutation)

        for i in range(len(keys)):
            bits = DES.cryptFunc(bits, keys[i])
            print(bits + " as result of " + str(i+1) + " interation, key - " + keys[i] )

        result = shift(bits, int(len(bits)/2))

        result = permutation(result, DES.finalPermutation)
        print(result + " result of last encryption iteration" )

        return result


    @staticmethod
    def decrypt(bits, keys):
        bits = permutation(bits, DES.initialPermutation)

        for i in reversed(range(len(keys))):
            bits = DES.cryptFunc(bits, keys[i])
            print(bits + " as result of " + str(len(keys) - i) + " interation, key - " + keys[i] )

        result = shift(bits, int(len(bits)/2))

        result = permutation(result, DES.finalPermutation)
        print(result + " result of last decryption iteration" )

        return result


#Full DES cycle
key = "1101100100"
text = "11100010"
rounds = 200
keys = DES.generateKeys(key,rounds)
print("keys" + str(keys))

x = DES.encrypt(text, keys)
y = DES.decrypt(x, keys)
