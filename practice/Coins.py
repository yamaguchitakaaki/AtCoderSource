#  Aの取得
a = int(input())
#  Bの取得
b = int(input())
#  Cの取得
c = int(input())
#  Xの取得
x = int(input())

cnt = 0

for i in range(a+1):
  for j in range(b+1):
    for k in range(c+1):
      if x == (500 * i + 100 * j + 50 * k):
        cnt+=1
print(cnt)