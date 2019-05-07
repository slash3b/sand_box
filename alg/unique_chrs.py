from pprint import pprint

string = 'abcedfgHih'

def check_unique(line: string):
    chrMap = {}
    for x in line:
        if x in chrMap:
            return False
        chrMap[x] = True
    return True

pprint(check_unique(string))