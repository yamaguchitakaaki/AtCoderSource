# Sの入力
S = input()
# Tの入力
T = input()

boolean = True

for i in range(len(S)):
  if (S[i] != T[i]):
    boolean = False

if (len(S) + 1 != len(T)):
  boolean = False

if (boolean):
  print('Yes')
else:
  print('No')