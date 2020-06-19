N, M, Q = map(int, input().split())
times = Q
n = []
for i in range(times):
    n.append(input().split())

maxScore = 0
array = []

# 数列Aをarrayとする
for i in range(N):
  array.append(1)
print(array)

score = 0
for j in range(times):
  if(n[j][2] == array[int(n[j][1])] - array[int(n[j][0])]):
    # 満たす時のdiを足す
    score += n[j][3]
if maxScore < score:
  maxScore = score

print(maxScore)