N, A, B = map(int, input().split())


total = 0
for i in range (N + 1):
  # X = i // 1000 + (i % 1000) // 100 +((i % 1000) % 100) // 10 + (((i % 1000) % 100) % 10)
  X = sum(map(int, str(i)))
  if A <= X and X <= B:
    total += i
print(total)