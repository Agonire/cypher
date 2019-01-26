
from abc import ABC, abstractmethod

class Cypher():

    @abstractmethod
    def makeCypherText(plainText):
        pass

    @abstractmethod
    def makePlainText(cypherText):
        pass


class Ceaser(Cypher):

    @staticmethod
    def makeCypherText(plainText, key):
        temp = 0
        output = ""
        for letter in plainText:
            letterIndex = ord(letter)
            if letterIndex >= 97 and letterIndex <= 122:
                letterIndex -= 97
                temp = 97
            elif letterIndex >= 65 and letterIndex <= 90:
                letterIndex -= 65
                temp = 65
            else:
                output += letter
                continue
            letterIndex += key
            letterIndex = (letterIndex%26)+temp
            letter = chr(letterIndex)
            output += letter
        return output

    @staticmethod
    def makePlainText(cypherText):
        pass


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
