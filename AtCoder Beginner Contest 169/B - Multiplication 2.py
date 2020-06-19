# Nの入力
N = int(input())

A = list(map(int, input().split()))

result = 1
if 0 in A:
    result = 0
else:
    for i in A:
        result *= i
        if result > 10 ** 18:
            result = -1
            break
print(result) 
    