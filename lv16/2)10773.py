import sys
input = sys.stdin.readline

result = []
sum = 0
n = int(input())
for i in range(n) :
    k=int(input())
    if(k==0) :
        result.pop()
    else :
        result.append(k)
for i in result :
    sum +=i
print(sum)