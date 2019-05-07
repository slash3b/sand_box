from pprint import pprint

def getBinaryGap(number: int):
    binaryRepresentaion = bin(number)
    binaryString = binaryRepresentaion[2:] # got rid of 0b prefix

    map = []
    counter = 0

    for i in binaryString:
        if int(i) == 1:
            map.append(counter)
        counter += 1
    
    if len(map) == 1 or len(map) == 0:
        return 0

    max = 0
    n = len(map)-1
    while n > 0:
        diff = abs(map[n] - map[n-1]) - 1
        if diff > max:
            max = diff
        n -= 1

    return max


print(getBinaryGap(1025))

print(getBinaryGap(10250))

print(getBinaryGap(1025))

print(getBinaryGap(2147483649))