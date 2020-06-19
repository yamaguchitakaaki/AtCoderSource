import math
# Xの入力
X = int(input())
crdit = 100
cnt = 0

while crdit < X:
  crdit = math.floor(crdit * 1.01)
  cnt += 1
print(cnt)