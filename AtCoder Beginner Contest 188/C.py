N = int(input())
A = list(map(int, input().split()))

if (N==1):
    if(A[0]>A[1]):
        print(2)
    else:
        print(1)
else:
    i = A.index(max(A))
    if i < 2 ** (N-1):
        B = A[2**(N-1):2**N]
        print(B.index(max(B)) + 2**(N-1) + 1)
    else:
        B = A[0:2**(N-1)]
        print(B.index(max(B)) + 1)