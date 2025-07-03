n = int(input())

str = ""

for i in range(1, n+1) :
    str = str + " " * (n-i) + "*" * i
    if(i!=n) :
        str +="\n"
print(str)