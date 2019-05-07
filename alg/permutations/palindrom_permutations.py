from pprint import pprint
import hashlib

permutation = 'tactcoa'


def hash_key(key: str) -> str:
    m = hashlib.md5()
    m.update(key.encode('utf-8'))
    return m.hexdigest()

def isPalindrome(perm: str) -> bool:
    # go through each symbol and flip its value by +1 and -1
    # get value by hash
    # if it is a palindrome then in the end you should get all zeroes and only one 1
    # because all other chars will have duplicates

    hash_map = {}
    for elem in perm:
        key = hash_key(elem)
        if key not in hash_map:
            hash_map[key] = 1
        else:
            hash_map[key] = 0

    return sum(hash_map.values()) == 1

pprint(isPalindrome(permutation))