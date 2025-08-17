import sys
from collections import deque

sample = list(map(int, input().split()))
q = deque()
result = []
count = 1
for i in range(1, sample[0]+1) :
    q.append(i)
for _ in range(sample[0]): 
    for i in range(sample[1]) :
        last_value = q.popleft()
        if i!=sample[1]-1 :
            q.append(last_value)
        else :
            result.append(last_value)
print('<', end='')
for i in range(len(result)) :
    if i!=len(result)-1 :
        print(result[i], end=', ')
    else :
        print(result[i], end='')
print('>')