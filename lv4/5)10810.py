m, n = map(int, input().split())
list = [0 for i in range(m)]
for x in range(n) :
    i,j,k = map(int, input().split())
    for x in range(i-1, j) :
        list[x] = k
print(map(int, list))
    
