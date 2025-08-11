## 완전수 판별 -> n이 주어졌을 때 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수
## 입력(테스트케이스)은 한 줄 간격으로 주어짐
## 입력(테스트케이스)의 마지막은 -1
## 테스트케이스 마다 한줄에 하나씩 출력
## n이 완전수라면 ex) 6 = 1 + 2 + 3으로 출력, 약수는 오름차순
## n이 완전수가 아니라면 n is NOT perfect

## 어떤 특정 수의 약수를 구하는 방법 -> [16 : 1, 2, 4, 8, 16], [57 : 1, 3, 19, 57] 어떤 작은 소수를 특정수와 나누어서, 나누어 떨어지는지 확인, 그 몫을 재귀적으로 나누어 본다.
## 어떤 특정 수의 약수를 구하는 방법 -> n의 약수 -> n // i에서 나누어떨어지는 i값 확인 

## 소수의 판별 -> 1과 자기자신으로만 나누어 떨어지는 수. 즉 약수의 갯수가 2개

## 1) 완전수는 짝수가 아니다( 적어도 10^5 안에서는 )
## 2) 소수에서 유일한 짝수는 2다.
## 3) 유명한 소수 정리 : 2,3,5,7,13,17,19,31
## 4) 컴퓨터는 계산기다.. 명심할 것

# n = int(input())
# result = []
# sum = 0
# for i in range(1, n+1) :
#     if n%i==0 :
#         result.append(i)
# for i in range(0, len(result)-1) :
#     sum += result[i]
# if(sum==result[len(result)-1]) :
#     print("perfect")
# else : 
#     print("not")

while(1) :
    n = int(input())
    result = []
    if(n==-1) :
        break
    sum = 0
    for i in range(1, n+1) :
        if n%i==0 :
            result.append(i)
    for i in range(0, len(result)-1) :
        sum += result[i]
    if(sum==result[len(result)-1]) :
        print(n, '= ', end='')
        for i in range(len(result)-1) :
            if i==len(result)-2 :
                print(result[i])
            else :
                print(result[i], '+ ', end='')
    else :
        print(n, 'is NOT perfect.')