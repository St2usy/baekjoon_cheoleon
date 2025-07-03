n = int(input())
str = ""
for i in range(1, n+1) :
    str += "*" * i
    if i!=n :
        str += "\n"

print(str)