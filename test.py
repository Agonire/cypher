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

testCypher(leCaesar, 1, testPlainCaesar, testCypherCaesar)
testCypher(leVizhener, leKey, testPlainVizhener, testCypherVizhener)
