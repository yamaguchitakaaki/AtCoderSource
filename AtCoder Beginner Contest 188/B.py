N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0
for i in range(N):
    cnt += A[i] * B[i]
if cnt == 0:
    print('Yes')
else:
    print('No')