import sys

if len(sys.argv) != 4:
    print('Invalid number of arguments!') 
    sys.exit() # Errors out if argument number is invalid

input = sys.argv[1]

secret = sys.argv[2]
secretLen = len(secret)

for i in secret:
    if not i.isalpha() and not i.isnumeric():
        print('Password must contain only letters and numbers!')
        sys.exit() # Errors out if password is invalid

output = sys.argv[3]

try:
    f = open(input, 'rb') 
except FileNotFoundError:
    print('File', input, 'does not exist!')
    sys.exit() # Errors out if input file does not exist

g = open(output, 'w')

textIn = (f.read()).decode('utf-8') # Read from binary file
f.close()

# Initialise variables used in the xor process
textOut = ''
counter = 0

for letter in textIn: #T he actual decryption algorithm
    textOut += chr(ord(letter) ^ ord(secret[counter%secretLen]))
    counter += 1

print(textOut, file = g, end = '')

g.close()