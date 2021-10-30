import copy
N, S = input().split()
N = int(N)
result = 0
data = [0,0,0,0]
rukieiwadata = [[0,0,0,0]]
for i in range(N):
    if (S[i] == 'A'):
        data[0] = data[0] + 1
    elif (S[i] == 'G'):
        data[1] = data[1] + 1
    elif (S[i] == 'C'):
        data[2] = data[2] + 1
    else:
        data[3] = data[3] + 1
    rukieiwadata.append(copy.copy(data))
for i in range(N+1):
    for j in range(i+1,N+1):
        if ((rukieiwadata[j][0] - rukieiwadata[i][0]) == (rukieiwadata[j][3] - rukieiwadata[i][3]) and (rukieiwadata[j][1] - rukieiwadata[i][1]) == (rukieiwadata[j][2] - rukieiwadata[i][2])):
            print(rukieiwadata[j])
            print(rukieiwadata[i])
            result += 1
print(result)