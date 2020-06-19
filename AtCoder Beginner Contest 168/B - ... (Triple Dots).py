# Kの入力
K = int(input())
# Sの入力
S = input()

if (len(S) <= K):
  print(S)
else:
  print(S[0:K] + '...')