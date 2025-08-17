n = int(input())
result = []
for i in range(n) :
    sample = input()
    result.append(sample)
result2 = list(set(result))
result2.sort(key = lambda x:(len(x), x))
for i in range(len(result2)) :
    print(result2[i])