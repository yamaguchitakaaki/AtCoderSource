import itertools
H,W,K = map(int, input().split())
C = [input().split() for l in range(H)]

for i in range(len(C)):
    D = [] 
    for j in range(W):
        D.append(C[i][0][j])
    C[i] = D

yokohani = list(range(W))
tatehani = list(range(H))
cnt = 0
for i in range(W):
    for yokokumi in itertools.combinations(yokohani, i):
        for j in range(H):
            for tatekumi in itertools.combinations(tatehani, j):
                
                print(tatekumi)