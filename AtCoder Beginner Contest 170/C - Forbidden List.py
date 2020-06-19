X,N = map(int,input().split())
P = list(map(int,input().split()))

result = 0
if N == 0:
    result = X
else:
    list = [i for i in range(201)]
    for i in P:
        list.remove(i)
    if len(list) == 0:
        result = 0
    else:
        min = 100
        for i in list:
            if min > abs(X-i):
                min = abs(X - i)
                result = i
print(result)