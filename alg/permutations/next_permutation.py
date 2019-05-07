from pprint import pprint


def rearrangeWord(word):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    length = len(word)-1

    while length >= 0:
        if (length-1 >= 0 and alpha.index(word[length]) > alpha.index(word[length-1])):
            return word[0:length-1] + word[length] + word[length-1] + word[length+1:]
        length -= 1

    return 'no answer'

    

pprint(rearrangeWord('hefg'))
pprint(rearrangeWord('pp'))
pprint(rearrangeWord('abcd'))
pprint(rearrangeWord('baca'))
pprint(rearrangeWord('xy'))
