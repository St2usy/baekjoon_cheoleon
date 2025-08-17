import sys
input = sys.stdin.readline
stack = []
n = int(input())
for i in range(n) :
    sample = input().rstrip('\n')
    for ch in sample :
        if(stack) :
            if(ch=='(') :
                stack.append(ch)
            elif(ch==')' and stack[-1]=='(') :
                stack.pop()
        else :
            stack.append(ch)
    if not stack : 
        print('YES')
    else : 
        print('NO')
        stack.clear()