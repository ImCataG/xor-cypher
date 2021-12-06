import sys

inputPath = 'output'

fileInput = open(inputPath, "rb")


inputString = fileInput.read()
lengthString = len(inputString)

decryptedString = ""

for d in range(128):
    decryptedString = ""
    for x in inputString:
        #print(x)
        decryptedString = decryptedString + chr(x ^ d)
    out = 'file' + str(d) + '.txt'

    g = open(out, 'w')

    print(decryptedString, file = g)

    g.close()
