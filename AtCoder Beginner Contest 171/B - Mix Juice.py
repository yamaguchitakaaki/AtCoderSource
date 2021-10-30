N,K = map(int,input().split())
P = list(map(int,input().split()))

P.sort()
result = 0
for i in range(K):
    result = result + P[i]
print(result)
