## 소인수 분해 : 소수인 인수로 분해 시키기
## 약수 구하기 프로세스 + 소수 구하기 프로세스 혼합

n = int(input())
if (n==1) : pass
else : 
    for i in range(2, n+1) :
        if(n%i==0) :
            while(1) :
                if(n%i!=0) :
                    break
                n = n/i
                print(i)
