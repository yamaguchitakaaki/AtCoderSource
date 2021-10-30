from collections import deque
N,M,K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cntTime = 0 
result = 0

#Aのみを読む場合
for i in range(len(A)):    
    if cntTime + C[i] <= K:
        cntTime += C[i]
        result += 1
    else:
        lastIndex = i - 1
        break
#Aの途中で終わる場合
A[lastIndex]の時間で2冊以上Bが読めるかどうか



C = []
for i in range(N):
    A[i] 
    for j in range(M):
        B[j]
        if A[i] <= B[j]:
            continue
        else:


C = A + B
C.sort()




cntTime = 0 
result = 0
for i in range(len(C)):
    cntTime += C[i]
    if cntTime <= K:
        result += 1
    else:
        break
print(result)