A = [-2, -3]

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    total = sum(A)
    equil = total//2;
    
    temp_sum = 0
    for k, v in enumerate(A):
        temp_sum += v
        if temp_sum >= equil:
            break
    if temp_sum == sum(A):
        return abs(total - A[-1])
    else:
        return abs(temp_sum - sum(A[k+1:]))

print(solution(A))