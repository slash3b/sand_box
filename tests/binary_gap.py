def solution(n):
    result = []
    while n > 0:
        result.append(str(n%2))
        n = int(n/2)
    indexes = []
    for k,v in enumerate(reversed(result)):
        if v == '1':
            indexes.append(k)
    if len(indexes)%2:
        indexes = indexes[:-1]
    gaps = []
    for k, v in enumerate(indexes):
        if (k+1 < len(indexes)):
            # take into account consequitive indexes and do not append in case there is no actual length between them
            gaps.append((indexes[k+1] - indexes[k])-1)
    if len(gaps) > 0:
        return max(gaps)
    else:
        return 0

print(solution(15))