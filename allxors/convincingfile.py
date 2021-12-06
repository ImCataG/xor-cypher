import sys

check = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.;:!?\'\"()\n/\\<>- 0123456789' 

good = []
maxx = 0

for d in range(128):
    res = 0
    inp = 'file' + str(d) + '.txt'

    try:
        f = open(inp, 'r')
        inputString = f.read()
    except:
        print('you cant read a file or something')
        sys.exit()

    for x in inputString:
        #print(x)
        if x in check:
            res += 1

    if res > maxx:
        good = [d]
        maxx = res
    elif res == maxx:
        good.append(d)

print(good)