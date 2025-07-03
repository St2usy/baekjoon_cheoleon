n = int(input())
sample = list(map(int, input().split()))
k = int(input())
count = 0
for i in sample :
    if(i == k) :
        count +=1
print(count)