
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
        for letter in plainText:
            output += modularAdding(letter, key)
        return output

    @staticmethod
    def decrypt(cypherText, key):
        output = ""
        for letter in cypherText:
            output += modularAdding(letter, -key)
        return output

class Vizhener(Cypher):

    @staticmethod
    def encrypt(plainText, key):
        output = ""
        i = 0
        for letter in plainText:
            # finfing index from key
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
