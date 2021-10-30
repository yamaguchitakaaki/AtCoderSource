N, C = map(int, input().split())
a = [input().split() for l in range(N)]
cnt = 0
data = [0] * 10**9
for i in range(N):
    data[int(a[i][0])] += int(a[i][2])
    data[int(a[i][1])+1] -= int(a[i][2])
ruiseki = [0] * 10**9
ruiseki[0] = data[0]
for i in range(1, 10**9):
    ruiseki[i] = ruiseki[i-1] + data[i]
    if (ruiseki[i] >= C):
        cnt += C
    else:
        cnt += ruiseki[i]
print(cnt)