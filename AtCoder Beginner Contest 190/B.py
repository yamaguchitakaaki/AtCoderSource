N, S, D = map(int, input().split())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
result = 'No'
for i in range(N):
    if(x[i] < S and y[i] > D):
        result = 'Yes'
print(result)