def reverse(A):
    N = len(A)
    for i in range(N // 2):
        k = N - i - 1
        A[i], A[k] = A[k], A[i]
    return A

reverse([1,2,3,4,5,6,7,8,9,10])