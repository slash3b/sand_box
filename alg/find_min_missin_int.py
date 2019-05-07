a =  [1, 2, 4]


# find max value
# build array with length equal to the max + 1 + 999 999
# count all elements
# go through elements and first that has 0 as count it missing

# what to do with negative numbers + 1 000 000

def find_min_missing(aList: list):

    maximum = max(aList)
    count = [0] * (maximum + 2000001)

    for x in aList:
        internalIndx = x + 1000000
        if count[internalIndx] != aList[internalIndx] and count[internalIndx] == 0:
            count[internalIndx] = 1

    counter = 0
    for x in count:
        if x == 0:
            missingValue = counter - 1000000
            if missingValue <= 0:
                return 1
            else:
                return missingValue
        counter += 1

    return 0

print(find_min_missing(a))

