N, M = map(int, input().split())
AB = [map(int, input().split()) for _ in range(M)]
A, B = [list(i) for i in zip(*AB)]

K = int(input())
CD = [map(int, input().split()) for _ in range(K)]
C, D = [list(i) for i in zip(*CD)]

result = 0
for i in range(2 ** K):
    resultList = [0] * N
    cnt = 0
    
    binary = bin(i)
    trueBin = ''
    for i in range(2,len(binary)):
        trueBin += binary[i]
    bin_zero = trueBin.zfill(K)

    for j in range(len(bin_zero)):
        if(bin_zero[j] == '0'):
            resultList[(C[j] - 1)] += 1
        else:
            resultList[(D[j] - 1)] += 1
    for h in range(M):
        if(resultList[A[h]-1] > 0 and resultList[B[h]-1] > 0):
            cnt += 1
    if(result<cnt):
        result = cnt
print(result)