## 소수 : 1과 자기자신 제외 약수가 없는 수, 즉 약수의 갯수 2

# n = int(input())
# count=0
# for i in range(1,n+1) :
#     if(n%i==0) :
#         count +=1
# if(count==2) :
#     print("소수")
# else :
#     print("not")

M = int(input())
N = int(input())
result = []
sum = 0
for i in range(M, N+1) :
    count = 0
    for j in range(1, i+1) :
        if(i%j==0) :
            count+=1
    if(count==2) :
        result.append(i)
        sum += i

if(len(result)>=1) :
    print(sum)
    print(min(result))
else :
    print(-1)