bucket = list()
sum = 0
sub = 0
for i in range(20) :
    sample = list(map(str, input().split()))
    if(sample[2]=='A+') :
        sub += float(sample[1])
        sum += float(sample[1])*4.5
    elif(sample[2]=='A0') :
        sub += float(sample[1])
        sum += float(sample[1])*4
    elif(sample[2]=='B+') :
        sub += float(sample[1])
        sum += float(sample[1])*3.5
    elif(sample[2]=='B0') :
        sub += float(sample[1])
        sum += float(sample[1])*3
    elif(sample[2]=='C+') :
        sub += float(sample[1])
        sum += float(sample[1])*2.5
    elif(sample[2]=='C0') :
        sub += float(sample[1])
        sum += float(sample[1])*2
    elif(sample[2]=='D+') :
        sub += float(sample[1])
        sum += float(sample[1])*1.5
    elif(sample[2]=='D0') :
        sub += float(sample[1])
        sum += float(sample[1])*1
    # elif(sample[2]=='P') :
    #     sum += float(sample[1])*0
    elif(sample[2]=='F') :
        sub += float(sample[1])
        sum += float(sample[1])*0
print(sum/sub)