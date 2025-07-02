a,b,c = map(int, input().split())

print((a+b)%c)
print(((a%c) + (b%c)) % c)
print((a*b)%c)
print(((a%c) * (b%c)) % c)
# The above code calculates the sum and product of two integers a and b modulo c,