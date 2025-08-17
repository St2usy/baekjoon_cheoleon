import sys
input = sys.stdin.readline
n = int(input())
stack = []
out = []
for i in range(n) :
    order = input().split()
    if order[0] == '1' :
        stack.append(int(order[1]))
    elif order[0] == '2' :
        if not stack : 
            out.append(-1)
        else :
            out.append(stack.pop())
    elif order[0] =='3' :
        out.append(len(stack))
    elif order[0] =='4' :
        if not stack :
            out.append(1)
        else :
            out.append(0)
    elif order[0] =='5' :
        if not stack :
            out.append(-1)
        else : 
            out.append(stack[-1])
sys.stdout.write('\n'.join(map(str, out)))