from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
d = deque()
for i in range(n) :
    order = input().split()
    if order[0] == '1' :
        d.appendleft(int(order[1]))
    elif order[0] == '2' :
        d.append(int(order[1]))
    elif order[0] =='3' :
        if not d :
            print(-1)
        else :
            print(d.popleft())
    elif order[0] =='4' :
        if not d :
            print(-1)
        else :
            print(d.pop())
    elif order[0] =='5' :
        print(len(d))
    elif order[0] =='6' :
        if not d :
            print(1)
        else :
            print(0)
    elif order[0] =='7' :
        if not d :
            print(-1)
        else :
            print(d[0])
    elif order[0] =='8' :
        if not d :
            print(-1)
        else :
            print(d[-1])
