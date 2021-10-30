Y = list(map(int, input().split()))

N = Y[0]
X = Y[1]
S = input()

for i in range(len(S)):
    if S[i] == "o":
        X += 1
    else:
        if X > 0:
            X -= 1
print(X)