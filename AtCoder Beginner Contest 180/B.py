import math

N = int(input())
X = list(map(int, input().split()))

man = 0
for i in range(N):
    man += abs(X[i])
print(man)
yuu = 0
for i in range(N):
    yuu += X[i]**2

print(math.sqrt(yuu))
tye = abs(X[0])
for i in range(N):
    if tye < abs(X[i]):
        tye = abs(X[i])
print(tye)
