import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = deque()
for i in range(n) :
    order = input().split()
    if(order[0]=='push') :
        q.append(int(order[1]))
    elif(order[0]=='pop') :
        if not q :
            print(-1) 
        else : 
            pop_value = q.popleft()
            print(pop_value)
    elif(order[0]=='size') :
        print(len(q))
    elif(order[0]=='empty') :
        if not q :
            print(1)
        else :
            print(0)
    elif(order[0]=='front') :
        if not q :
            print(-1)
        else :
            print(q[0])
    elif(order[0]=='back') :
        if not q :
            print(-1)
        else :
            print(q[-1])