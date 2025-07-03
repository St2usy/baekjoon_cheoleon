result = int(input())
sample = 0
n = int(input())
for i in range(n) :
    a, b = map(int, input().split())
    sample += a*b

if(result==sample) : print("Yes")
else : print("No")