N = int(input())
A = list(map(int, input().split()))
sum = 0
for i in range(N):
    if i == 0:
        continue
    else:
        if A[i-1] <= A[i]:
            ## 身長が後ろの方が高く補正がいらない時はそのまま
            continue
        else:
            height = A[i-1] - A[i]
            A[i] = A[i-1]
            sum += height
print(sum)