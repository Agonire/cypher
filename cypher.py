
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
def modularAdding(letter, key):

    index = indexCheck(ord(letter))
    if index:
        letter = chr(((index["modular"] + key) % 26)+index["asci"])

    return letter

#func a 0-255 num to 8-bit string
def toEightBit(num):
    if num > 255 or num < 0:
        return "Wrong value, out of 8 bit range"
    bitStr = ""
    bitValue = 128
    while True:
        if bitValue < 1:
            break
        if num >= bitValue:
            bitStr += "1"
            num -= bitValue
        else:
            bitStr += "0"
        bitValue /= 2

    return bitStr

def permutation(bits, pattern):
    if len(bits) != len(pattern):
        return "permutation func error: bit strings should be equal"
    result = ""
    for i in range(len(pattern)):
        result += bits[int(pattern[i])-1]

    return result

#IP 2 6 3 1 4 8 5 7
def initialPermutation(bits):
    pattern = "26314857"
    return permutation(bits, pattern)

#commnt
def initialPermutationRev(bits):
    pattern = "41357286"
    return permutation(bits, pattern)



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

    @staticmethod
    def encrypt(plainText):
        pass

    @staticmethod
    def decrypt(cypherText):
        pass
