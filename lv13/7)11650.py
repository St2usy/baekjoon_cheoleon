n = int(input())
result = []
for i in range(n) :
    sample = list(map(int, input().split()))

    result.append(sample)
result.sort(key = lambda x : (x[0], x[1]))
for i in range(len(result)) :
    print(' '.join(map(str, result[i])))

