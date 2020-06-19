import copy
import math
# Nの入力
N = int(input())
A = list(map(int,input().split()))
A.sort()
inf=10**6+1
t=[True for i in range(inf)]

ans=0
for j in range(N):
    if j+1<=N-1 and t[A[j]]:
        if A[j+1]!=A[j]:
            ans+=1
        else:
            t[A[j]]=False
        for numb in range(A[j],inf,A[j]):
            t[numb]=False
    elif j==N-1 and t[A[j]]:
        ans+=1
 
print(ans)