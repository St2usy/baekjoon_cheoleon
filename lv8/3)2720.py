T = int(input())
for i in range(T) :
    Q_count = 0
    D_count = 0
    N_count = 0
    P_count = 0
    C = int(input())
    while(C!=0) :   
        if(C>=25) :
            Q_count += C//25
            C = C%25
        elif(C>=10 and C<25) :
            D_count += C//10
            C = C%10
        elif(C>=5 and C<10) :
            N_count += C//5
            C = C%5
        else : 
            P_count += C//1
            C = C%1
    print(Q_count, D_count, N_count, P_count)    
