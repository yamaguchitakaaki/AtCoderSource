N = int(input())
L = list(map(int, input().split()))

L.sort()
cnt = 0
for i in range(len(L)):
    for j in range(i+1,len(L)):
        for k in range(j+1,len(L)):
            if L[k] < (L[j] + L[i]) and L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                cnt = cnt + 1
print(cnt)
