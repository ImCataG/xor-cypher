import sys

if len(sys.argv) != 4:
    print('invalid arguments')
    exit()

secret = sys.argv[1]
sl = len(secret)

input = sys.argv[2]

output = sys.argv[3]

f = open(input, 'r')
g = open(output, 'wb')

s = f.read()

f.close()
i = 0

res = ''

for l in s:
    t = bin(ord(l) ^ ord(secret[i%sl]))[2:]
    if len(t) != 8:
        res += '0' * (8-len(t))
    res += t
    i += 1

#print(res, file = g, end ='')

g.write(bytearray(int(res[x:x+8], 2) for x in range(0, len(res), 8)))

g.close()