from pprint import pprint
import hashlib

hash_table = {}


first_sample = (b'test', 333333)
second_sample = (b'poin -black', 333333)
third_sample = (b'http://sublime.org', '<html><h1>OK</h1></html>')

m = hashlib.sha256()
# m.update(b"Nobody inspects")
# m.update(b" the spammish repetition")
# pprint(m.digest())


m.update(first_sample[0])
hash_table[m.hexdigest()] = first_sample[1]
m.update(second_sample[0])
hash_table[m.hexdigest()] = second_sample[1]
m.update(third_sample[0])
hash_table[m.hexdigest()] = third_sample[1]

m.update(b'test')


# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

def hash_key(key: str) -> str:
    m = hashlib.sha256()
    m.update(key.encode('utf-8'))
    return m.hexdigest()

stringA = '4abcdef'
stringB = 'defabc'

hash_map = {}
for i in stringB:
    hash_map[hash_key(i)] = True

isIdentical = True
for a in stringA:
    if hash_key(a) not in hash_map:
        isIdentical = False
        break

pprint(isIdentical)

# end of permutation