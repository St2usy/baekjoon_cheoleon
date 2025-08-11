sample = [list(input()) for i in range(5)]
result = []
for i in range(5) :
    result.append(len(sample[i]))
max_val = max(result)

for i in range(max_val) :
    for j in range(5) :
        try :
            print(sample[j][i], end='')
        except IndexError:
            continue

# input().split()
# list(map(int, input().split()))
# list(input())
# k = list(map(int, list(input())))
# print(k)