N,M =map(int,input().split())
H = list(map(int,input().split()))
ab = [map(int, input().split()) for _ in range(M)]
a, b = map(list, zip(*ab))

cnt = 0
removeList = []

for i in range(len(a)):
  if (H[a[i]-1] > H[b[i]-1]):
    removeList.append(b[i])
  elif (H[a[i]-1] < H[b[i]-1]):
    removeList.append(a[i])
  else:
    removeList.append(a[i])
    removeList.append(b[i])

set(removeList)
print(N - len(set(removeList)))
