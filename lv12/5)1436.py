## n번째 큰 종말의 수 찾기..?
## 666이 1번째

n = int(input())
cnt = 0
result = 0
while(1) :
    if('666' in str(result)) :
        cnt +=1
        if(n==cnt) :
            print(result)
            break
        else :
            result +=1
    else : 
        result +=1


