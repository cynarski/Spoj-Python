import struct

def printfloat(f: float):
    bytes = struct.pack('<f',f)
    unpacked32bits = struct.unpack('<I',bytes)
    return hex(unpacked32bits[0])

testy = int(input())
for i in range(testy):
    dane = float(input())
    result = printfloat(dane)[2:]
    chunks = [result[i:i+2] for i in range(0,len(result),2)]
    while len(chunks) < 4:
        chunks.append('0')
    for i in range(len(chunks)):
        if chunks[i] != '0' and chunks[i][0] == '0':
            chunks[i] = chunks[i][1]
    print(' '.join(chunks))

