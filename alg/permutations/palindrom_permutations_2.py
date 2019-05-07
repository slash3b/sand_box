from pprint import pprint

permutation_1 = 'tactcoa'
permutation_2 = 'abba'
permutation_3 = 'abbb'
permutation_4 = 'ab'


def isPalindrome(perm: str) -> bool:
    map = []
    counter = 0
    for x in perm:
        if x in map:
            counter -= 1
        else:
            map.append(x)
            counter += 1

    if counter == 0 or counter == 1:
        return True
    return False

pprint(isPalindrome(permutation_1))
pprint(isPalindrome(permutation_2))
pprint(isPalindrome(permutation_3))
pprint(isPalindrome(permutation_4))