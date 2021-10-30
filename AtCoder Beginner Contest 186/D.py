N = int(input())
A = list(map(int, input().split()))
sortedA = sorted(A)
cntPlus = 0
cntMinus = 0
for i in range(len(sortedA)):
    cntPlus += sortedA[i] * (N - (i+1))
    cntMinus += sortedA[i] * i
print(cntMinus - cntPlus)