import sys

f = open('input.txt', 'r')
g = open('output', 'rb')
o = open('passwd.txt', 'w')

input1 = f.read()
input2 = g.read()

f.close()
g.close()

for i in range(len(input1)):
    print(chr(ord(input1[i]) ^ input2[i]), file = o, end = '')

o.close()