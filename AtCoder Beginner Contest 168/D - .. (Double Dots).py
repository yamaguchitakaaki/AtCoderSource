# N Mの入力
N, M = map(int, input().split())

ab = [map(int, input().split()) for _ in range(M)]
a, b = map(list, zip(*ab))

l = [0] * N

for i in range(M):
  if (a[i] == 1):
    l[b[i]] = 1
  elif (b[i] == 1):
    l[a[i]] = 1

