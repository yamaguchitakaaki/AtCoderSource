X, Y = map(int, input().split())
a = abs(X-Y)
if a < 3:
    print('Yes')
else:
    print('No')