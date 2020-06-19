# Kの入力
K = int(input())
# A Bの入力
A, B = map(int, input().split())

boolean = False

for i in range(A ,B + 1):
  if(i % K == 0):
    print("OK")
    boolean = True
    break

if(not boolean):
  print("NG")
