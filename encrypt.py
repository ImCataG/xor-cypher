import sys

if len(sys.argv) != 4:
    print('Invalid number of arguments!') 
    sys.exit() # Errors out if argument number is invalid

secret = sys.argv[1]
secretLen = len(secret)

for i in secret:
    if not i.isalpha() and not i.isnumeric():
        print('Password must contain only letters and numbers!')
        sys.exit() # Errors out if password is invalid

if secretLen > 15 or secretLen < 10:
    print('Password length must be between 10 and 15 characters!')
    sys.exit() # Errors out if password length is invalid

input = sys.argv[2]

output = sys.argv[3]

try:
    f = open(input, 'r', encoding = 'utf8') 
except FileNotFoundError:
    print('File', input, 'does not exist!')
    sys.exit() # Errors out if input file does not exist

g = open(output, 'wb')

textIn = f.read()
f.close()

# Initialise variables used in the xor process
counter = 0 
textOut = ''

for letter in textIn: # The actual encryption algorithm
    textOut += chr(ord(letter) ^ ord(secret[counter%secretLen]))
    counter += 1

g.write(bytes(textOut.encode('utf8'))) # Write to binary file

g.close()