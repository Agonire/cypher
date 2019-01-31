
import re

# get proper words from raw text - vocabulary.txt to sorted list
# write them into sortedWordList.txt
# make external function that checks if there is a sorted list or creates one and return a list
# create function to compare cypherword with list


# create file if it does not exist
def createFile(filePath):
    try:
        file = open(filePath, "r", encoding="utf-8")
    except:
        file = open(filePath, "x", encoding="utf-8")
    file.close()


# returns true, if empty
def isFileEmpty(filePath):
    createFile(filePath)
    file = open(filePath, "r", encoding="utf-8")
    result = True
    if file.readlines():
        result = False
    file.close()

    return result


# get words from vocabulary using pattern
def extractWords(filePath):
    pattern = "\d*\s*(\w*)"
    if not isFileEmpty(filePath):
        list = []
        print("there are words in vocabulary")
        file = open(filePath, "r", encoding="utf-8")
        lines = file.readlines()
        for line in lines:
            theWord = re.match(pattern, line).group(1)
            list.append(theWord)

        return list


# external one lane function to get sorted list set up
# should return a list from sorted list file
def makeItWork(listPath, rawTextPath):
    if isFileEmpty(listPath):
        pass


# this function is an external tool to compare cypherword with
# vocabulary or sorted list of words
def compareCypherWord(arg):
    pass


path = ".\\Files folder\\"
listPath = path+"sortedWordList.txt"
rawTextPath = path+"vocabulary.txt"

extractWords(listPath)
