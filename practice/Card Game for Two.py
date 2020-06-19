N = int(input())
An = list(map(int,input().split()))

totalA = 0
totalB = 0
while (0 < len(An)):
  pointA = max(An)
  totalA += pointA
  An.remove(pointA)
  if 0 < len(An):
    pointB = max(An)
    totalB += pointB
    An.remove(pointB)
print(totalA - totalB)