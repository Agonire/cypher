import cypher

def testCaesar(key):
    testPlain = ["alfpha", "omega", "zet purpose"]

    #cypher text from external site
    testCypher = ["bmgqib", "pnfhb", "afu qvsqptf"]
    print("\n")


    for i in range(3):
        outpt = cypher.Caesar.makeCypherText(testPlain[i], key)
        print("The plain text is:         ", testPlain[i])
        print("The cypher text is:        ", outpt)
        print("The cypher test should be: ", testCypher[i])
        print("The key is: ", key)
        print("The encrypting is correct: ",outpt == testCypher[i],"\n\n")

    for i in range(3):
        outpt = cypher.Caesar.makePlainText(testCypher[i], key)
        print("The cypher text is:       ", testCypher[i])
        print("The plain text is:        ", outpt)
        print("The plain test should be: ", testPlain[i])
        print("The key is: ", key)
        print("The decrypting is correct: ",outpt == testPlain[i],"\n\n")





testCaesar(1)
