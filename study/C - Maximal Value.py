
N = int(input())
B = list(map(int,input().split()))

result = B[0]
for i in range(len(B)):
    if i == 0:
        result += B[0]
    elif i == len(B) - 1:
        result += B[i]
    elif(B[i] >= B[i+1]):
        result += B[i+1]
    else:
        result += B[i]

print(result)ß