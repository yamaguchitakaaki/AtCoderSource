N = int(input())

AB = [map(int, input().split()) for _ in range(N)]
A, B = map(list, zip(*AB))

listXmin = []
listXmax = []
maxXi = 0
minXi = 10 ** 10
for i in range(N):
    listXmin.append(A[i])
    listXmax.append(B[i])

listXmin.sort()
listXmax.sort()
if N % 2 == 0:
    centrali = int(N / 2) - 1
    centralinext = int(N / 2)
    print(((listXmax[centrali] + listXmax[centralinext]) - (listXmin[centrali] + listXmin[centralinext])) + 1)
else:
    centrali = int((N + 1) / 2) - 1
    print(listXmax[centrali] - listXmin[centrali] + 1)