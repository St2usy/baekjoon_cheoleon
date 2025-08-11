## 예를 들어 10진법으로 157(10) 표현시
## 157이 몇째 자리수 인지 확인 -> 3째 자리 수
## 1 * 10^2 + 5*10^1 + 7*10^0

## 36진법으로 60466175(10) 표현시
## 60466175를 이하 n로 표시, 36을 이하 x로 표시
sample = list(map(int, input().split()))
n = sample[0]
x = sample[1]
result = []
while(1) :
    if(n<x) :
        result.append(n)
        break
    else :
        result.append(n%x)
        n = n//x

for i in range(len(result)) :
    if 10 <= result[i] <= 35:
        result[i] = chr(65 + (result[i]- 10))    

print(''.join(map(str,result[::-1])))
