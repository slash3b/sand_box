'''
Find if values is permutation of key values in the following way:

For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
should return 1 as it is permuation

but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
should return 0

'''

def solution(A):
    return 1 if sum(range(len(A)+1)) == (sum(A)) else 0
