N = int(input())
A = list(map(int,input().split()))
Q = int(input())
B=[]
C=[]

for _ in range(Q):
    bi, ci = list(map(int, input().split()))
    B.append(bi)
    C.append(ci)

dic = {}
for i in A:
    dic[i] = dic.get(i,0) + 1

sum = sum(A)

for i in range(Q):
    sum += dic.get(B[i], 0) * (C[i] -B[i])
    dic[C[i]] = dic.get(C[i], 0) + dic.get(B[i], 0)
    dic[B[i]] = dic.get(B[i], 0)
    dic[B[i]] = 0
    print(sum)