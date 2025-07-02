a = int(input())
b = input()
num = list(b)

digits = [int(d) for d in num]

digits.reverse()  # 리스트를 뒤집습니다.

result = map(lambda x: x * a, digits)

print(*result, sep='\n') 
# *은 unpacking operator로, 리스트의 각 요소를 개별 인자로 전달합니다.
# sep='\n'은 각 요소를 줄바꿈으로 구분하여 출력합니다.

print(a * int(b))  # a와 b를 곱한 결과를 출력합니다.
