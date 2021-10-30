N = int(input())
cnt  = 0
for i in range(1, N+1):
    Nstr = str(i)
    if ('7' in Nstr):
        cnt += 1
        continue
    N8Str  = oct(i)
    if ('7' in N8Str):
        cnt += 1
print(N -cnt)