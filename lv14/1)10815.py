n = int(input())
result = set()
sample = list(map(int, input().split()))
for i in range(n) :
    result.add(sample[i])
m = int(input())
sample2 = list(map(int, input().split()))
for i in range(m) :
    if(sample2[i] in result) :
        print(1, end=" ")
    else :
        print(0, end=" ")