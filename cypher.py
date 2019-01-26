
from abc import ABC, abstractmethod

class Cypher():

    # def __init__(self, value):
    #     self.value = value
    #     super().__init__()

    @abstractmethod
    def makeCypherText(plainText):
        pass

    @abstractmethod
    def makePlainText(cypherText):
        pass


class Ceaser(Cypher):

    @staticmethod
    def makeCypherText(plainText):
        pass

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
