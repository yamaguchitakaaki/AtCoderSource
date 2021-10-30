N, X = map(int, input().split())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
for i in range(N):
    X -= x[i] * y[i] / 100
    if X < 0:
        print(i+1)
        break
if X >= 0:
    print(-1)