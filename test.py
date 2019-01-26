
def testCeaser():
    testPlain = ["alfpha", "omega", "zet purpose"]
    testCypher = ["bmgqib", "pnfhb", "afu qvsqptf"]

    for i in range(3):
        outpt = testPlain[i] == testCypher[i]
        print(outpt)

    for i in range(3):
        outpt = testPlain[i] == testPlain[i]
        print(outpt)

    # for i in range(3):
    #     outpt = Ceaser.makeCypherText(testPlain[i], 1) == testCypher[i]
    #     print(outpt)
    #
    # for i in range(3):
    #     outpt = Ceaser.makePlainText(testCypher[i], 1) == testPlain[i]
    #     print(outpt)
