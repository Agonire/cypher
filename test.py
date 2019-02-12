import cypher

testPlainCaesar = ["alfpha", "omega!*!@(,)", "zet purpose", "hello"]
testCypherCaesar = ["bmgqib", "pnfhb!*!@(,)", "afu qvsqptf", "ifmmp"]

testPlainVizhener = ["dog", "creature", "the independent woman"]
testCypherVizhener = ["eqh", "dtfcuwsg", "ujf koffrfpegov xqnco"]

def testCypher(lCypher, key, testPlain, testCypher):
    iterations = len(testPlain)
    print("\n")

    for i in range(iterations):
        outpt = lCypher.encrypt(testPlain[i], key)
        print("The plain text is:         ", testPlain[i])
        print("The cypher text is:        ", outpt)
        print("The cypher test should be: ", testCypher[i])
        print("The key is: ", key)
        print("The encrypting is correct:                  ",outpt == testCypher[i],"\n\n")

    for i in range(iterations):
        outpt = lCypher.decrypt(testCypher[i], key)
        print("The cypher text is:       ", testCypher[i])
        print("The plain text is:        ", outpt)
        print("The plain test should be: ", testPlain[i])
        print("The key is: ", key)
        print("The decrypting is correct:                  ",outpt == testPlain[i],"\n\n")


leKey = "bc"

leCaesar = cypher.Caesar
leVizhener = cypher.Vizhener

# testCypher(leCaesar, 1, testPlainCaesar, testCypherCaesar)
# testCypher(leVizhener, leKey, testPlainVizhener, testCypherVizhener)
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


initialPermutation = "2,6,3,1,4,8,5,7"
finalPermutation = "4,1,3,5,7,2,8,6"
permutationTen = "3,5,2,7,4,10,1,9,8,6"
permutationEight = "6,3,7,4,8,5,10,9"
expansionPermutation = "4,1,2,3,2,3,4,1"
permutationFour = "2431"
s_zero= "1032,3210,0213,3131"
s_one = "1123,2013,3010,2103"

xorSplit = splitInTwo(xorLines("10111110", "10010100"))
print(xorSplit["left"])
l = substitutionBox("1032,3210,0213,3131", "1000")
# r = substitutionBox(s_one, xorSplit["right"])
# funcResult = l + r
print(l)
