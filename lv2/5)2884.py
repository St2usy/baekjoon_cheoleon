a, b = map(int, input().split())

if(b-45 < 0):
    if(a == 0):
        a = 23
    else :
        a -= 1
    b = b - 45 + 60 # 60 단위로 돌아가는 시계, 45분전이므로 -45 후 +60을 함 (b-45 < 0 일 때)
else :
    b -= 45

print(a, b)