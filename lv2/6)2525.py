a, b = map(int, input().split())
c = int(input())

d = (b+c) // 60
b = (b+c) % 60

a = (a + d) % 24

print(a, b)