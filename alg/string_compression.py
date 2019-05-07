from pprint import pprint
import hashlib

string = 'tactcoaaaa'

def compress(str_to_compress: str) -> str:

    output = {}
    for v in str_to_compress:
        if v in output:
            output[v] += 1
        else:
            output[v] = 1

    def convert_to_str(items: iter):
        out = ''
        for x in items:
            if x[1] > 1:
                out += str(x[0]) + str(x[1])
            else:
                out += str(x[0])

        return out

    return convert_to_str(output.items())

pprint(compress(string))

