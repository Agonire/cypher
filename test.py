import cypher

def testCeaser():
    testPlain = ["alfpha", "omega", "zet purpose"]
    testCypher = ["bmgqib", "pnfhb", "afu qvsqptf"]


    # for i in range(3):
    #     outpt = testPlain[i] == testCypher[i]
    #     print(testPlain[i], testCypher[i])
    #     print(outpt)

    for i in range(3):
        outpt = cypher.Ceaser.makeCypherText(testPlain[i], 1) == testCypher[i]
        # print(test(testPlain[i], 1), testCypher[i])
        print(outpt)

    # for i in range(3):
    #     outpt = Ceaser.makePlainText(testCypher[i], 1) == testPlain[i]
    #     print(outpt)



# test()

testCeaser()
