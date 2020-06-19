from math import floor
A, B, N = map(int, input().split())
maxResult = 0

for x in range(N + 1):
  result = floor((A * x)/B) - A * floor(x/B)
  if (maxResult < result):
    maxResult = result
print(maxResult)