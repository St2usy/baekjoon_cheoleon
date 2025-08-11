# sample = list(map(int, input().split()))
# for i in range(2) :

# n = int(input())
# mat = [list(map(int, input().split())) for i in range(n)]
# print(mat)

# sample = list(map(int, input().split()))
# mat2 = []
# for i in range(sample[0]) :
#     row = list(map(int, input().split()))
#     if(len(row)>sample[1]) :
#         print("err")
#         sys.exit(1)
#     else :
#         mat2.append(row)
# print(mat2)

sample = list(map(int,input().split()))
mat1 = [list(map(int, input().split())) for i in range(sample[0])]
mat2 = [list(map(int, input().split())) for i in range(sample[0])]
result = [[0]*sample[1] for i in range(sample[0])]
for i in range(sample[0]) :
    for j in range(sample[1]) :
        result[i][j] = mat1[i][j] + mat2[i][j]

# print(' '.join(map(str, bucket)))
result2 = "\n".join(" ".join(map(str, row)) for row in result)
print(result2)