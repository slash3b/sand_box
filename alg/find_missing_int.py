
from pprint import pprint

def work(integers: list):
    my_list = sorted(integers)

    for k,v in enumerate(my_list):
        next = k + 1
        diff = my_list[next] - my_list[k]
        if diff > 1:
            return diff
    return None

pprint(work([3,6,1]))