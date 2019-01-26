
from abc import ABC, abstractmethod

def learn(letter, polus, key):
    temp = 0
    lowLetterFirst = 97
    lowLetterLast = 122
    upLetterFirst = 65
    upLetterLast = 90
    alfphabetLength = 26

    letterIndex = ord(letter)
    if letterIndex >= lowLetterFirst and letterIndex <= lowLetterLast:
        letterIndex -= lowLetterFirst
        temp = lowLetterFirst
    elif letterIndex >= upLetterFirst and letterIndex <= upLetterLast:
        letterIndex -= upLetterFirst
        temp = upLetterFirst
    else:
        return letter
    if polus == True:
        letterIndex += key
    else:
        letterIndex -= key
    letterIndex = (letterIndex % alfphabetLength)+temp
    letter = chr(letterIndex)
    return letter

class Cypher():

    @abstractmethod
    def makeCypherText(plainText):
        pass

    @abstractmethod
    def makePlainText(cypherText):
        pass


class Caesar(Cypher):

    @staticmethod
    def makeCypherText(plainText, key):
        output = ""
        for letter in plainText:
            lette = learn(letter, True, key)
            output += lette
        return output

    @staticmethod
    def makePlainText(cypherText, key):
        output = ""
        for letter in cypherText:
            lette = learn(letter, False, key)
            output +=lette
        return output

class Vizhener(Cypher):

    @staticmethod
    def makeCypherText(plainText):
        pass

    @staticmethod
    def makePlainText(cypherText):
        pass


class DES(Cypher):

    @staticmethod
    def makeCypherText(plainText):
        pass

    @staticmethod
    def makePlainText(cypherText):
        pass
