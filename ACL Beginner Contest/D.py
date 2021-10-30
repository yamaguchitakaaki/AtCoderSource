N,K = map(int, input().split())
A = [int(input()) for i in range(N)]
B = []
for i in range(len(A)):
    if i == (len(A) - 1):
        print(i)
        break
    else:
        print('初手' + str(i))
        if A[i] + K >= A[i+1] and A[i] - K <= A[i+1]:
            B.append(A[i])
        else:
            i += 1
print(B)           
print(len(B))