S = input()
T = input()
result=0
for i in range(len(S)):
    if S[i] != T[i]:
        result += 1
print(result)