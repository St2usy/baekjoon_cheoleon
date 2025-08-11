## N이 주어질 때
## 3x + 5y = N을 만족할 때, x+y의 최솟값
## ex) 57 : 3*9 + 5*4 or 3*4 + 5*9

n = int(input())
result = []
for i in range(0, n//5+1) :
    for j in range(0, n//3+1) :
        if(3*j + 5*i == n) :
            result.append(i+j)
if(len(result)>=1):
    print(min(result))
else :
    print(-1)