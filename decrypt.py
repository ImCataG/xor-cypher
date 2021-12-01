import sys
import time
if len(sys.argv) != 4:
    print('invalid arguments')
    exit()

input = sys.argv[1]

secret = sys.argv[2]
sl = len(secret)

output = sys.argv[3]

f = open(input, 'rb')
g = open(output, 'w')

s = f.read()

f.close()

res = ''

for i in s:
    t = bin(i)[2:]
    if len(t) != 8:
        res += '0' * (8-len(t))
    res += t


j = 0

for i in range(0, len(res), 8):
    t = int(res[i:i+8], 2)
    print(chr(ord(secret[j%sl]) ^ t), file = g, end = '')
    j += 1

g.close()