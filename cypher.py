
from abc import ABC, abstractmethod
import textwrap

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
def checkBlockLength(bits, length = 8):
    if len(bits) == length:
        return True
    else:
        return False

def divideBitStream(bitStream, length = 8):
    if len(bitStream)%length == 0:
        return textwrap.wrap(bitStream, length)
    else:
        return length - len(bitStream)%length

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

def addEmptyBit(bits, bitRate = 8):
    result = ""
    if len(bits) > bitRate:
        print("You are trying to convert bigger bit-rate in lower, in addEmptyBit function")
    if len(bits) < bitRate:
        for i in range(bitRate - len(bits)):
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

def getFileContent(path):
    try:
        f = open(path, "rt", encoding="utf-8")
        content = f.read()
        f.close()
        return content
    except:
        print("File in destination " + path + " does not exist")
        return False

def setFileContent(path, content = ""):
    try:
        f = open(path, "xt", encoding="utf-8")
        print("\n    Creating and writing to a new file at " + path + " location\n")
    except:
        print("\n    Writing to an existing file at " + path + " location\n")
    finally:
        f = open(path, "wt", encoding="utf-8")
        f.write(content)
        f.close()

def textToBitStream(text, bitRate = 8):
    # Since this function is working with ASCII table the lowest possible bit-rate value should be 8, or you will get incorrect values
    bitStream = ""
    for symbol in text:
        bitValue = addEmptyBit(toBit(ord(symbol)), bitRate)
        bitStream += bitValue

    return bitStream

def bitStreamToText(bitStream, bitRate = 8):
    # Since this function is working with ASCII table the lowest possible bit-rate value should be 8, or you will get incorrect values
    text = ""
    bitStream = textwrap.wrap(bitStream, bitRate)
    for item in bitStream:
        text += chr(fromBit(item))

    return  text

def getValue(tokenName, default = "", length = -1):
    result = ""
    if default and len(default) != length and length > 0:
        print("**Default value length is incorrect, during function invoking")
        return False

    while True:
        if default:
            inp = input("\n Enter " + tokenName + " please, or default " + default + " will be used\n\n  ")
        else:
            inp = input("\n Enter " + tokenName + " please\n\n  ")

        if inp and len(inp) != length and length > 0:
            print("**Input value length is incorrect")
            continue

        if inp:
            result = inp
            # print("\n New value for " + tokenName + " will be used - \"" + result + "\"\n")
            break
        if not inp and default:
            result = default
            # print("\n *Default " + tokenName + " will be used\n")
            break
        print(" You must enter value for " +  tokenName)

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

    initialPermutation = "2,6,3,1,4,8,5,7"
    finalPermutation = "4,1,3,5,7,2,8,6"
    permutationTen = "3,5,2,7,4,10,1,9,8,6"
    permutationEight = "6,3,7,4,8,5,10,9"
    expansionPermutation = "4,1,2,3,2,3,4,1"
    permutationFour = "2,4,3,1"
    s_zero= "1032,3210,0213,3131"
    s_one = "1123,2013,3010,2103"

    @staticmethod
    def keyGenerator(key, rounds = 1):
        keys = []
        key = permutation(key, DES.permutationTen)
        parts = splitInTwo(key)
        for i in range(1, rounds+1):
            left = shift(parts["left"], i)
            right = shift(parts["right"], i)
            key = left + right
            keys.append( permutation(key, DES.permutationEight) )
        return keys


    @staticmethod
    def crypt(bits, key):
        splitedInitPerm = splitInTwo(bits)

        rightInitPerm = permutation(splitedInitPerm["right"], DES.expansionPermutation)
        xorWithKey = splitInTwo(xorLines(rightInitPerm, key))
        sBoxResult = substitutionBox(DES.s_zero, xorWithKey["left"]) + substitutionBox(DES.s_one, xorWithKey["right"])
        sBoxResult = permutation(sBoxResult, DES.permutationFour)

        splitedInitPerm["left"] = xorLines(splitedInitPerm["left"], sBoxResult)
        result = splitedInitPerm["left"] + splitedInitPerm["right"]

        return result


    @staticmethod
    def encrypt(bits, keys):
        bits = permutation(bits, DES.initialPermutation)

        for i in range(len(keys)):
            bits = DES.crypt(bits, keys[i])
            print(bits + " as result of " + str(i+1) + " encryption round, key - " + keys[i] )
            shift(bits, int(len(bits)/2))
        # nigelation of simple P in iteration
        result = shift(bits, int(len(bits)/2))

        result = permutation(result, DES.finalPermutation)
        print("\n" + result + " result of encryption\n" )

        return result


    @staticmethod
    def decrypt(bits, keys):
        bits = permutation(bits, DES.initialPermutation)

        for i in reversed(range(len(keys))):
            bits = DES.crypt(bits, keys[i])
            print(bits + " as result of " + str(len(keys) - i) + " decryption round, key - " + keys[i] )
            shift(bits, int(len(bits)/2))
        # nigelation of simple P in iteration
        result = shift(bits, int(len(bits)/2))

        result = permutation(result, DES.finalPermutation)
        print("\n" + result + " result of decryption\n" )

        return result


    @staticmethod
    def start():
        key = "1101100110"
        text = "11000010"
        rounds = 2
        keys = DES.keyGenerator(key,rounds)
        print("\n\nkeys" + str(keys) + "\n\n")

        encr = DES.encrypt(text, keys)
        decr = DES.decrypt(encr, keys)

class StreamCypher(Cypher):

    @staticmethod
    def getValues():
        #tokens for getValue function
        plainToken = "plain text file location"
        cypherToken = "cypher text file location"
        resultToken = "decryption text file location"
        patternToken = "pattern"
        initRegToken = "initial register"

        #default values
        ptPath = "./Text files/plainText.txt"
        ctPath = "./Text files/cypherText.txt"
        resPath = "./Text files/resultText.txt"
        pattern =  "8,4,3,2,0"
        initialRegister = "00010110"


        print("\n   Starting stream cypher program \n initialization...\n")

        ptPath = getValue(plainToken, ptPath)
        ctPath = getValue(cypherToken, ctPath)
        resPath = getValue(resultToken, resPath)
        pattern = getValue(patternToken, pattern)
        initialRegister = getValue(initRegToken, initialRegister)

        return {"ptPath":ptPath, "ctPath":ctPath, "resPath":resPath, "pattern":pattern, "initReg":initialRegister}


    @staticmethod
    def keyGenerator(initialRegister, pattern, bitStream = "", length = 0):
        if length:
            keyLength = length
        else:
            keyLength = len(bitStream)
        keyStream = ""
        pattern = pattern.split(",")

        if int(pattern[0]) != len(initialRegister):
            print("\n\n   Initial register does not have valid length, program can't generate keys\n\n")
            return False

        pattern = pattern[1:] #removing 1st elem of a list
        register = initialRegister[::-1] #reverse bit stream
        for i in range(keyLength):
            newBit = 0
            for val in pattern:
                newBit += int(register[int(val)])

            newBit = str(newBit%2)
            keyStream += register[0]
            register = register[1:] + newBit #next round register

        return keyStream #string of bits length equal to


    @staticmethod
    def crypt(fromPath, toPath, initialRegister, pattern):

        content = getFileContent(fromPath)
        if content or content == "":
            bitStream = textToBitStream(content)
            keyStream = StreamCypher.keyGenerator(initialRegister, pattern, bitStream = bitStream)

            bitStream = xorLines(bitStream, keyStream)
            output = bitStreamToText(bitStream)

            setFileContent(toPath, output)
        else:
            # this option is used to create empty file if not exist
            setFileContent(fromPath)


    @staticmethod
    def start():
        data = StreamCypher.getValues()

        print("\n Starting encrytion...")
        StreamCypher.crypt(data["ptPath"], data["ctPath"], data["initReg"], data["pattern"])

        print("\n Starting decrytion...")
        StreamCypher.crypt(data["ctPath"], data["resPath"], data["initReg"], data["pattern"])

class BlockCypher(Cypher):



    @staticmethod
    def getValues():


        #tokens for getValue function
        inToken = "input text file location"
        outToken = "cypher text file location"
        keyToken =  "key"
        initRegToken = "initial register"
        workingModToken = "working mod"
        cypherToken = "cypher mod"

        #default values
        inPath = "./Text files/plainText.txt"
        outPath = "./Text files/cypherText.txt"
        key =  "1111111111000000000011111111110000000000111111111100000000001111111111000000000011111111110000000000111111111100000000001111111111000000000011111111110000000000111111111100000000001111111111000000000011111111110000000000111111111100000000001111111111001100"
        initialRegister = ""
        workingMod = ""
        cypherMod = ""

        print("\n   Starting block cypher program \n initialization...\n")

        inPath = getValue(inToken, inPath)
        outPath = getValue(outToken, outPath)
        key = getValue(keyToken, key)
        while True:
            if not checkBlockLength(key, 256):
                print("You have entered incorrect key length")
                key = getValue(keyToken)
            else:
                break

        initialRegister = getValue(initRegToken, initialRegister)
        workingMod = getValue(workingModToken, workingMod)
        while True:
            if workingMod.lower() == "simple permutation" or workingMod.lower() == "sp":
                workingMod = "sp"
                break
            elif workingMod.lower() == "gamma" or workingMod.lower() == "g":
                workingMod = "g"
                break
            elif workingMod.lower() == "gamma feadback" or workingMod.lower() == "gf":
                workingMod = "gf"
                break
            else:
                print("  You have entered incorrect working mod value! Try \"Simple permutation\", \"Gamma\" or \"Gamma feadback\"")
                workingMod = getValue(workingModToken)

        cypherMod = getValue(cypherToken, cypherMod)
        while True:
            if cypherMod.lower() == "encrypt" or cypherMod.lower() == "e":
                cypherMod = "e"
                break
            elif cypherMod.lower() == "decrypt" or cypherMod.lower() == "d":
                cypherMod = "d"
                break
            else:
                print("  You have entered incorrect cypher mod value! Try encrypt or decrypt")
                cypherMod = getValue(cypherToken)


        return {"inPath":inPath, "outPath":outPath,  "key":key, "initReg":initialRegister, "workingMod":workingMod, "cypherMod":cypherMod}


    @staticmethod
    def simplePermMod(bitStream, key, cypherMod):
        s_0 = "1 0 3 2,3 2 1 0,0 2 1 3,3 1 3 1"
        s_1 = "1 1 2 3,2 0 1 3,3 0 1 0,2 1 0 3"

        #...s_8
        pass

    @staticmethod
    def gamma(bitStream, key, cypherMod):
        pass

    @staticmethod
    def gammaFeadback(bitStream, key, cypherMod):
        pass


    @staticmethod
    def start():
        data = BlockCypher.getValues()

        bitStream = textToBitStream(getFileContent(data["inPath"]))

        result = BlockCypher.simplePermMod(bitStream, data["key"], data["cypherMod"])

        # if data["workingMod"] == "sp":
        #     print("  Using simple permutation mod")
        #     result = BlockCypher.simplePermMod(bitStream, data["key"], data["cypherMod"])
        # elif data["workingMod"] == "g":
        #     print("  Using gamma mod")
        #     result = BlockCypher.gamma(bitStream, data["key"], data["cypherMod"])
        # elif data["workingMod"] == "gf":
        #     print("  Using gamma feadback mod")
        #     result = BlockCypher.gammaFeadback(bitStream, data["key"], data["cypherMod"])

        setFileContent(data["outPath"], bitStreamToText(result))


        print("\n\n Would you like to continue? \n")
        inp = input()
        if bool(inp):
            BlockCypher.start()
        else:
            print("\n\n Ending block cypher \n")


DES.start()
# StreamCypher.start()
# BlockCypher.start()
