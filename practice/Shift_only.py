#  Nの取得
n = int(input())

# Anをn個を取得する
AList = list(map(int, input().split()))
list = []
for idx,elem in enumerate(AList):
  cnt = 0
  while (elem % 2 == 0):
    elem = elem / 2
    cnt = cnt + 1
  list.append(cnt)
list.sort()
print(list[0])