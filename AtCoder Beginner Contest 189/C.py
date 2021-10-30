N = int(input())
A = list(map(int,input().split()))
max = 0
maxA = 0
for i in range(N):
    for j in range(i+1,N):
        if A[i] > A[j]:
            maxA = A[i] * (j - i)
            if max < maxA:
                max = maxA
            break
        elif(j == N -1):
            maxA = A[i] * (j - i + 1)
            if max < maxA:
                max = maxA
            break
print(max)