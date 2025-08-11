sample = list(map(int, input().split()))
bucket = [i+1 for i in range(sample[0])]
for i in range(sample[1]) :
    sample2 = list(map(int, input().split()))
    bucket[sample2[0]-1:sample2[1]] = bucket[sample2[0]-1:sample2[1]][::-1]
print(' '.join(map(str, bucket)))