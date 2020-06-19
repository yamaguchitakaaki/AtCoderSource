N,K = map(int,input().split())
A = list(map(int,input().split()))


if K > 1000:
    A = [N] * N
else:
    for count in range(K):
        B = [0] * N
        for i in range(N):
            # i - A[i]以上、i + A[i]以下のBの要素に1を足す
            startIndex = i - A[i]
            endIndex = i + A[i -1]
            if startIndex < 0:
                startIndex = 0
            if N < endIndex:
                endIndex = N - 1
            
            if startIndex <= i and i <= endIndex:
                B[i] = B[i] + 1
        A = B

A=[str(a) for a in A]
A = ' '.join(A)
print(A)
