N,K=map(int,input().split())
n = []
for i in range(1 , N +1):
  n.append(i)


for i in range(K):
  di = int(input())
  arr= list(map(int,input().split()))
  for j in arr:
    if(j in n):
      n.remove(j)

print(len(n))