#!/usr/bin/python2

msg = 'Skynet is alive !'
msgBinaryStr = ''.join('{0:08b}'.format(ord(x), 'b') for x in msg)
payloadByteArray = []
color = [255,255,255]
nbBits = 4
mask = 256 - pow(2, nbBits)

while (len(msgBinaryStr) % nbBits != 0):
    msgBinaryStr += '0'

i = 0
while (len(msgBinaryStr) > 0):
    data = int(msgBinaryStr[0:nbBits], 2)
    msgBinaryStr = msgBinaryStr [nbBits:]
    if (i % 3 == 0):
        payloadByteArray.append([])
    payloadByteArray[i // 3].append((color[i % 3] & mask) + data)
    i += 1

while (i % 3 != 0):
    payloadByteArray[i // 3].append(color[i % 3])
    i += 1

# Printing color array :
for i in range(0, len(payloadByteArray)):
    print "{}: {} {} {}".format(i, payloadByteArray[i][0], payloadByteArray[i][1],payloadByteArray[i][2])